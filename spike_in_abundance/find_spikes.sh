#!/bin/bash 

eval "$(conda shell.bash hook)"
conda activate biopython

python find_spikes.py -i $1 -otu $2 -o $3

blastn -query $3 -subject Spikes.fasta -outfmt '6 std' -out results.txt

awk '$3>98' results.txt > spikes.txt

python rem_spikes.py -i $1 -t spikes.txt -o OTUs-Seqs-spikes-rem.fasta  

echo "Spike sequences removed" 
