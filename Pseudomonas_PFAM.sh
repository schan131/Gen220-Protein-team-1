#!/usr/bin/bash
#SBATCH -p short -N 1 -n 24

module load hmmer
module load db-pfam

QUERY1=/rhome/avale043/Gen220-Protein-team-1/Pseudomonas/psyr_specific_genes.fasta
OUT1=psyr_specific

QUERY2=/rhome/avale043/Gen220-Protein-team-1/Pseudomonas/pflr_specific_genes.fasta
OUT2=pflr_specific

QUERY3=/rhome/avale043/Gen220-Protein-team-1/Pseudomonas/paer_specific_genes.fasta
OUT3=paer_specific

QUERY4=/rhome/avale043/Gen220-Protein-team-1/PFAM/psyr_genes/unassigned/psyr_unassigned_sequences.fasta
OUT4=psyr_unassigned

QUERY5=/rhome/avale043/Gen220-Protein-team-1/PFAM/pflr_genes/unassigned/pflr_unassigned_sequences.fasta
OUT5=pflr_unassigned

QUERY6=/rhome/avale043/Gen220-Protein-team-1/PFAM/paer_genes/unassigned/paer_unassigned_sequences.fasta
OUT6=paer_unassigned

hmmscan --cut_ga --cpu 24 --domtbl $OUT1.domtbl $PFAM_DB/Pfam-A.hmm $QUERY1 > $OUT1.hmmscan
hmmscan --cut_ga --cpu 24 --domtbl $OUT2.domtbl $PFAM_DB/Pfam-A.hmm $QUERY2 > $OUT2.hmmscan
hmmscan --cut_ga --cpu 24 --domtbl $OUT3.domtbl $PFAM_DB/Pfam-A.hmm $QUERY3 > $OUT3.hmmscan
hmmscan --cut_ga --cpu 24 --domtbl $OUT4.domtbl $PFAM_DB/Pfam-A.hmm $QUERY4 > $OUT4.hmmscan
hmmscan --cut_ga --cpu 24 --domtbl $OUT5.domtbl $PFAM_DB/Pfam-A.hmm $QUERY5 > $OUT5.hmmscan
hmmscan --cut_ga --cpu 24 --domtbl $OUT6.domtbl $PFAM_DB/Pfam-A.hmm $QUERY6 > $OUT6.hmmscan