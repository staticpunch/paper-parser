#!/bin/bash

# Directory containing the PDF files
TESTDATA_DIR="./testdata"

# Output directory for the markdown files
OUTPUT_DIR="./markdown/ocr"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through all PDF files in the testdata directory
for pdf_file in "$TESTDATA_DIR"/*.pdf; do
  # Check if the file exists to avoid errors if the directory is empty
  if [ -f "$pdf_file" ]; then
    # Get the base name of the file
    base_name=$(basename "$pdf_file")
    
    # Print the file being processed
    echo "Processing $base_name..."
    
    # Run the ocr.py script
    CUDA_VISIBLE_DEVICES=0 python ocr.py "$pdf_file" \
      --output-dir "$OUTPUT_DIR" \
      --threads 32 \
      --section-header-threshold 0.85 \
      --text-threshold 0.95
      
    echo "Finished processing $base_name."
    echo "---------------------------------"
  fi
done