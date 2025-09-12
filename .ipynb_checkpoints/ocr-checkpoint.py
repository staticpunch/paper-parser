#!/usr/bin/env python3
"""
Document converter using Docling with custom confidence thresholds.
Converts PDF documents to Markdown with configurable filtering.
"""

import argparse
import time
from pathlib import Path
from typing import Dict

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.accelerator_options import AcceleratorOptions, AcceleratorDevice
from docling.datamodel.base_models import InputFormat
from docling.utils.layout_postprocessor import LayoutPostprocessor
from docling_core.types.doc import DocItemLabel


def setup_debug_config(confidence_config: Dict[DocItemLabel, float]) -> Dict:
    """
    Setup confidence filtering configuration.
    
    Args:
        confidence_config: Dictionary mapping DocItemLabel to confidence thresholds
        
    Returns:
        Dictionary containing original and custom threshold configurations
    """
    original_thresholds = LayoutPostprocessor.CONFIDENCE_THRESHOLDS.copy()
    custom_thresholds = original_thresholds.copy()
    
    # Set impossible thresholds (>1.0) for labels not in your config
    for label in DocItemLabel:
        if label not in confidence_config:
            custom_thresholds[label] = 2.0  # Impossible threshold
        else:
            custom_thresholds[label] = confidence_config[label]
    
    return {
        'original_thresholds': original_thresholds,
        'custom_thresholds': custom_thresholds,
    }


def create_custom_converter(debug_config: Dict, num_threads: int = 32) -> DocumentConverter:
    """
    Create converter with custom confidence thresholds.
    
    Args:
        debug_config: Configuration dictionary from setup_debug_config
        num_threads: Number of threads for processing
        
    Returns:
        Configured DocumentConverter instance
    """
    # Apply custom thresholds
    LayoutPostprocessor.CONFIDENCE_THRESHOLDS = debug_config['custom_thresholds']
    
    # Create converter with pipeline options
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True
    pipeline_options.ocr_options.lang = ["en"]
    pipeline_options.layout_options.create_orphan_clusters = False # important as this is for deleting figures and other unimportant elements.
    pipeline_options.accelerator_options = AcceleratorOptions(
        num_threads=num_threads, 
        device=AcceleratorDevice.AUTO
    )
    
    return DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )


def restore_thresholds(debug_config: Dict) -> None:
    """Restore original confidence thresholds."""
    LayoutPostprocessor.CONFIDENCE_THRESHOLDS = debug_config['original_thresholds']


def convert_document(input_path: Path, output_dir: Path, confidence_config: Dict[DocItemLabel, float], 
                    num_threads: int = 32) -> None:
    """
    Convert a document with custom confidence configuration.
    
    Args:
        input_path: Path to input document
        output_dir: Directory for output files
        confidence_config: Confidence threshold configuration
        num_threads: Number of processing threads
    """
    # Setup configuration
    debug_config = setup_debug_config(confidence_config)
    
    try:
        # Create converter
        custom_converter = create_custom_converter(debug_config, num_threads)
        
        # Convert document
        print(f"Converting: {input_path}")
        start_time = time.time()
        result = custom_converter.convert(input_path)
        end_time = time.time() - start_time
        print(f"Document converted in {end_time:.2f} seconds.")
        
        # Save output
        output_dir.mkdir(parents=True, exist_ok=True)
        doc_filename = result.input.file.stem
        output_path = output_dir / f"{doc_filename}.md"
        
        with output_path.open("w", encoding="utf-8") as fp:
            fp.write(result.document.export_to_markdown())
        
        print(f"Output saved to: {output_path}")
        
    finally:
        # Always restore original thresholds
        restore_thresholds(debug_config)


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert PDF documents to Markdown using Docling with custom confidence thresholds"
    )
    
    parser.add_argument(
        "input_path",
        type=Path,
        help="Path to input PDF file"
    )
    
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=Path("./output"),
        help="Output directory for converted files (default: ./output)"
    )
    
    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=32,
        help="Number of processing threads (default: 32)"
    )
    
    parser.add_argument(
        "--section-header-threshold",
        type=float,
        default=0.8,
        help="Confidence threshold for section headers (default: 0.8)"
    )
    
    parser.add_argument(
        "--text-threshold",
        type=float,
        default=0.95,
        help="Confidence threshold for text (default: 0.95)"
    )
    
    # parser.add_argument(
    #     "--table-threshold",
    #     type=float,
    #     default=0.9,
    #     help="Confidence threshold for tables (default: 0.9)"
    # )
    
    # parser.add_argument(
    #     "--title-threshold",
    #     type=float,
    #     default=0.85,
    #     help="Confidence threshold for titles (default: 0.85)"
    # )
    
    return parser.parse_args()


def main() -> None:
    """Main function."""
    args = parse_arguments()
    
    # Validate input file
    if not args.input_path.exists():
        print(f"Error: Input file '{args.input_path}' does not exist.")
        return
    
    if not args.input_path.suffix.lower() == '.pdf':
        print(f"Warning: Input file '{args.input_path}' may not be a PDF.")
    
    # Build confidence configuration from arguments
    confidence_config = {
        DocItemLabel.SECTION_HEADER: args.section_header_threshold,
        DocItemLabel.TEXT: args.text_threshold,
        # DocItemLabel.TABLE: args.table_threshold,
        # DocItemLabel.TITLE: args.title_threshold,
    }
    
    # Convert document
    try:
        convert_document(
            input_path=args.input_path,
            output_dir=args.output_dir,
            confidence_config=confidence_config,
            num_threads=args.threads
        )
    except Exception as e:
        print(f"Error during conversion: {e}")
        return


if __name__ == "__main__":
    main()