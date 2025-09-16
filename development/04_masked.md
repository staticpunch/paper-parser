## An Integrated Systems Biology Approach Identifies TRIM?5 as a Key Determinant of Breast Cancer Metastasis

Graphical Abstract

Highlights

Authors

## Correspondence

## In Brief

Aberrantly activated transcriptional networks drive metastatic dissemination: Walsh et al. reverse engineer a breast cancer-specific regulatory network; uncovering a transcriptional hierarchy underlying breast cancer metastasis: Findings suggest that collapsing transcriptional hierarchies by targeting keystone proteins, such as TRIM25, is critical to affect the coordinated transcriptomic reprogramming required for metastasis:

Logan A. Walsh; ',11 Mariano J. Alvarez,?,3,11 Erich Y. Sabio, Marsha Reyngold; Vladimir Makarov,' Suranjit Mukherjee; Ken-Wing Lee;' Alexis Desrichard, Sevin Turcan; Martin G. Dalin;' Vinagolu K. Rajasekhar;6 Shuibing Chen; Linda T. Vahdat; Andrea Califano,2, and Timothy A Chan',4,8,9,10,12,

## SUMMARY

At the root of most fatal malignancies are aberrantly activated transcriptional networks that drive metastatic dissemination: Although individual metastasis-associated genes have been described, the complex regulatory networks pre siding over the initiation and maintenance of metastatic tumors are still poorly understood: There is untapped value in identifying therapeutic targets that broadly govern coordinated transcriptional modules  dictating metastatic gression. Here, we reverse engineered and interrogated a breast cancer-specific transcriptional interaction network (interactome) to define transcriptional control structures causally responsible for regulating genetic programs underlying breast cancer metastasis in individual   patients: Our analyses confirmed established pro-metastatic   transcription   factors, and uncovered TRIM25 as a regulator of metastasis-related transcriptional programs: Further, in vivo analyses established TRIM25 as a potent regulator of metastatic disease and poor survival outcome Our findings   suggest that identifying and targeting keystone proteins; like TRIM25, can effectively collapse transcriptional hierarchies necessary for metastasis   formation, thus representing an innovative cancer intervention strategy: prothey key

## INTRODUCTION

Metastatic   progression is the primary   underlying cause of breast cancer-associated death (Spano et al,, 2012). Although both functional and genomic studies have identified important genetic aberrations associated with risk of malignant   progression (Navin; 2015) , the fundamental drivers and the associated complex mechanisms of breast cancer metastasis remain poorly mapped and poorly understood: Specifically; several pathways have been identified as contributors to metastatic disease (Hanahan and Weinberg; 2011), but identification and dissection of the regulatory machinery that is necessary and sufficient to implement metastatic progression (metastasis checkpoints) remain critically unanswered questions in cancer research we approached metastatic progression as a transition between cellular states defined by the differential gene expression signature of these states in the same patient, using patient-matched primary and metastatic   samples Then we investigated the specific transcriptional regulators responsible for initiating this transition; and ultimately for maintaining the stability of the metastatic state, based on their mechanistic ability to regulate differentially expressed the transition  signature): We have shown such cancer-related state transitions can be efficiently and  systematically  elucidated by interrogating tumor-specific transcriptional networks (henceforth interactomes) with representative differential gene expression signatures, using the virtual inference of protein activity by regulon enrichment  analysis (VIPER) algorithm (Alvarez et al,, 2016), which further extends the master regulator inference algorithm two

These validated analyses have helped elucidate master regulator (MR) proteins whose concerted, aberrant activity is both necessary and sufficient for tumor phenotype implementation and maintenance, including tumor initiation (Aytes et al,, 2014; Carro et al, 2010), progression (Aytes et al,, 2014; Lefebvre et al,, 2010), and resistance (Piovan et al,, 2013; Rodriguez-Barrueco et al,, 2015). drug

To implement this approach, first  assembled a breast cancer-specific regulatory network, using the algorithm for the reconstruction of accurate cellular networks (ARACNe) Basso et al: tial expression signatures representing same-patient cell state transitions from primary tumors to lymph node metas tases, using both ER-positive (ER+) and triple-negative breast cancer (TNBC) samples: Finally, we used the VIPER algorithm to prioritize transcriptional regulators that are the most likely causal determinants of these metastasis-related   signatures: Using this strategy, we uncovered a hierarchy of transcriptional regulators  controlling metastatic progression, revealing both previously unknown and well-established pro-metastatic transcription factors, thus confirming the potential value of the proposed methodology: we gene

## RESULTS

## Identifying Keystone Transcriptional Regulators of Breast Cancer Metastasis

To identify the transcriptional machinery driving breast cancer metastasis (Figure 1A), we first characterized the transcriptional signature representative of breast carcinoma metastatic progression (metastasis [MET] gene expression signature [MET GES]) : This was achieved by differential expression analysis of patient-matched primary tumors and Iymph node metastases from 20 ER+ and 11 TNBC patients (Figure SIA; Table S1). Critically, two-tail gene set enrichment analysis (GSEA2) of these signatures revealed strong concordance across the two subtypes, suggesting the existence of common metastatic progression mechanisms (Figures S1B-SID), independent of hormonal state.

To identify the genes that causally implement the MET-GES, thus representing candidate causal determinants of breast carcinoma metastatic progression; we utilized the VIPER algorithm a breast carcinoma-specific interactome, we analyzed 851 The Cancer

Genome Atlas (TCGA) breast carcinoma gene expression profiles using the ARACNe algorithm (Basso et al,, 2005; Margolin et al,, 2006a): ARACNe is an information theory-based approach to infer mechanistic interactions between transcription factors (TFs) and target genes based on large sets of gene expression data, which has proven very effective in assembling interactomes for VIPER analysis (Alvarez et al,, 2016; Basso et al:, 2010; Carro Kushwaha et al:, 2015; Lefebvre et al , 2010). The ARACNe-inferred breast cancer interactome included 1,748 TFs, regulating 18,783 target genes through 365,634 transcriptional interactions. A schematic representation of our pipeline is represented in Figure 1A.

