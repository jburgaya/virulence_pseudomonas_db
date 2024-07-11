#!/usr/bin/env python

import os
import argparse
import pandas as pd
import warnings

def get_options():
    description = 'Filter blast output to generate one single file'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("blastout",
                        help='Blast output directory')
    parser.add_argument("virfile",
                        help='Virulence genes and categories file')
    parser.add_argument("--minid",
                        default=90,
                        type=float,
                        help='Min identity threshold')

    return parser.parse_args()

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    options = get_options()

    vf = pd.read_csv(options.virfile, sep="\t")
    locus_to_vags = vf.set_index("Locus Tag")["VAGs_category"].to_dict()
    locus_to_genes = vf.set_index("Locus Tag")["Gene"].to_dict()

    input_files = [f for f in os.listdir(options.blastout) if f.endswith(".txt")]
    print(f"Found input files: {input_files}")

    headers=["qseqid", "sseqid", "pident", "qlen", "slen", "length", "nident"]
    
    categ_summary = pd.DataFrame(columns=vf["VAGs_category"].unique(), index=input_files)
    gene_summary = pd.DataFrame(columns=vf["Gene"].unique(), index=input_files)
    locustag_summary = pd.DataFrame(columns=vf["Locus Tag"].unique(), index=input_files)

    for file in input_files:
        file_path = os.path.join(options.blastout, file)
        df = pd.read_csv(file_path, sep="\t", header=None, names=headers)
    
        # filter hits pident
        df_filtered = df[df["pident"] >= options.minid]
        df_filtered = df_filtered.drop_duplicates(subset=["qseqid"])

        # map locustag to vag_category
        df_filtered["VAGs_category"] = df_filtered["qseqid"].map(locus_to_vags)

        # map locustag to genes
        df_filtered["gene"] = df_filtered["qseqid"].map(locus_to_genes)

        output_file_path = os.path.join(options.blastout, file.replace(".txt", "_filtered.txt"))
        df_filtered.to_csv(output_file_path, sep="\t", index=False, header=False)

        # update categ_summary based on filtered results
        for v_category in vf["VAGs_category"].unique():
            if v_category in df_filtered["VAGs_category"].values:
                categ_summary.loc[file, v_category] = 1
            else:
                categ_summary.loc[file, v_category] = 0

        # update genes_summary based on filtered results
        for v_gene in vf["Gene"].unique():
            if v_gene in df_filtered["gene"].values:
                gene_summary.loc[file, v_gene] = 1
            else:
                gene_summary.loc[file, v_gene] = 0

        # update genes_summary based on filtered results
        for v_locustag in vf["Locus Tag"].unique():
            if v_locustag in df_filtered["qseqid"].values:
                locustag_summary.loc[file, v_locustag] = 1
            else:
                locustag_summary.loc[file, v_locustag] = 0

    # save summaries
    categ_summary_file = os.path.join(options.blastout, "summary_categ.tsv")
    categ_summary.to_csv(categ_summary_file, sep="\t", index=True, header=True)
    gene_summary_file = os.path.join(options.blastout, "summary_gene.tsv")
    gene_summary.to_csv(gene_summary_file, sep="\t", index=True, header=True)
    locustag_summary_file = os.path.join(options.blastout, "summary_locustag.tsv")
    locustag_summary.to_csv(locustag_summary_file, sep="\t", index=True, header=True)












