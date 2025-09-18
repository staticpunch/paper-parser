#!/bin/bash

PDF_FILE="./testdata/pdf/05.pdf"
OUTPUT_DIR="./output"

base_name=$(basename "$PDF_FILE")
base_name_no_ext="${base_name%.pdf}"
md_file="$OUTPUT_DIR/${base_name_no_ext}.md"

python ocr.py "$PDF_FILE" "$OUTPUT_DIR"
python structure.py "$md_file" "$OUTPUT_DIR"
