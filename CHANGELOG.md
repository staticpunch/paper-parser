# 16/09/2025

## Objective
Extract essential content from computational biology papers, specifically section titles and main text, while excluding figures, diagrams, images, and their descriptions.

## Approaches Investigated

### 1. LayoutPostprocessor Patching
**Method:** Monkey patch `LayoutPostprocessor.CONFIDENCE_THRESHOLDS` to filter unwanted content types.

**Implementation Steps:**
1. **Initialize DocumentConverter**
   ```python
   pipeline_options = PdfPipelineOptions()
   doc_converter = DocumentConverter(
       format_options={
           InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
       }
   )
   ```

2. **Pipeline Selection**
   DocumentConverter uses StandardPdfPipeline by default:
   ```python
   def _get_default_option(format: InputFormat) -> FormatOption:
       format_to_default_options = {
           ...,
           InputFormat.PDF: FormatOption(
               pipeline_cls=StandardPdfPipeline, 
               backend=DoclingParseV4DocumentBackend
           ),
           ...
       }
   ```

3. **Processing Chain**
   StandardPDFPipeline → LayoutModel → LayoutPostprocessor.process() → filtering based on CONFIDENCE_THRESHOLDS

4. **Issue Encountered**
   Filtering unwanted labels (headers, footnotes, etc.) creates orphan clusters that get rebranded as `text`. 
   
   **Workaround:** Disabled orphan cluster inclusion by commenting `clusters.extend(orphan_clusters)` in LayoutPostprocessor.

**Result:** Robust approach, but requires native support for excluding unwanted clusters.

---

### 2. Component Masking Approach
**Method:** 
- Mask components that are not SECTION_HEADER or TEXT
- Apply OCR to masked content

**Issues:**
- Works well with native PDFs but struggles with images saved as PDFs
- Increased processing time
- Disrupted reading order

**Result:** Not effective for the target use case.

---

### 3. ReadingOrderModel Patching
**Method:** Modify the `__call__` method of ReadingOrderModel to actively exclude clusters that are not TEXT or SECTION_HEADER.

**Implementation:** Combined with LayoutPostprocessor patching from Approach 1.

**Result:** Similar performance to Approach 1, potentially more robust due to dual-layer filtering.