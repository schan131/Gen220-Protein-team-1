#!/usr/bin/bash
#SBATCH -p short -N 1 -n 24

module load hmmer
module load db-pfam

QUERY1=/rhome/avale043/Gen220-Protein-team-1/Pseudomonas/psyr.final.fasta
OUT1=psyr_search

QUERY2=/rhome/avale043/Gen220-Protein-team-1/Pseudomonas/pflr.final.fasta
OUT2=pflr_search

QUERY3=/rhome/avale043/Gen220-Protein-team-1/Pseudomonas/paer.final.fasta
OUT3=paer_search

hmmscan --cut_ga --cpu 24 --domtbl $OUT1.domtbl $PFAM_DB/Pfam-A.hmm $QUERY1 > $OUT1.hmmscan
hmmscan --cut_ga --cpu 24 --domtbl $OUT2.domtbl $PFAM_DB/Pfam-A.hmm $QUERY2 > $OUT2.hmmscan
hmmscan --cut_ga --cpu 24 --domtbl $OUT3.domtbl $PFAM_DB/Pfam-A.hmm $QUERY3 > $OUT3.hmmscan

awk '{print $2,"\t" $1}' $OUT1.domtbl | sort -k1 -h > psyr_domains.txt
awk '{print $2,"\t" $1}' $OUT2.domtbl | sort -k1 -h > pflr_domains.txt
awk '{print $2,"\t" $1}' $OUT3.domtbl | sort -k1 -h > paer_domains.txt



#FILE=/etc/resolv.conf
#if [ -f "$FILE" ]; then
#    echo "$FILE exist"
#else 
#    echo "$FILE does not exist"
#fi
