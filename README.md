# 0. Installation

(To be updated) The core libarary is `docling`.

# 1. PDF -> Text Conversion.

The following script extracts the main text only from a given paper. This means that I will omit any figures, diagram, images and their descriptions in the paper.
```
CUDA_VISIBLE_DEVICES=0 python ocr.py "path/to/filename.pdf" "path/to/output_dir" \
```

# 2. Information Retrieval

To extract the RESULTS section and parse its all subsections within a paper, refer to `run.sh` script.
