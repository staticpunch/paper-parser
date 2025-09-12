# 0. Installation

(To be updated) The core libarary is `docling`.

# 1. PDF -> Text Conversion.

The following script extracts the main text only from a given paper. This means that I will omit any figures, diagram, images and their descriptions in the paper.
```
CUDA_VISIBLE_DEVICES=0 python ocr.py "path/to/filename.pdf" \
      --output-dir "path/to/output" \
```

`run_ocr.sh` is a convenient script to convert all files within an input directory.

# 2. Information Retrieval

(To be updated)
