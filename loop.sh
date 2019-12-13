#!/bin/sh

while read i
do
sed "s/PA2257/$i/g" sequence_finder.sh > genes/sequence_finder$i.sh
sbatch genes/sequence_finder$i.sh
done<genes.txt