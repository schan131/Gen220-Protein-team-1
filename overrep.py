import re, csv, pandas
from scipy.stats import hypergeom


#Define files
Ortho_genecount = 'Orthogroups.GeneCount.tsv'

#Define strains into the categories
patho = ['IHE3034','O157H7','O83H1','UM146','UTI189']
nonpatho = ['K12_1','K12_2','Nissle1917','StrainW']

#Make pandas array
ogc = pandas.read_csv(Ortho_genecount,delimiter='\t')

#Partition array into pathogenic and non pathogenic bacteria
Pathogenic = ogc[['Orthogroup','IHE3034','O157H7','O83H1','UM146','UTI189']]
Nonpathogenic = ogc[['Orthogroup','K12_1','K12_2','Nissle1917','StrainW']]

#define how many organisms in each type
#have to minus 1 because we have the orthogroup column
path_len = len(Pathogenic.columns)-1
nonpath_len = len(Nonpathogenic.columns)-1


#Create an empty list
patho_l = []
nonpatho_l = []

#This is to change the pandas array into a list (of lists)
for i in range(len(Pathogenic)):
    patho_l.append(list(Pathogenic.iloc[i,0:path_len]))
for i in range(len(Nonpathogenic)):
    nonpatho_l.append(list(Nonpathogenic.iloc[i,0:nonpath_len]))

ortho_over_patho = []
ortho_over_nonpatho = []
#Sum and find difference per orthogroup
for i in range(int(len(patho_l))): #First we want to go one by one down the rows or orthogroups (in this case list)
    patho_count = sum(patho_l[i][1:]) #Count up how many genes are in the orthogroup for the pathogens
    nonpatho_count = sum(nonpatho_l[i][1:]) #same as above but for nonpathogens
    if patho_count-nonpatho_count > 4:
        ortho_over_patho.append(patho_l[i][0])
        # print('over rep in patho',patho_count, nonpatho_count, patho_l[i][0])
    if nonpatho_count-patho_count > 4:
        ortho_over_nonpatho.append(nonpatho_l[i][0])
print('There are ',str(len(ortho_over_patho)),'overrepresented orthogroups in pathogens')
print('There are ',str(len(ortho_over_nonpatho)),'overrepresented orthogroups in non-pathogens')

# list = []
nonpatho_writer = open('nonpatho_over.txt', mode ='w')
csv_np_writer = csv.writer(nonpatho_writer, delimiter=',')
patho_writer = open('patho_over.txt', mode ='w')
csv_p_writer = csv.writer(patho_writer, delimiter=',')

patho_over_genes = 0
nonpatho_over_genes = 0
for i in ortho_over_patho:
    file = './Orthogroup_Sequences/'+i+'.fa'
    with open(file) as fa:
        for line in fa:
            if line.startswith('>U'):
                # line = line.split()
                # print(line[0])
                continue
            elif line.startswith('>'):
                line = line.split('|')[1]
                csv_p_writer.writerow([line])
                patho_over_genes += 1
                # print(line)
for i in ortho_over_nonpatho:
    file = './Orthogroup_Sequences/'+i+'.fa'
    with open(file) as fa:
        for line in fa:
            if line.startswith('>U'):
                # line = line.split()
                # print(line[0])
                continue
            elif line.startswith('>'):
                line = line.split('|')[1]
                csv_np_writer.writerow([line])
                nonpatho_over_genes += 1
                # print(line)
print('There are ', str(patho_over_genes),'genes in the pathogen overrepresnted orthogroups')
print('There are ', str(nonpatho_over_genes),'genes in the non-pathogen overrepresnted orthogroups')



#Tried to do a hypergeomtric test.
# for i in range(int(len(patho_l))): #First we want to go one by one down the rows or orthogroups (in this case list)
#     patho_count = sum(patho_l[i][1:]) #Count up how many genes are in the orthogroup for the pathogens
#     nonpatho_count = sum(nonpatho_l[i][1:]) #same as above but for nonpathogens
#     if patho_count-nonpatho_count > 4:
#         ortho_over_patho.append(patho_l[i][0])
#         # print('over rep in patho',patho_count, nonpatho_count, patho_l[i][0])
#     if nonpatho_count-patho_count > 4:
#         ortho_over_nonpatho.append(nonpatho_l[i][0])
#         print('over rep in nonpatho',patho_count, nonpatho_count, patho_l[i][0])
#     pval= hypergeom.sf(patho_count,4,3,nonpatho_count) #The hypergeometric test.
#     print(pval)
#     if pval <= .05:
#         print(patho_count, nonpatho_count, patho_l[i][0], ' ',pval) #Prints out a table (kind of)


## Was going to try to do a chi square test, but then realized that was dumb of me...
# array_exp = [1,1,1,1]
    #first overrep
    # print(i)
    # pval=hypergeom.sf(x-1,path_len,)
    # x = chisquare(i[1:],f_exp=array_exp)
    # if x[1] <= .05:
    #     print(i[0])