Of the top candidate MRs, most are largely unexplored metastasis-associated genes, ranking significantly higher than wellknown pro-metastatic TFs, such as C-MYC (ranked 585) , ETV4 (ranked 1,443), and SMAD4 (ranked 1,447). Nevertheless, the high ranking of breast cancer-specific metastasis-associated such as PRRX-1 (ranked 6,p = 6.8 x 10 further corroborates the accuracy of our approach. Importantly, top candidate MR genes were not highly differentially expressed  following TFs,

Figure 1. Transcriptome Analysis of Matched Primary Tumors and Lymph Node Metastasis in ER+ and TNBC

(A) Schematic regulators of the metastasis phenotype (MRs) in breast carcinoma, representing the strategy used to generate VIPER-inferred candidate MRs of the metastatic state

Finally; we inferred the regulatory proteins that are candidate drivers of the MET-GES by VIPER analysis of the breast carcinoma interactome The algorithm prioritizes the regulatory proteins that are the most likely determinants of an observed differential expression signature, and thus of the associated cell state transition; by assessing the enrichment of their direct targets (regulons) in differentially expressed signature genes (i.e., in genes that are over- or underexpressed during metastatic progression, in this case): Thus, the ARACNe-inferred regulon of each regulatory protein (Table S2) is used as a highly multiplexed, endogenous reporter for its role in physically controlling We used the statistical significance, estimated by sample permutation analysis, to rank-sort the list of putative MRs of the metastatic phenotype in ER+ breast cancer and TNBC (Table S3). Given the strong concordance between ER+ and TNBC MET-GES and between candidate MRs of the two subtypes (Figures SIB-SID), we inferred the MRs of metastatic progression of breast carcinoma regardless of subtype by VIPER analysis of a subtype-agnostic MET-GES. This generated a single ranked Iist of breast cancer metastatic progression candidate MRs (breast cancer [BRCA]) ; independent of hormonal status (Figure IB; Table S3). From these analyses, TRIM25 emerged by far as the strongest candidate MR (p = 3.25 x 10-5). A schematic summary of these data is shown in Figure SIE:

metastatic progression: In fact, none of the top 15 candidate MR genes were in the 100 most differentially expressed genes, and, therefore, they could not have been identified without direct analysis of their regulatory context: This further emphasizes the distinct advantage of the proposed methodology. As previously shown (Chen et al,, 2014), regulatory proteins with the highest probability to directly regulate the signature of interest are more likely to be critically necessary to implement the associated cell state   transition, because they represent the most proximal integrators (i.e-, regulatory bottlenecks) of genetic and epigenetic determinants of the associated phenotype. This suggests that TRIM25 may be a more universal determinant of metastatic progression in breast cancer as compared to previously identified genes that appear further down in the prioritized MR list. top

We based the analysis on an average gene expression signature of metastatic progression across all ER+ and TNBC METs: Thus, while it is effective in identifying mechanisms that are common across most of the patients, it fails to capture mechanisms that may be patient specific. We thus extended our analysis at the single-patient level by inferring the transcriptional regulators driving each patient's metastatic progression with the VIPER algorithm (Alvarez et al , 2016). This analysis also identified TRIM25 as the most consistently activated regulatorin these metastases (Figure 1C), further supporting its role as a regulator of the metastatic progression in both ER+ and TNBC tumors\_ key

## TRIM25 Is a Global Regulator of Breast Cancer Metastasis Signature

The identification of established metastasis-associated genes, et al,, 2012; Ratkaj etal , 2010; Zhang et al,,2011), demonstrates the robustness of our methodology toward elucidating meta-

To functionally test these hypotheses, we performed small interfering RNA (siRNA)-mediated knockdown for a selected set of 14 MRs in 2 ER+ (MCF7 and T-47D) and 2 TNBC (BT549 and MDAMB-231) cell lines, and we analyzed subsequent changes in gene expression using RNA sequencing (RNA-seq) (Table S4). The MR genes selected for validation represent the top most differentially activated TFs in each of the patient-derived signacarcinoma BRCA MET-GES, the ER+ MET-GES, and the TNBC MET-GES (Figures 1B, 1C, and S2A; Table S3). MRs were prioritized by stepwise linear regression with exhaustive selection to first identify the best combination of MRs controlling the metastatic progression signature and then to compute the fraction of metastasis signature genes regulated by each MR, using GSEA leading-edge analysis (Subramanian et al,, 2005). The best linear combination of n MRs, where n was the highest number of MRs for which all coefficients of the model were different than zero at Bonferroni's corrected p 0.001, was selected by maximizing the variance explained by the model (Figures S2B and S2C; Table S5). Employing a complementary approach, we repeated this analysis by separately comparing the expression between metastasis and primary tumor for each individual patient . Stepwise linear regression with exhaustive search was applied to each gene expression signature and then integrated by the Stouffer method. Results were very similar using either method (Table S5).

