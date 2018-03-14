
# script that rewrite the .gtf file without the ids present on different
# chromosomes
# use of the script command python rewrite_gtf.py file.gtf>new_file.gtf
import sys
diz = {}
file1= open(sys.argv[1],'r')
with open (sys.argv[1]) as l:
    for riga in l:
        lines1=riga.split('\t')[8].strip('\n')
        chro=riga.split('\t')[0]
        gene=lines1.split(' ')[1].rstrip('\";').lstrip('\"')
        if gene not in diz:
            diz[gene] = chro
            print(riga.strip('\n'))
        elif chro == diz[gene]:
            print(riga.strip('\n'))
