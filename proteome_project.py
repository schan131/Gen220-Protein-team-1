#!/usr/bin/env python
# Prior to running this code ensure that OrthoFinder and Python 2 are loaded
# OrthoFinder is incompatible with Python 3. 

import os,csv
import pandas as pd

# Make a new directory called Ecoli_genomes 
# and place FASTA protein sequences in it before running this script.

# Just to make sure we haven't run OrthoFinder already.
if os.path.exists("./OF_results"):
    print("Please remove or archive the existing results prior to running this script.")

else:
    # Run OrthoFinder on our E. coli dataset
    # Simplify the headers for each protein
    os.system("mkdir ./Ecoli_proteins/new_fastas")
    for filename in os.listdir("./Ecoli_proteins"):
        if filename.endswith(".fasta"):
            os.system("python protein_parse.py ./Ecoli_proteins/" + filename + " > ./Ecoli_proteins/new_fastas/" + filename)
    os.system("orthofinder -f ./Ecoli_proteins/new_fastas -o ./OF_results")

# Make a symbolic link (ln -s) to the Orthogroups_SingleCopyOrthologues.txt file
# created as a result of OrthoFinder. 

# Create a directory for any resulting output, for the single-copy orthologs 
# Initialize a list of SCOGs to search with
os.system("mkdir -p SCOG_output")
scogs = []
non_patho = ["K12_1", "K12_2", "Nissle1917", "StrainW"]
patho = ["IHE3034","O157H7","O83H1","UM146","UTI189"]

with open("Orthogroups_SingleCopyOrthologues.txt") as fh:
    for line in fh:
        scogs.append(line.strip())

# Columns in order are: IHE3034, K12_1, K12_2, Nissle1917, O157H7, 
# O83H1, StrainW, UM146, UTI189
# Each column index corresponds to a different strain. 
# Since these are single-copy orthologs, no need to worry about commas within 
# an index. 
#
# Count all SCOGs belonging to pathogens, non-pathogens, and both. 
# Save the accession numbers for O157H7 
# to look up the proteins in UniProt and get their GO IDs
df = pd.read_csv("Orthogroups.tsv")
patho_core_count = 0
nonpatho_core_count = 0
patho_pan_count = 0
nonpatho_pan_count = 0

flex_queries = []
O157H7_core_queries = []

with open("Orthogroups.tsv") as fh:
    for line in fh:
        new_line = line.split("\t")
        if not new_line[2] and not new_line[3] and not new_line[4] and not new_line[7]:
            patho_pan_count += 1
            for item in new_line: 
                if item and not item.startswith("U") and not item.startswith("OG"): # If this index is not empty
                    flex_queries.append(item.strip().split(",")[0]) # Just take the first item if there are duplicates 
                    break
            if new_line[1] and new_line[5] and new_line[6] and new_line[8] and new_line[9]:
                patho_core_count += 1
                O157H7_core_queries.append(new_line[5])
                print(new_line[0])
        elif not new_line[1] and not new_line[5] and not new_line[6] and not new_line[8] and not new_line[9]:
            nonpatho_pan_count += 1
            if new_line[2] and new_line[3] and new_line[4] and new_line[7]:
                nonpatho_core_count += 1

print("Genes in pathogens only: " + str(patho_pan_count))
print("Genes in the core pathogen genome: " + str(patho_core_count))
print("Genes in non-pathogens only: " + str(nonpatho_pan_count))
print("Genes in the core non-pathogen genome: " + str(nonpatho_core_count))

print(O157H7_core_queries)
with open("flex_query_list.txt", "w") as writer:
    for item in flex_queries:
        writer.write(item+"\n")
    writer.close()
