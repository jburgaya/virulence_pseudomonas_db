# virulence_pseudomonas_db

``virulence_factors.csv``: is a conservative list of Pseudomonas species virulence factors obtained from the Virulence Factor Database (VFDB), Victors Virulence Factors (PHIDIAS) and curation by the Pseudomonas Genome Database (PseudoCAP) with focus being primarily on PAO1 and PA14. [Ref: virulence factor evidence, from pseudomonas.com db](https://pseudomonas.com/virulenceFactorEvidence/list).


``virulence.csv``: filtered ``virulence_factors.csv`` file for dubplicated entries (locus tags). **VAGs_category** column is added according to [Liao, 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9299443/pdf/fcimb-12-926758.pdf), [Qin, 2022](https://www.nature.com/articles/s41392-022-01056-1#Sec2), and other references (described in google drive)


``db/virulence.fasta``: contains all DNA sequences for the virulence associated genes.

## Usage

``snakemake --use-conda --cores 4 -p -R run_blastn summary``

## TODO

* [x] remove spaces from ``virulence.fasta``
* [x] remove duplicates in ``virulence_factors.csv``  
* [x] add category col in ``virulence_factors.csv``
* [x] pipeline
  * [x] rule blastn: blast virulence db to a set of fasta files.
  * [x] rule summary: get summary tables for genes, vag categories and locus tags


