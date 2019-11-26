<<<<<<< HEAD
import re, os, csv, itertools

#make sure to overwrite the files or remove them before running this program

#paer1: creates a list of predicted secreted protein names and another list of SP sites
paer = []
paersp = []
paerlist = []
paerpred = open('paer.pred.txt', 'r')
fh = csv.reader(paerpred,delimiter=' ')
for i in fh:
    if "Y" in i:
        paer.append(i[0])
        paersp.append(i[23])
paerlist = [">" + gene for gene in paer]

#paer2: non mature sequence list
paernonmat = []
paerfullname = []
file1=open('paer.txt', "r+")
temp1=file1.next()
while(temp1):
    for x in paerlist:
        for line in file1:
            if x in line:
                paerfullname.append(line)
                paernonmat.append(next(file1))
                break
    break

#paer3: mature sequence list
g = 0
paermat = []
paerfinal = open('paer.final.fasta', 'a')
for sp in paersp:
    x = int(sp)
    for z in paernonmat:
        a = z[x:]
        paerfinal.write(paerfullname[0])
        paerfinal.write(a)
        g += 1
        paernonmat.remove(paernonmat[0])
        paerfullname.remove(paerfullname[0])
        break

#psyr1: creates a list of predicted secreted protein names and another list of SP sites
psyr = []
psyrsp = []
psyrlist = []
psyrpred = open('psyr.pred.txt', 'r')
fh = csv.reader(psyrpred,delimiter=' ')
for i in fh:
    if "Y" in i:
        psyr.append(i[0])
        psyrsp.append(i[22])
        psyrsp.append(i[23])
psyrlist = [">" + gene for gene in psyr]
psyrsp = filter(None, psyrsp)

#psyr2: non mature sequence list
psyrnonmat = []
psyrfullname = []
file1=open('psyr.txt', "r+")
temp1=file1.next()
while(temp1):
    for x in psyrlist:
        for line in file1:
            if x in line:
                psyrfullname.append(line)
                psyrnonmat.append(next(file1))
                break
    break

#psyr3: mature sequence list
g = 0
psyrmat = []
psyrfinal = open('psyr.final.fasta', 'a')
for sp in psyrsp:
    x = int(sp)
    for z in psyrnonmat:
        a = z[x:]
        psyrfinal.write(psyrfullname[0])
        psyrfinal.write(a)
        g += 1
        psyrnonmat.remove(psyrnonmat[0])
        psyrfullname.remove(psyrfullname[0])
        break

#pflr1: creates a list of predicted secreted protein names and another list of SP sites
pflr = []
pflrsp = []
pflrlist = []
pflrpred = open('pflr.pred.txt', 'r')
fh = csv.reader(pflrpred,delimiter=' ')
for i in fh:
    if "Y" in i:
        pflr.append(i[0])
        pflrsp.append(i[21])
pflrlist = [">" + gene for gene in pflr]
pflrsp = filter(None, pflrsp)

#pflr2: non mature sequence list
pflrnonmat = []
pflrfullname = []
file1=open('pflr.txt', "r+")
temp1=file1.next()
while(temp1):
    for x in pflrlist:
        for line in file1:
            if x in line:
                pflrfullname.append(line)
                pflrnonmat.append(next(file1))
                break
    break


#pflr3: mature sequence list
g = 0
pflrmat = []
pflrfinal = open('pflr.final.fasta', 'a')
for sp in pflrsp:
    x = int(sp)
    for z in pflrnonmat:
        a = z[x:]
        pflrfinal.write(pflrfullname[0])
        pflrfinal.write(a)
        g += 1
        pflrnonmat.remove(pflrnonmat[0])
        pflrfullname.remove(pflrfullname[0])
        break
=======

>>>>>>> 134d7a4fbd8fe3d32cbf783cc8603a65bf303c53
