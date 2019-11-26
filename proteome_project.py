#!/usr/bin/env python
# Prior to running this code ensure that OrthoFinder and Python 2 are loaded

import os

# Make a new directory called Ecoli_genomes 
# and place FASTA protein sequences in it

# Run OrthoFinder on our E. coli dataset
os.system("orthofinder -f Ecoli_genomes")
