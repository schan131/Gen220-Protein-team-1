#!/usr/bin/env python
# Prior to running this code ensure that OrthoFinder and Python 2 are loaded

import os

# Run OrthoFinder on our E. coli dataset
# At the moment, the default build on the cluster lacks the 
# dependencies to do tree building with iqtree.
os.system("orthofinder -f Ecoli_genomes")
