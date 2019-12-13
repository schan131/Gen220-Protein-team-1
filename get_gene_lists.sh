grep "PA"  /rhome/avale043/Gen220-Protein-team-1/Pseudomonas/OrthoFinder/Results_Nov25_1/Orthogroups/Orthogroups_UnassignedGenes.tsv | awk '{print $2}' > paer_genes/unassigned/paer_unassigned_genes.txt

grep "PF"  /rhome/avale043/Gen220-Protein-team-1/Pseudomonas/OrthoFinder/Results_Nov25_1/Orthogroups/Orthogroups_UnassignedGenes.tsv | awk '{print $2}' > pflr_genes/unassigned/pflr_unassigned_genes.txt

grep "PS"  /rhome/avale043/Gen220-Protein-team-1/Pseudomonas/OrthoFinder/Results_Nov25_1/Orthogroups/Orthogroups_UnassignedGenes.tsv | awk '{print $2}' > psyr_genes/unassigned/psyr_unassigned_genes.txt