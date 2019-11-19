module load signalp

sigp='Y'

#P.aeruginosa PAO1 amino acid
if [ -e "paer.txt" ]; then
 echo 'p.aer.txt already exists'
else
 curl -0 http://www.pseudomonas.com/downloads/pseudomonas/pgd_r_19_1/Pseudomonas_aeruginosa_PAO1_107/Pseudomonas_aeruginosa_PAO1_107.faa.gz > paer.txt.gz
 gunzip paer.txt.gz
fi
signalp -c 30 -M 15 -t gram- paer.txt > paer.pred.txt

#P.syringae pv. tomato DC3000 amino acid
if [ -e "psyr.txt" ]; then
 echo 'p.syr.txt already exists'
else
 curl -0 http://www.pseudomonas.com/downloads/pseudomonas/pgd_r_19_1/Pseudomonas_syringae_pv_tomato_DC3000_111/Pseudomonas_syringae_pv_tomato_DC3000_111.faa.gz > psyr.txt.gz
 gunzip psyr.txt.gz
fi
signalp -c 30 -M 15 -t gram- psyr.txt > psyr.pred.txt

#P.fluorescens SBW25 amino acid
if [ -e "pflr.txt" ]; then
 echo 'p.flr.txt already exists'
else
 curl -0 http://www.pseudomonas.com/downloads/pseudomonas/pgd_r_19_1/Pseudomonas_fluorescens_SBW25_116/Pseudomonas_fluorescens_SBW25_116.faa.gz > pflr.txt.gz
 gunzip pflr.txt.gz
fi
signalp -c 30 -M 15 -t gram- pflr.txt > pflr.pred.txt

