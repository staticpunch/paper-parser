This tool extracts and structures content from computational biology papers in PDF format. The tool focuses specifically on parsing the RESULTS section, breaking it into individual subsections while also capturing the paper's opening context (title, abstract, and introduction).
- Input: PDF file of a computational biology paper
- Output: JSON file with this structure:
```
{
    "opening": "Combined text from TITLE + ABSTRACT + INTRODUCTION sections",
    "results": [
        {
            "subtitle": "Subsection title from RESULTS section",
            "content": "Full text content of that subsection"
        },
        {
            "subtitle": "Next subsection title from RESULTS section", 
            "content": "Full text content of that subsection"
        }
    ]
}
```

In the next version, this tool will also be in charge of classifying subsection titles into according categories: `FACTUAL`, `MECHANISM`, `SPECULATION`.


The script `run.sh` illustrates how a PDF file is converted into a structured JSON. Simply run `bash run.sh` to test out! There are also some other test files stored in the `./testdata/pdf` directory, you can modify the input path of the PDF file in the `run.sh` to experiment. 
