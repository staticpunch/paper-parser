#!/usr/bin/env python3
"""
Simple layout visualization script using docling.

Usage:
    python layout_viz.py input_file.pdf annotated_file.pdf

This script processes a PDF document with docling's layout analysis
and creates an annotated version showing detected layout elements.
"""

import sys
import logging
from pathlib import Path
from PIL import Image

from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.settings import settings
from docling.utils.visualization import draw_clusters


def setup_logging():
    """Setup basic logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def create_annotated_pdf(input_file: Path, output_file: Path):
    """
    Process PDF with layout analysis and create annotated visualization.
    
    Args:
        input_file: Path to input PDF file
        output_file: Path to save annotated PDF
    """
    logger = logging.getLogger(__name__)
    
    # Enable layout visualization in debug settings
    settings.debug.visualize_layout = True
    settings.debug.debug_output_path = str(output_file.parent / "debug_output")
    
    # Configure pipeline options for layout analysis
    pipeline_options = PdfPipelineOptions(
        # Enable components needed for layout analysis
        do_table_structure=True,
        do_ocr=True,
        # Generate page images for visualization
        generate_page_images=True,
        # Optional: enable other enrichments
        do_picture_classification=False,
        do_code_enrichment=False,
        do_formula_enrichment=False,
    )
    
    # Initialize document converter with proper format options
    from docling.document_converter import PdfFormatOption
    
    converter = DocumentConverter(
        allowed_formats=[InputFormat.PDF],
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    
    logger.info(f"Processing document: {input_file}")
    
    try:
        # Convert document
        result = converter.convert(input_file)
        
        if result.status.name != "SUCCESS":
            logger.error(f"Conversion failed with status: {result.status}")
            return False
            
        logger.info(f"Successfully processed {len(result.document.pages)} pages")
        
        # Create annotated images for each page
        annotated_images = []
        
        for page_num, page in enumerate(result.document.pages, 1):
            logger.info(f"Processing page {page_num}")
            
            # Get page image
            if hasattr(page, '_backend') and page._backend:
                page_image = page.get_image(scale=1.0)
                if page_image is None:
                    logger.warning(f"Could not get image for page {page_num}")
                    continue
            else:
                logger.warning(f"No backend available for page {page_num}")
                continue
            
            # Get layout predictions (clusters)
            if page.predictions and page.predictions.layout:
                clusters = page.predictions.layout.clusters
                
                # Calculate scaling factors
                scale_x = page_image.width / page.size.width if page.size else 1.0
                scale_y = page_image.height / page.size.height if page.size else 1.0
                
                # Create annotated image
                annotated_image = page_image.copy()
                draw_clusters(annotated_image, clusters, scale_x, scale_y)
                
                annotated_images.append(annotated_image)
                
                logger.info(f"Page {page_num}: Found {len(clusters)} layout elements")
                
                # Log detected element types
                element_types = {}
                for cluster in clusters:
                    elem_type = cluster.label.name
                    element_types[elem_type] = element_types.get(elem_type, 0) + 1
                
                logger.info(f"Page {page_num} elements: {element_types}")
            else:
                logger.warning(f"No layout predictions for page {page_num}")
                annotated_images.append(page_image)
        
        if not annotated_images:
            logger.error("No images were processed successfully")
            return False
        
        # Save annotated images as PDF
        if len(annotated_images) == 1:
            # Single page
            annotated_images[0].save(str(output_file), "PDF", resolution=100.0)
        else:
            # Multiple pages
            annotated_images[0].save(
                str(output_file), 
                "PDF", 
                resolution=100.0,
                save_all=True, 
                append_images=annotated_images[1:]
            )
        
        logger.info(f"Annotated PDF saved to: {output_file}")
        
        # Also save individual page images for inspection
        debug_dir = output_file.parent / "debug_output"
        if debug_dir.exists():
            logger.info(f"Debug images available in: {debug_dir}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error processing document: {e}")
        return False


def main():
    """Main function to handle command line arguments and run the visualization."""
    if len(sys.argv) != 3:
        print("Usage: python layout_viz.py input_file.pdf annotated_file.pdf")
        print("\nExample:")
        print("    python layout_viz.py document.pdf document_annotated.pdf")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])
    
    # Validate input file
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)
    
    if not input_file.suffix.lower() == '.pdf':
        print(f"Error: Input file must be a PDF. Got: {input_file.suffix}")
        sys.exit(1)
    
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("Docling Layout Visualization Tool")
    logger.info("=" * 40)
    
    # Process the document
    success = create_annotated_pdf(input_file, output_file)
    
    if success:
        logger.info("✅ Layout visualization completed successfully!")
        print(f"\n📄 Annotated PDF saved to: {output_file}")
        
        # Check for debug output
        debug_dir = output_file.parent / "debug_output"
        if debug_dir.exists():
            print(f"🔍 Debug images saved to: {debug_dir}")
            
    else:
        logger.error("❌ Layout visualization failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()