# script that print all the different chromosome
# present in the gtf file
# command for the script --> python chr_list.py file.gtf
import sys
diz = {}
file1= open(sys.argv[1],'r')
with open (sys.argv[1]) as l:
    for riga in l:
        lines1=riga.split('\t')[8].strip('\n')
        chro=riga.split('\t')[0]
        if chro not in diz:
            diz[chro] = 'var'
            print (chro)
