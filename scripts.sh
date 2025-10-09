# Convert to markdown.
## Example 01
PDF_FILE="./testdata/pdf_v2/t01.pdf"
OUTPUT_DIR="./output"

base_name=$(basename "$PDF_FILE")
base_name_no_ext="${base_name%.pdf}"
md_file="$OUTPUT_DIR/${base_name_no_ext}.md"

python ocr.py "$PDF_FILE" "$OUTPUT_DIR"

## Example 02
python ocr.py "/mnt/disk2/hiennm/practice/paper-parser/testdata/pdf_v2/01.pdf" "./output"