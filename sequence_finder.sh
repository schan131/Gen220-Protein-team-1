#!/usr/bin/bash
#SBATCH -p short -N 1 -n 8 --mem 8gb

grep ">PA2257" -A 1 /rhome/avale043/Gen220-Protein-team-1/paer.final.fasta > genes/PA2257.fasta