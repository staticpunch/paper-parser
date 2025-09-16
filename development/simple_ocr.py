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



def create_converter(num_threads: int = 32) -> DocumentConverter:
    
    # Create converter with pipeline options
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True
    pipeline_options.ocr_options.lang = ["en"]
    pipeline_options.accelerator_options = AcceleratorOptions(
        num_threads=num_threads, 
        device=AcceleratorDevice.AUTO
    )
    
    return DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )


def convert_document(
    input_path: Path, 
    output_dir: Path, 
    num_threads: int = 32
) -> None:
    converter = create_converter(num_threads)
    
    # Convert document
    print(f"Converting: {input_path}")
    start_time = time.time()
    result = converter.convert(input_path)
    end_time = time.time() - start_time
    print(f"Document converted in {end_time:.2f} seconds.")
    
    # Save output
    output_dir.mkdir(parents=True, exist_ok=True)
    doc_filename = result.input.file.stem
    output_path = output_dir / f"{doc_filename}.md"
    
    with output_path.open("w", encoding="utf-8") as fp:
        fp.write(result.document.export_to_markdown())
    
    print(f"Output saved to: {output_path}")


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert PDF documents to Markdown"
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
        help="Output directory for converted files"
    )
    
    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=32,
        help="Number of processing threads (default: 32)"
    )
    
    
    return parser.parse_args()


def main() -> None:
    """Main function."""
    args = parse_arguments()
    
    # Validate input file
    assert args.input_path.exists()
    assert args.input_path.suffix.lower() == '.pdf'

    # Convert document
    convert_document(
        input_path=args.input_path,
        output_dir=args.output_dir,
        num_threads=args.threads
    )



if __name__ == "__main__":
    main()