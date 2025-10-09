import os
from pathlib import Path

condition_template = """
**[START OF ARTICLE]**
```
{{text}}
```
**[END OF ARTICLE]**

You are a scientific data curator responsible for summarizing experimental designs from research articles. Your task is to identify the 'Control Condition' and the 'Extra Perturbed Condition' from a given paper.

### Instructions:
1.  **Control Condition:** Identify the baseline state or reference group used for comparison. This is typically the "normal" or unmanipulated sample, such as a wild-type (WT) organism/cell line, a vehicle-treated group (e.g., DMSO), or a mock-transfected group.
2.  **Extra Perturbed Condition:** Identify the primary experimental variable or intervention being tested against the control. This is the main change introduced to test the paper's hypothesis, such as a gene knockout (KO) or knockdown (KD), a drug treatment, or the overexpression of a protein.
3.  Focus on the central experiment that defines the paper's main conclusion. If the paper describes multiple experiments, extract the conditions from the one that is most central to the overall story (often a key 'omics' experiment like RNA-seq or a primary functional assay).
4.  **Be Concise:** Keep your descriptions brief and to the point, mirroring the style of the following examples.

### Few-shot Examples:
| Publication tittle | Experiment type | Control condition | Extra perturbed condition |
| :--- | :--- | :--- | :--- |
| The transcription factor SP1 orchestrates metabolic reprogramming in response to glucose starvation | RNA-seq | HepG2 | SP1 KO |
| A novel long non-coding RNA, NEBULA, regulates neuronal differentiation in the developing cortex | RNA-seq | Mouse primary cortical neurons | NEBULA KD |
| Cross-talk between the Hippo and Wnt pathways is mediated by the kinases LATS1 and LATS2 | RNA-seq | MCF-7 | LATS1 KD, LATS2 KD |
| Epigenetic silencing by PRC2 is essential for maintaining pluripotency in human embryonic stem cells | RNA-seq | H9 hESCs | EZH2-/- |
| A screen identifies SMARCA4 as a key regulator of the T-cell immune checkpoint response | RNA-seq | Jurkat T cells | SMARCA4 OE |
| Metformin treatment reverses age-associated transcriptional changes in the liver | RNA-seq | C57BL/6 liver (24 months) | treated with metformin |
| The RNA helicase DDX3 promotes translation of oncogenic transcripts in glioblastoma | RNA-seq | U-87 MG | DDX3 KO, DDX3 over-expressing |
| A comprehensive map of alternative splicing events during zebrafish embryogenesis | RNA-seq | Zebrafish embryo (24 hpf) | None |
| Phase separation of FUS protein drives aberrant stress granule formation in motor neurons | RNA-seq | iPSC-derived motor neurons | FUS P525L mutant |
| The DNA damage response kinase ATM regulates alternative polyadenylation to control mRNA stability | RNA-seq | U2OS | treated with doxorubicin, ATM inhibitor |

### Your Task:
Analyze the provided article and extract the required information based on the instructions and examples above. Provide your answer in the following format:
`| Publication tittle | Experiment type | Control condition | Extra perturbed condition |`
""".strip()


if __name__ == "__main__":
    markdown_dir = Path("../output/v2/markdown")
    prompts_dir = Path("./output/v2/prompts")
    
    prompts_dir.mkdir(parents=True, exist_ok=True)
    
    for md_file in sorted(markdown_dir.glob("*.md")):
        print(f"Processing {md_file}...")
        text = md_file.read_text(encoding='utf-8')
        prompt = condition_template.replace("{{text}}", text)
        output_file = prompts_dir / f"{md_file.stem}.txt"
        output_file.write_text(prompt, encoding='utf-8')