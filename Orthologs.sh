#!/usr/bin/bash
#SBATCH --ntasks 16 --mem 8G -p short

module load ncbi-blast
module load orthofinder
module load miniconda2
CPU=8

mkdir -p Pseudomonas
cd Pseudomonas

cd ..
orthofinder.py -a $CPU -f Pseudomonas