static progression drivers. Based on these analyses, TRIM25 emerged as the strongest (i.e., most statistically significant) MR candidate using both TNBC cell lines and patient breast tumor-derived signatures   (Figures S2B and TRIM25 also significantly regulated the ER+ MET-GES in 1 ER+ cell line (Table S5). Critically, siRNA-mediated silencing of TRIM25 strongly affected 50% of the 20 VIPER-inferred candidate MRs (Table S4), demonstrating that TRIM25 can coordinate multiple downstream transcriptional programs to implement the metastatic progression transcriptional signature. The predicted regulatory relationship between TRIM25 and target transcripts is shown in Figure 1D. top

## TRIM25 Expression Is Not Correlated with Estrogen Signaling

TRIM25 was originally named estrogen-responsive finger protein (EFP), and it has since been described as an estrogen-responsive gene and a cO-factor for estrogen signaling: Therefore, the identification most  statistically  significant candidate metastatic progression MR in TNBC was surprising: Yet; when we compared TRIM25 expression in ER+ and TNBC tumors from TCGA, it was actually significantly higher in the latter (Figure S2D): Consistent with these findings, we did not observe estrogen-dependent expression of TRIM25 in multiple high-throughput  studies that test the effects of estrogen on gene expression (Carroll et al,, 2006; Creighton et al,, 2006; Kamalakaran et al , 2005; Lin et al., 2004).

To further investigate the relationship between TRIM25 and estrogen   signaling; we generated a Spearman's correlation matrix using RNA-seq expression data from 1,100 breast cancer tumors, comparing  TRIM25 expression with ten established estrogen-responsive genes (Figure S2E). As expected, Estrogen receptor 1 (ESRI) expression correlated strongly with all ten estrogen-responsive genes. Yet;  despite expressed in ER+ tumors, expression of TRIM25 was not  correlated with the expression of ESRI or other estrogen-responsive genes: For comparison, we also included the Y box-binding protein (YBXI) in these analyses, a gene specifically associated with estrogen-negative tumors. While the analysis revealed significant negative correlation between YBXI expression and the expression of estrogen-responsive genes, as well as ESR1, no correlation was detected with TRIM25 expression.  Taken together, these results suggest that TRIM25 expression can be regulated by factors independent of estrogen or estrogen signaling; especially in TNBCs: being

## TRIM25 Mediates Breast Cancer Metastasis in Human Xenograft Models

To test the effect of TRIM25 on the metastatic potential of TNBC cells, we engineered human MDA-MB-231 cells, derived from a TNBC tumor, to express either high (TRIM25high) or low (TRIM25low) levels of TRIM25 (Figure S3A), and we labeled them with Luc-GFP or Luc-RFP. Distinctly labeled TRIM25high and TRIM2Slow cells were mixed 1:1, injected into the lateral tail vein of athymic nude mice, and monitored for the development of lung metastases via bioluminescence imaging: When lung metastases were visible, mice were sacrificed and their lungs were first imaged via ex vivo fluorescence imaging and spectral unmixing for a global picture of the relative abundance then sectioned and the percentage content of TRIM2Shigh versus TRIM2slow cells was accurately quantified via immunofluorescence (Figures 2B and 2C): We found that TRIM2Shigh cells constituted the overwhelming majority of metastatic   burden in the lungs compared to TRIM25low We confirmed these results in parallel experiments, in which

Intriguingly, increased expression of TRIM25 did not affect proliferation or invasion of MDA-MB-231 cells in vitro (Figures S3B and S3C): We then used a primary culture generated from a patient-derived xenograft (PDX) model of TNBC to test the effect of TRIM25 perturbation on primary tumor growth in vivo. Consistent   with  the in vitro assays, we found that neither TRIM25 knockdown nor overexpression altered primary tumor growth in the mammary fat pad of NOD scid gamma (NSG) mice (Figures S3D-S3F): Similarly, when we injected the aforementioned fluorescently labeled TRIM2Shigh:TRIM2Slow cell mixture into the mammary fat of NSG mice, we found that TRIM25 did not affect cellular proliferation at the orthotopic site, with TRIM25high and TRIM2Slow cells showing uniform representation in primary tumors &gt;1 cm in diameter (Figure 2D): Notably , when these mice became symptomatic and lungs were harvested, we found that TRIMZShigh cells metastasized to the lung more efficiently than TRIM2Slow cells, despite representing a similar fraction in corresponding primary tumors (Figures 2E and 2F): Interestingly, perturbation of TRIM25 expression in MDA-MB-231 cells injected into the mammary fat of NSG mice in limiting dilution   experiments  revealed that TRIM25 knockdown resulted in decreased seeding potential, suggesting TRIM25 may be involved in promoting self-renewal We further explored the relationship between TRIM25 and metastasis in an additional TNBC cell line, CAL-51. TRIM25 knockdown in CAL-51 cells injected into the lateral tail vein of athymic nude mice resulted in significantly decreased lung metastases (Figures 2G and S3H): Lungs were stained with anti-human COX4 to clearly differentiate human CAL-51 metastases from mouse lung tissue (Figure 2G): Overexpression of TRIM25 in CAL-51 cells resulted in an ~2-fold increase in lung metastases (p = 0.10; Figures 2H and S3H): This increase was not due to an increase in extravasapad pad tion (Figure 831). Together these data demonstrate that TRIM25 is a potent regulator of TNBC metastasis.

## The E3 Ubiquitin Ligase Activity of TRIM25 in Promoting Metastasis

To determine whether the E3 ubiquitin ligase domain of TRIM25 was required for TRIM25 to promote metastasis, first we employed a CRISPR strategy to knock out TRIM25 (TKO) in 2 TNBC cell lines (Figures 3A and S4A): Then, we expressed either full-length TRIM25 (TRIM25) or a RING-deficient TRIM25 (TRIMZSAR) in these cells (Figures 3B and 3C). The lack of E3 ubiquitin ligase activity was confirmed in TRIMZ5AR cells (Figure S4B): Tail vein-injected CAL-51-TKO cells expressing either TRIM25 or TRIMZSAR rescued the metastasis phenotype to a similar extent, suggesting that the E3 ubiquitin ligase activity of TRIM25 is not required (at least entirely) for promoting metastasis in this context (Figure 3D). In contrast, orthotopic injection rescued the seeding potential of TNBCs that expressed fulllength TRIM25 (Figure 3E), suggesting that the E3 ubiquitin ligase domain of TRIM25 in part, contribute to tumorigenicity and, therefore, metastatic potential: Interestingly, the expression of TRIM25 or TRIMZSAR did not alter the localization of TRIM25 in TNBCs via immunofluorescence (Figure S4C): Consistent with the role of TRIM25 in promoting metastasis,  expression of TRIM25 or TRIMZSAR (Figure S4D) in an already highly metastatic TNBC line did not significantly affect primary tumor growth or tion of these cells into the lateral tail vein of nude mice revealed no differences in metastatic seeding in the lung (Figure 3H): Together  these data suggest  TRIM25 promotes metastasis through multiple mechanisms, with at least one being independent of its E3 ligase activity: may,

## TRIM25-Mediated Transcriptional Regulation of the MET-GES

Since TRIM25 contains a hallmark   zinc-finger B-box DNAbinding domain (Figure SSA), we hypothesized that it regulates the BRCA metastatic signature, at least in part; as a bona fide TF. Cell fractionation of ER+ breast cancer and TNBC cells revealed that TRIM25 is present in the cytoplasmic, nuclear, and chromatin fractions (Figures 4A and SSB): Immunofluorescence

<!-- image -->

revealed TRIM25 was most abundantly localized to the perinuclear region (Figure 4B): To investigate the DNA-binding properties of TRIM25, we performed chromatin immunoprecipitation sequencing (ChIP-seq) in the TNBC cell lines BT549 and MDA-MB-231\_ TRIM25 ChIP antibody was validated according to Encyclopedia of DNA Elements (ENCODE) guidelines (Landt et al., 2012), and a representative   immunoprecipitation (IP) is shown in Figure SSC. The distribution of ChIP-seq peaks (genome ontology) is shown in Figures 4C and 4D. Interestingly, TRIM25 primarily associated with DNA at CpG islands and gene promoters. Several ChIP targets were selected for validation by qPCR (Figure SSD): When we examined the metastasis signature genes by plotting TRIM25 ChIP-seq reads (input) for the 876 genes (p &lt; 0.05) from the TNBC MET-GES, we observed that TRIM25 mainly localizes to the transcriptional start site (TSS) of these genes (Figures 4E-4H): top

To further refine the identity of genes transcriptionally regulated by TRIM25, we performed iterative GSEA (GSEA) while incrementally   increasing the number of TRIM25-bound genes, based on TSS peak scores, compared to the cell line data in which TRIM25 was silenced (GES) as negative control, The TRIM25-bound gene set was determined as the smallest set for which a maximum GSEA enrichment score could be obtained (Figure 41). These TRIM25-bound genes were significantly enriched in genes that were upregulated   following siRNA-mediated   silencing of TRIM25   (SiTRIM25-GES) , both in BT549 and in MDA-MB-231 cells: This was consistent with TRIM25 functioning, at least in part; as a transcriptional repressor (Figures 4J and 4K): Specific overlap is shown in ures   SSE and SSF and   Table S4. Further,  iGSEA inferred TRIM25-bound genes were significantly enriched among the downregulated MET-GES genes for both BT549 and MDAMB-231 cells, again suggesting that TRIM25 may function as a transcriptional repressor to and 4M): Specific overlap is represented in Figures SSG and SSH and Table S4. top Fig-

