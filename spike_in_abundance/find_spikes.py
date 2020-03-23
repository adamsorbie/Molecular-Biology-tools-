#!/usr/bin/env python
from Bio import SeqIO
import argparse
import pandas as pd


def get_seqs(otu, fasta):
    """
    find otus with no taxonomy (suggested spikes)
    and filter fasta file for these
    :param otu: OTU table (pandas dataframe)
    :param fasta: fasta filename (str)
    :return: filtered fasta file containing
    putative spikes
    """
    otu_put_spikes = otu[otu.taxonomy == "Bacteria;;;;;;"]
    spike_otus = otu_put_spikes.index.tolist() 
    otu_seqs = list(r for r in SeqIO.parse(fasta, "fasta") if r.id in spike_otus)
    return otu_seqs
	
def main():
    """ create cli arguments and call get_seqs, 
	writing output to file"""
    parser = argparse.ArgumentParser(description="filter OTU fasta file for putative spikes")
	
    parser.add_argument("-i", "--input", type=str, help="otu fasta file")
    parser.add_argument("-otu", "--otu_table", type=str, help="otu table")
    parser.add_argument("-o", "--output", type=str, help="name for fasta output")
    args = parser.parse_args()

    otu = pd.read_csv(args.otu_table, sep="\t", header=0, index_col=0)
    otu_seqs = get_seqs(otu, args.input)
    SeqIO.write(otu_seqs, args.output, "fasta")

if __name__ == '__main__':
    main()


