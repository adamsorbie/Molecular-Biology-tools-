#!/usr/bin/env python
from Bio import SeqIO
import argparse
import pandas as pd

def filt_spikes(fasta, list_spikes):
    """
    remove spikes from input fasta file
    :param fasta:
    :param list_spikes:
    :return:
    """
    spikes_df = pd.read_csv(list_spikes, sep="\t", header=0, index_col=0)
    spikes = spikes_df.index.tolist()
    OTU_seqs = list(r for r in SeqIO.parse(fasta, "fasta") if r.id not in spikes)
    return OTU_seqs

def main():
    """
    parse cli arguments and write output to file
    :return: writes fasta with spikes removed to file
    """
    parser = argparse.ArgumentParser(description="remove spikes from fasta file")
    parser.add_argument("-i", "--input", type=str, help="otu fasta file")
    parser.add_argument("-t", "--text_file", type=str, help="text file containing list of spikes, one per line")
    parser.add_argument("-o", "--output", type=str, help="name for fasta output")
    args = parser.parse_args()

    otu_seqs = filt_spikes(args.input, args.text_file)
    SeqIO.write(otu_seqs, args.output, "fasta")

if __name__ == '__main__':
    main()