## TRIM25 Mediates MET-GES Regulation at the Posttranscriptional Level

TRIM25 is also an established RNA-binding protein (Choudhury interacts with the mRNA of metastasis-associated genes and whether this binding was associated with their expression levels To test this hypothesis, we performed RNA immunoprecipitation sequencing (RIP-seq) in BT549 and MDA-MB-231 cells to identify TRIM25-bound RNA species, which were scored and ranked

(see the Experimental Procedures) We randomly chose 3 positive and 3 negative RIP-seq target genes to confirm as described in the previous section, we detected a strong enrichment of TRIM25-bound RNAs among genes that were elevated upon knockdown of TRIM25 in both MDA-MB-231 and BT549 cells (Figures SB and 5C), suggesting that TRIM25 negatively regulates the abundance of these transcripts The specific overlap is represented in Figures S6B and S6C. Similarly, we found enrichment  of the top iGSEA-inferred TRIM25-bound RNAs among genes that were reduced in the MET-GES, again gesting that TRIM25 may negatively regulate the abundance of these MET-GES genes (Figures 5D and 5E). Specific overlap is represented in Figures S6D and SGE and Table S4. sug-

## TRIM25 Regulates the MET-GES through Transcriptional and Post-transcriptional Mechanisms

To insight into the potentially distinct biological processes mediated by TRIM25 transcriptionally versus post-transcriptionally, we performed pathway enrichment analysis, using Kyoto Encyclopedia of Genes and Genomes (KEGG), Biocarta, and Reactome pathways from the Molecular Signature Database (MSigDB) (Subramanian et al,, 2005) , on these core gene sets\_ gain

Next, we proceeded to examine the  relationship between transcriptional and post-transcriptional   regulation of gene expression, as mediated by TRIM25. First; to identify the core set of genes transcriptionally regulated by TRIM25 in TNBC, we integrated the TRIM25 ChIP-seq results with gene expression changes resulting from TRIM25 knockdown in cell lines. While the former indicates binding of TRIM25 to promoter regions; the latter provides clues about causal regulatory effects on transcription. Confirming our analysis and the ARACNe-inferred regulon of TRIM25, these core genes were significantly enriched in genes downregulated in the MET-GES (Figure S6F): In parallel, we identified a core set of genes post-transcriptionally regulated by TRIM25 in TNBC by integrating the TRIM25 RIP-seq results with gene expression profiles following SiRNAmediated silencing of TRIM25 in TNBC cell lines: This second core gene set; which is post-transcriptionally regulated by TRIM2S, was also significantly enriched in genes downregulated in the MET-GES (Figure S6G). Remarkably, we also found significant overlap between the transcriptional and post-transcriptional TRIM25-regulated core gene sets (Figure 5F), suggesting that TRIM25 regulates the expression of these genes at both transcriptional and post-transcriptional levels, thus implementa classic feedforward loop structure. ing

<!-- image -->

We found a striking overlap between processes regulated by TRIM25 transcriptionally and post-transcriptionally (Figure SG; Table S6) , suggesting that TRIM25 may control these biological processes through tight transcriptional and post-transcriptional mechanisms:

## TRIM25 Promotes Tumorigenicity and a Stemness Phenotype

To assess which cellular processes associated with metastasis are modulated by TRIM25, we first inferred the highest confidence MET-GES genes transcriptionally and post-transcriptionally regulated by TRIM25 as the genes in the leading edge when computing the enrichment of the core set of transcriptionally or post-transcriptionally regulated by TRIM25 on the MET-GES (Figure  SZA): we performed gene ontology (GO) analysis on these gene sets. Enriched biological processes were dominated by developmental processes (Figure 6A), suggesting that  TRIM25 may mediate metastases by affecting differentiation. genes

Next we tested whether altering more than one MR, which together more broadly cover the MET-GES, is   sufficient to enhance tumor implantation in an otherwise poorly tumorigenic breast cancer   cell  line, BT549. that   modulation of TRIM25 and zinc-finger protein 581 (ZNF581) in combination yielded the most  substantial coverage of the MET-GES (61%) compared to all other pairs of candidates (Figures S2B and S2C; Table S5). We therefore overexpressed TRIM25 and knocked down ZNF581 in BT549 cells (Figure S7B) , and we per formed a limiting dilution assay in the mammary fat pads of NSG mice. Concomitant TRIM25 overexpression and ZNF581 knockdown significantly enhanced tumorigenicity (Figure 6B) without affecting  proliferation in an expanded tumor-initiating cell population with this combined genetic alteration. These data suggest that broad coverage of

To further insight into the specific effect of TRIM25 on the phenotype of TNBC cells, we characterized the global transcriptional changes downstream of TRIM25. GSEA was performed on genes identified by RNA-seq to be differentially expressed upon knockdown of TRIM25 in BT549 and MDA-MB-231 cells: Of the 189 MSigDB oncogenic gene signatures tested, we found that the strongest enrichment was a signature related to differentiaof embryonic stem cells (ESCs), suggesting that TRIM25 may be involved in the maintenance of stemness (Figure 6C; Table S7). This is particularly interesting as TRIM2S was previgain tion ously found to be the target of 7 of 9 pluripotency factors in ESCs (Figure 6D) (Kim et al , 2008), and TRIM25 expression is significantly decreased during embryonic differentiation (Kwon et al , 2013).

Across 32 cancer types from TCGA, TRIM25 was rarely deleted and was most frequently amplified in breast cancer (Figures 7A and 7B): TRIM25 amplification was associated with a significant rank test using RNA-seq data consisting of 1,038 breast cancer tumors from TCGA revealed that elevated TRIM25 expression is significantly associated with poor overall survival (Figure 7D): Further, prediction of clinical outcomes from genomic profiles (PRECOG) analysis of TRIM25 confirmed that TRIM25 expression is significantly associated with poor outcome in breast cancer (Figure 7E): In fact; TRIM25 was most strongly associated with poor outcome in breast cancer over any other cancer type. There were no significant differences based on TRIM25 expression or predicted protein activity in normal breast tissue was a significant difference in the activity of TRIM25 protein between primary tumors and metastases (Figure 7H): In addition, log

We functionally tested this correlative relationship   using human ESCs (hESCs): To determine whether loss of TRIM25 could induce   differentiation, we lentivirally expressed short hairpins against TRIM25. Strikingly, TRIM25 depletion induced changes in hESC morphology consistent with  differentiation revealed a considerable increase in mesoderm, endoderm, and ectoderm marker genes after TRIM25 knockdown, suggesting that TRIM25 is required to maintain a stem cell state (Figure 6F): Recently,  Akrap used single-cell RNA-seq to identify markers of functionally enriched stem and progenitor cells in breast cancer. In both primary breast tumors and TNBC cell lines, POUSF1 , NANOG, and SOX2 were major determinants of a quiescent cancer stem cell (CSC)-Iike cell phenotype with  high stemness and  tumorgenicity (Akrap et al,, 2016): Using our CRISPR TRIM25-knockout cell models, we found that expression of either TRIM25 or TRIM2SAR in TNBC-TKO cells increased the expression of POUSFI, NANOG, and SOX2 (Figures 6G and 6H), suggesting that TRIM2S regulates the core genes involved in maintaining quiescent CSC-Iike phenotypes. Together, these results suggest TRIM25 promotes metastasis through increasing the stemness and tumorigenicity of breast cancer cells, enhancing their capacity for colonization, survival, and outgrowth at the secondary site\_

<!-- image -->

although the TCGA dataset only contains 7 matched pairs of primary tumors and metastases, 6 of 7 metastases had higher TRIM25 expression than their respective primary tumors (Figure 71): TRIM25 immunohistochemistry in primary breast tumors, lymph node, and distant metastases revealed similar TRIM25 localization, suggesting localization of TRIM25 is not overtly these data support a role of TRIM25 as a driver of poor outcome in breast cancer\_

## DISCUSSION

Context-specific   regulatory   networks, inferred by   unbiased reverse engineering algorithms, provide a framework for identifying the proteins causally associated with specific phenotypic states (Lefebvre et al,, 2010). Here we reverse engineered a breast cancer-specific regulatory network to uncover a transcriptional hierarchy driving breast cancer metastasis. Importantly, we discovered that TRIM25, a multifunctional TF, lies at the epicenter of this hierarchy. Altered TRIM25 activity causes coordinated broad changes in the metastatic program , affecting the expression of many metastasis effectors simultaneously and promoting the metastatic phenotype.

Although we focused our study on the role of TRIM25 in TNBC, VIPER analysis identified this regulator protein as the most statistically significant metastatic progression MR both in TNBC and in ER+ tumors, suggesting that it may play an equally relevant role in ER+ breast cancer as well: Indeed, it has been proposed cascade in the absence of estrogen receptor, resulting in the evolution of estrogen independence and resistance to hormone therapy (Nalepa and Harper, 2002). A similar phenomenon was

Multifunctional proteins such as TRIM25 challenge a conventional one protein-one function paradigm. Many TFs that bind double-stranded DNA with sequence specificity also bind RNA (Cassiday and Maher; 2002). Similarly, several RNA-binding E3 ubiquitin ligases have recently been discovered to direct cellular   regulatory   pathways by   affecting both  protein and mRNA stability (Cano et al,, 2010). Interestingly, several of these RNA-binding E3 ubiquitin ligases contain a B-box zinc-finger DNA-binding domain analogous to TRIM25. Here we demonstrate that TRIM25 has the potential to control cellular phenotypes by interacting with DNA in addition to RNA (Streich et al, 2013) targets. Moreover, our data show that TRIM25 represses many targets at both levels, representing a transcriptional/posttranscriptional feedforward topology (Lefebvre et al,, 2010; Mandiversified functionality has not been described for TRIM25. yet recently observed in prostate cancer whereby the glucocorticoid receptor (GR) substitutes for the androgen receptor (AR) resulted in resistance to anti-androgen therapy (Arora et al,, 2013). However , here we show data supporting an estrogen-independent role of TRIM25. Further, in a parallel and ongoing study, we did not find TRIM25 as differentially expressed or differentially active TFs in letrozole-resistant breast cancer patients (data not shown):   Therefore, the phenotypes observed in  studies that link TRIM25 with tumorigenicity and survival of estrogendependent cells in the absence of estrogen (Urano et al,, 2002) may have been the result of TRIM2S promoting the stemness and tumor-initiating phenotypes described here, thus suggesting that its role in metastatic progression may be fully independent of hormonal status\_

The dynamic nature of metastasizing cancer cells cannot simply be explained by the accumulation of progressive genetic changes in the primary tumor (Monteiro and Fodde, 2010). The capacity to resist cytotoxic or targeted therapy, to undergo multiple profound phenotypic changes, to overcome the challenges of foreign microenvironments, and to maintain the ability to eventually recapitulate the heterogeneous composition of the primary tumor at distant organ sites is not typical behavior for a differentiated epithelial cell. Rather, this is likely achieved by stem-like cells that maintain active DNA repair, express a variety of drug transporters, resist apoptosis and pathotropism, and have highly dynamic cellular plasticity that supports multiple hallmarks of cancer (Lawson et al., 2015). Our data suggest that   collapsing transcriptional hierarchies that  regulate   the balance between differentiation and self-renewal, by targeting keystone proteins Iike TRIM25, is critical to affect the coordinated transcriptomic reprogramming that is required for metastasis and may represent promising future targets for cancer intervention\_

## EXPERIMENTAL PROCEDURES

## Primary Human Breast Cancer and Matched Lymph Node Metastases

Paired primary tumor and lymph node metastases were collected during surgical resection. All tissue was used with informed consent and banked at Memorial Sloan Kettering Cancer Center (MSKCC) in accordance with institutional review board (IRB) approval. All samples were snap-frozen and stored at 80*C until use. All samples were H&amp;E stained and independently reviewed by a breast cancer pathologist; Tumors were micro-dissected to obtain &gt;70% purity: RNA was isolated from fresh-frozen samples using the RNeasy Plus mini prep kit (QIAGEN; Valencia; CA, USA): Nucleic acid quality was determined with the Agilent 2100 Bioanalyzer (Agilent Technologies, Santa Clara, CA, USA): Primary tumor and matched metastasis pairs, for which RNA of sufficient quantity and quality was available, were analyzed on Affymetrix GeneChip Human Genome U133 2.0 (Affymetrix, Santa Clara, CA, Array

USA) at the genomics core at Memorial Sloan Kettering Center for Molecular

## Animal Studies

AIl animal work was done in accordance with the Institutional Animal Care and Use Committee at MSKCC. Athymic Nu/Nu mice were obtained from Harlan Laboratories (Indianapolis, IN, USA) and NOD-scid ILZRgnull (NSG) mice were obtained from Jackson Laboratory (Bar Harbor; ME; USA) and randomized MDA-MB-231 cells were first infected with GREEN pHIV-LucCells were then infected with the indicated constructs (Figure S3A) All animals were injected between 5 and 7 weeks of age. Single-cell suspensions of the indicated cells were mixed 1:1 with serum-free media for intravenous injections or 1:1 with Matrigel (BD Biosciences, Franklin Lakes, NJ, USA) for orthotopic injections.

CAL-51 cells (1 x 106) were injected into the lateral tail vein of 4- to 6-weekold athymic nude mice: Lungs were harvested 8 weeks post-injection. CAL-51 TKO cells (1 X 106) were injected into the lateral tail vein of 4- to 6-week-old NSG were harvested 8 weeks   post-injection: BT54g-TKO (2 X 106) cells were injected into the mammary fat pad of 4- to 6-week-old NSG mice and monitored to tumor take by bioluminescence imaging (IVIS): MDA-MB-231 cells (empty vector [EVJ; TRIM25, and 4TRIM25; X 106) were injected into the mammary fat pad of 4- to 6-week-old NSG mice. Primary tumors and lungs were harvested 8 weeks post-injection: MDA-MB-231 (EV, TRIM25, and ATRIM25; 5 x 105) were injected into the lateral tail vein of 4- to 6-week-old athymic nude mice: Lungs were harvested 8 weeks injection: post-

TRIM2Shigh (TRIM25 overexpression) and TRIM2Slow (TRIM25 knockdown) cells with opposing fluorescent labels were mixed 1:1 and injected (5 X 105 cells) into the lateral tail vein of athymic nude mice or 1 x 106 cells into the mammary fat pad of NSG mice: The development of primary tumors or lung metastases was monitored using bioluminescence imaging (BLI; IVIS, Xenogen, Alameda, CA, USA)  When lung metastases were visible , mice were sacrificed and their lungs were imaged via ex vivo fluorescence imaging and spectral unmixing: Lungs were then sectioned and stained with anti-RFP antibody (Abcam, Cambridge, MA USA): Lung tissues were blindly scanned using a Carl Zeiss Axioimager Z1 microscope (Oberkochen, Germany) equipwith a Tissue Gnostics slide-scanning platform. TissueQuest analysis software was used for automated quantification of RFP+ and GFP+ tumor cells per total number of DAPI+ cells within a full cross section of the primary tumor: For lung tissue analysis; two lobes per animal (one left and one right) were used for red:green ratio calculations\_ Two-tailed pairwise t test was used to statistically compare relative red versus green. Animals that were ill or died due to circumstances unrelated to the experiment were excluded from the study. ped

## Next-Generation Sequencing Data

ing the online PRECOG tool at https://precog stanford edul . Spearman's cor relation matrix was generated using corrplot 0.73 and PerformanceAnalytics 1.4.3541 in R\_

## RNA-Seq Analysis of Cell Lines

Mapped reads for each sample were counted for each gene in annotation files in GTF format (gencode.V19.annotation gtf available for download from GENECODE website, http://www:gencodegenes org/releases/19. html), using the FeatureCounts read summarization program (Liao et al. 2014) following the user guide (http://bioinfwehi edu.au/subread-packagel SubreadUsersGuide pdf) . Individual count files were merged to generate the raw-counts matrix by an in-house R script; normalized to account for differences in library size, and the variance was stabilized by fitting the dispersion to a negative-binomial distribution, as implemented in the DESeq R package (http //bioconductor org/packages/release/bioc/htmI/DESeq.html) (Anders and Huber, 2010).

Total RNA was isolated from cell lines using the RNeasy Plus mini prep kit (QIAGEN; Valencia CA USA) Nucleic acid quality was determined with the Agilent 2100 Bioanalyzer. RNA-seq was also performed at the New York Genome Center (New York; NY, USA) a HiSeq 2500 Ultra-High Throughput Sequencing System (Illumina, San CA USA): Raw reads in the fastq format were aligned to Human Genome HG19 using the RNAseq STAR aligner version 2.4.0d (Dobin et al , 2013; Dobin and Gingeras 2015) , as recommended by the user manual downloaded along with the software: STAR aligner was chosen for mapping accuracy and speed (Engstrom et al,, 2013). using Diego,

ChIP-seq and RIP-seq were performed at the Memorial Sloan Kettering Center for Molecular Oncology (New York; NY, USA) using a HiSeq 2500 UltraHigh-Throughput Sequencing System (Illumina, San CA, USA): Raw sequencing data were aligned to the hg37 genome build using the BurrowsWheeler Aligner (BWA) version 0.7.10 (Li and Durbin, 2009). Further indel realignment; base-quality score  recalibration and duplicate-read removal were performed using the Genome Analysis Toolkit (GATK) version 3.2.2 (McKenna et al, 2010) following raw read alignment guidelines (DePristo et al,, 2011). Peaks were called from the resulting bam files by Model-based Analysis of ChIP-seq (MACS2) version 2.1.0 (Feng et al,, 2012), following the Diego,

As a first filtering step, resulting raw peaks were filtered by p value 0.01. Next; for each peak, reads per kilobase of transcript per million mapped was calculated for IP and INPUT (for ChIP-seq) bam files\_ Only peaks with RPKM INPUTIRPKM IP ratio greater than 0.5 were reported to final results\_

## Statistical Analysis

TCGA RNA-seq, amplification; deletion, mutation, and reverse phase protein lysate microarray (RPPA) data were downloaded from the MSKCC cbio portal TCGA breast cancer data were downloaded from the Broad Institute GDAC Firehose (https:/Igdac broadinstitute org): PRECOG data were generated us-

The Kaplan-Meier method and log rank test were performed using the Prism 6 Software (GraphPad Software, La Jolla; CA, USA): Heatmaps were generated using Partek Genomics Suite software, version 6.6 (Partek, USA): We performed a minimum of 3 replicates per experiment to ensure adequate sample size for statistical analyses

The Cancer Cell Line Encyclopedia (CCLE) was used to eliminate candidate MR from potential functional validation based on the lack of expression in

## Figure 6. TRIM25 Regulates the MET-GES and Modulates Tumorigenicity and Stemness

(B) Bioluminescence imaging and tumor take rate 100 days after orthotopic injection of BT549 cells infected with indicated shRNA into the mammary fat pad of NSG mice (n = 4-8 mice as indicated):

(A) GO analysis of core MET-GES genes transcriptionally or post-transcriptionally regulated by TRIM25.

(C) GSEA for oncogenic signatures associated with differentially expressed genes from RNA-seq after TRIM25 knockdown in BT549 and MDA-MB-231 cells. Normalized enrichment score of the ESC\_J1\_Up\_Late.V1\_Up signature (left): (Right) Representative gene expression changes from this signature are shown:

<!-- image -->

breast cancer cell lines (http //wwW broadinstitute org/ccle/home) (Barretina et al,, 2012).

Differential expression analysis after MR gene silencing was performed by comparing the silenced  samples versus the scramble small hairpin RNA (shRNA) and mock controls independently, using the moderated Student's t test as implemented in the limma package from Bioconductor (Ritchie et al,, 2015). Gene expression signatures based on the scramble and mock controls were integrated using the Stouffer approach: Z = (Z1 + Zz) / V2, where Z1 and Zz are Z scores estimated by the moderated Student's t test: Lineal regression with exhaustive selection was performed with the package leaps The approach selected the lineal combination of n MRs that best predicts the subtypematched MET-GES\_ We selected n as the highest number of MRs for which all coefficients of the model were different than zero at Bonferroni's corrected 3 p &lt; 10 The proportion of the MET-GES modulated by each MR was inferred as the proportion of MET genes in the leading edge when computing the enrichment of the MET-GES on each MR-silencing gene expression signature by GSEA

Enrichment of oncogenic signatures o the TRIM25-silencing signature was performed by GSEA (Subramanian et al,, 2005). Oncogenic signature were downloaded from http //software broadinstitute org/ gsea/datasets jsp. Differentially expressed genes (false discovery rate [FDR] p&lt; 0.01; Table S4) between siSCR (control) versus siTRIM25 were pre-ranked based on Z score; and the GSEA was implemented using JAVA downloaded from the Broad Institute (http://software broadinstitute org/gsea): GSEA2 analysis was performed as previously described (Kruithof-de Julio et al., 2011) using an in-house implementation in R.

## Assembly of Context-Specific Regulatory Models and MR Analysis

A breast carcinoma context-specific network model of transcriptional regula was assembled with the ARACNe; based on 851 RNA-seq expression profiles obtained from TCGA ARACNe was run with 100 bootstraps, a p value threshold of 10 8 and 0 data processing inequality (DPI) tolerance, generating a network of 1,748 TFs associated with 18,783 target genes by 459,5689 interactions. The regulatory models were generated from the ARACNe results using the VIPER package from Bioconductor (http:/ /bioconductor org/packages/ tion

The gene expression signatures for 20 ER+ and 11 TNBC metastases (MET GES) were computed with paired Student's t test by comparing their profiles against the matching primary tumor ones Then; the enrichment of each regulaprotein regulon on the MET-GESs was inferred by the VIPER algorithm (AIvarez etal,,2016; Aytes etal,, 2014),asimplemented in the VIPER package for R available from Bioconductor (https://wwWbioconductor org/packages/releasel bioc/htmlviperhtml) . Statistical significance was estimated by permuting the samples uniformly at random 1,000 times\_ tory

For   single   patient-based analysis, gene expression   signatures were computed by comparing each MET expression profile with the matching primary tumor expression profile. A null model for statistical testing was generated by permuting the samples uniformly at random 1,000 times The most consistent MRs across all tumors were prioritized according to the average dysregulation (normalized enrichment score [NES]) divided by its SD.

## ACCESSION NUMBERS

The accession numbers for the RNA-seq after TRIM25 knockdown in breast cancer cell lines, ChIP-seq in TNBC cell lines, and RIP-seq in TNBC cell lines data reported in this paper are GEO: GSE79589, GSE79588,and GSE79587, respectively. The accession numberfor the primary breast cancer and matched metastases microarray data reported in this paper is GEO: GSE57968.

## SUPPLEMENTAL INFORMATION

Supplemental Information includes Supplemental Experimental Procedures; seven figures, and seven tables and can be found with this article online at http:I/dx doi.org/10.1016/j.celrep.2017.07.052.

## AUTHOR CONTRIBUTIONS

S.C , and conducted the bioinformatics analysis and T.A.C. analyzed the data. LT.V. provided the clinical samples LAW. M.J\_ AC-, and T.A.C. wrote the manuscript: All authors reviewed and edited the final manuscript,

## ACKNOWLEDGMENTS

We thank Agnes Viale and the MSKCC genomics core for technical assistance We thank members of the Chan and Califano labs for helpful discussions\_ LAW\_ was supported by The Canadian Institutes of Health Research PDF Award MFE-127325. This work was supported by a Department for Defense Era of Hope Grant (BC120568), the STARR Cancer Consortium, the Geoffrey Beene Cancer Center, and the MSKCC Metastasis Research Center (all to TAC-); the NIDDK (1 DP2 DK098093-01) and a CADC pilot grant (S.C. and S.M): This work was in part supported by NCI Cancer Support Grant P3O CA008748 to the Microchemistry and Proteomics Core.

## rEFERENCES

berg; G. (2016). Identification of Distinct Breast Cancer Stem Cell Populations Based on Single-Cell Analyses of Functionally Enriched Stem and Progenitor Pools. Stem Cell Reports 6, 121-136\_

Alvarez; M.J , Shen; Y. Giorgi, F.M , Lachmann; A, Califano, A. (2016). Functional characterization of somatic mutations in cancer using network-based inference of protein activity. Nat: Genet: 48, 838-847. Ding;

## Figure 7 TRIM25 Is Frequently Amplified in Breast Cancer and Is Associated with Poor Overall Survival

(A) Frequency of TRIM25 copy number alterations (CNAs) in 32 cancer types from the TCGA. CS, cell carcinoma; pRCC , papillary renal cell carcinoma; PCPG, pheochromocytoma and paraganglioma; ccRCC, clear cell renal cell carcinoma; GBM, glioblastoma multiforme; AML, acute myleiod leukemia; chRCC, chromophobe renal cell carcinoma; DLBC, diffuse large B cell Iymphoma; ACC, adenoid cystic carcinoma

Anders; S,, and Huber; W: (2010). Differential expression analysis for sequence coid receptor confers resistance to antiandrogens by bypassing androgen receptor blockade. Cell 155, 1309-1322\_

Lefebvre, C., Alvarez, M.J. Zheng, Eastham, JA Gopalan; A. Pienta; KJ. Shen; M.M. et al. (2014). Cross-species regulatory network analysis identifies a synergistic interaction between FOXMI and CENPF that drives prostate cancer malignancy: Cancer Cell 25, 638-651\_

V. Sonkin; D\_ et al. (2012). The Cancer Cell Line Encyclopedia enables predictive modelling of anticancer drug sensiNature 483 603-607 tivity:

Califano, (2005). Reverse engineering of regulatory networks in human B cells. Nat. Genet. 37, 382-390.

Basso, K , Saito, M: Margolin, AA , Wang; K , Lim; W.K Kitagawa; Y. Schneider, C Alvarez, M.J: Califano, A , and Dalla-Favera, R. (2010). Integrated biochemical and computational approach identifies BCL6 direct target genes controlling multiple pathways in normal germinal center B cells. Blood 115,975-984.

Cano, F; Miranda-Saavedra, D. and Lehner, P J. (2010). RNA-binding E3 38,1621-1626\_

Carro, M.S,, Lim, W.K,, Alvarez, Bollo, R.J: Zhao, X,, Snyder; E.Y Anne, S.L , Doetsch; F., Colman; H,, et al. (2010). The transcriptional network for mesenchymal transformation of brain tumours. Nature 463, 318-325

Carroll, J.S. Meyer; C.A,, Song; J. Fertuck; K.C , Hall, G.F , et al. (2006). Genomewide analysis of estrogen receptor binding sites. Nat: Genet: 38, 1289-1297\_ Cassiday, LA , and Maher; LJ;, 3rd. (2002). Having it both ways: transcription factors that bind DNA and RNA. Nucleic Acids Res. 30, 4118-4126.

Cerami, E: Gao, J. Aksoy, BA,, cer genomics portal: an open platform for exploring multidimensional cancer

Dhruv, H., Rieckhof; G.E: of causal genetic drivers of human disease through systems-level analysis of regulatory networks. Cell 159, 402-414.

Choudhury, NR:, Nowak, J.S: Michlewski, G. (2014). Trim25 Is an RNA-Specific Activator of Lin28a/TuT4Mediated Uridylation: Cell Rep. 9, 1265-1272.

Creighton, C.J,, Cordero, KE: Larios, J.M: Miller, R.S; Johnson, Genes regulated by estrogen in breast tumor cells in vitro are similarly regulated in vivo in tumor xenografts and human breast tumors. Genome Biol. 7, R28.

DePristo, MA: work for variation discovery and genotyping  using next-generation DNA sequencing data. Nat Genet: 43, 491-498\_

Protoc Bioinformatics 3,1-19\_

P and Gingeras, T.R: (2013). STAR: ultrafast universal RNA-seq aligner. Bioinformatics 29, 15-21.

Guigo, R., et al. (2013). Systematic evaluation of spliced alignment programs for RNA-seq data: Nat Methods 10,1185-1191\_

enrichment using MACS. Nat Protoc. 7, 1728-1740.

Sun; Y. Sinha; R,, Larsson, E,, et al. (2013). Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal. Sci. Signal. 6, pl1.

Hanahan; D. and Weinberg; R.A. (2011). Hallmarks of cancer: the next generation. Cell 144, 646-674\_

estrogen-responsive genes using a genome-wide analysis of promoter elements for transcription factor binding sites \_

An extended transcriptional network for pluripotency of embryonic stem cells. Cell 132 1049-1061\_

and Shen; MM: (2011). Regulation of extra-embryonic endoderm stem cell differentiation by Nodal and Cripto signaling: Development 138, 3885-3895.

Bansal, M. Interrogation of a context-specific transcription factor network identifies novel regulators of pluripotency. Stem Cells 33, 367-377 \_

Kwon, S.C repertoire of embryonic stem cells

Pauli; F Batzoglou; S., Bernstein; B.E: Bickel; P\_ guidelines and   practices of the ENCODE and modENCODE consortia\_ Genome Res. 22,1813-1831 \_

Eyob, H: et al. (2015). Single-cell analysis reveals a stem-cell program in human metastatic breast cancer cells\_ Nature 526, 131-135\_

Lefebvre, C., Rajbhandari, P . Alvarez; M.J , Bandaru; P. Wang, K,, Sumazin, P. Kustagi, M: Bisikirska, B.C. et al. (2010). A human B-cell interactome identifies MYB and FOXMI as master regulators of prolifer ation in germinal centers. Mol. Syst. Biol. 6, 377 \_

Li, H,, and Durbin, R. (2009). Fast and accurate short read alignment with Burrows-Wheeler transform. Bioinformatics 25, 1754-1760.

Liao, Y,, Smyth, G.K , and Shi; W: (2014). FeatureCounts: an efficient general purpose program for assigning sequence reads to genomic features. Bioinformatics 30,923-930.

SL, Yeo, AL , Thomsen; J.S , Chan; W.C , Doray, B., Bangarusamy, D.K , Ramasamy; A , et al. (2004). Discovery of estrogen receptor alpha target genes and response elements in breast tumor cells. Genome Biol: 5, R66. Kong, and Alon; U. (2003). Structure and function of the feed-forward

Stolovitzky, G, Dalla Faof gene regulatory networks in a mammalian cellular context: BMC Bioinfor matics 7 (Suppl 1), S7

A. (2006b). Reverse engineering cellular networks. Nat: Protoc. 1 , 662-671\_

A,, Garimella, K, Altshuler, D\_ Gabriel, S. Daly, M , and DePristo, M.A. (2010)\_ The genome analysis toolkit: A MapReduce framework for analyzing next-gen eration DNA sequencing data. Genome 20, 1297-1303\_ Res:

Monteiro, J., and Fodde, R: (2010). Cancer stemness and metastasis: therapeutic consequences and perspectives. Eur. J. Cancer 46, 1198-1203

661-662 \_

Navin; N.E: (2015). The first five years of single-cell cancer genomics and beyond. Genome Res. 25, 1499-1507 .

Pax-5 gene: pluripotent regulator of B-cell differentiation and cancer dis ease. Cancer Res. 71 , 7345-7350\_

S., Barrallo-Gimeno, A. tion requires the repression of the epithelial-mesenchymal transition inducer Prrx1 . Cancer Cell 22, 709-724. Vega;

Tosello, V. Herranz; D Ambesi-Impiombato, A , Da Silva, Sanchez-Martin; Perez-Garcia, Rigo, Castillo, M. et al. (2013). Direct reversal of glucocorticoid resistance by AKT inhibition in acute lymphoblastic Ieukemia. Cancer Cell 24, 766-776.

Kraljevic Pavelic; S. (2010). Integrated gene networks in breast cancer development. Funct: Integr. Genomics 10, 11-19.

Phipson, B., Wu, D. (2015). Iimma powers differential expression analyses for RNA-sequencing and microarray studies Nucleic Acids Res. 43, e47\_

Rodriguez-Barrueco, R,, Yu, Navas, D\_ Putcha; P

Castillo-Martin; M: et al: (2015). Inhibition autocrine STAT3-calprotectin axis as targeted therapy for HR-/HERZ+ breast cancers

Spano, D. Heck; C\_ De Antonellis, P\_ Christofori, G,, and Zollo, M. (2012). Molecular networks that regulate cancer metastasis. Semin. Cancer Biol. 22, 234-249.

Connick; JP and Haas, A.L: (2013). Tripartite motif ligases catalyze polyubiquitin chain formation through cooperative allosteric mechanism: J

Subramanian, A, Tamayo, P\_ Mootha; V.K , Mukherjee; Ebert; B.L, sirov, J.P. (2005). Gene set enrichment analysis: a knowledge-based approach for interpreting genome-wide expression profiles. Proc Natl. Acad. Sci. USA 102, 15545-15550\_

and Inoue, S. (2002). Efp targets 14-3-3 sigma for proteolysis and promotes breast tumour growth: Nature 417, 871-875.

and Wu; G. (2011). Forkhead transcription factor foxq1 promotes epithelialmesenchymal  transition  and breast cancer metastasis.  Cancer Res.  71, 1292-1301\_