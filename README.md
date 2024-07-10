# virulence_pseudomonas_db

``virulence_factors.csv``: is a conservative list of Pseudomonas species virulence factors obtained from the Virulence Factor Database (VFDB), Victors Virulence Factors (PHIDIAS) and curation by the Pseudomonas Genome Database (PseudoCAP) with focus being primarily on PAO1 and PA14. [Ref: virulence factor evidence, from pseudomonas.com db](https://pseudomonas.com/virulenceFactorEvidence/list). Duplicated locustags were only included once.


``virulence.csv``: filtered ``virulence_factors.csv`` file for dubplicated entries. Category column is added according to [Liao, 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9299443/pdf/fcimb-12-926758.pdf), [Qin, 2022](https://www.nature.com/articles/s41392-022-01056-1#Sec2).


``db/virulence.fasta``: contains all DNA sequences for the virulence associated genes.


## TODO

* [x] remove spaces from ``virulence.fasta``
* [ ] remove duplicates in ``virulence_factors.csv``  
* [ ] add category col in ``virulence_factors.csv``
* [ ] rule blast
* [ ] rule fetch results, add category column to results


