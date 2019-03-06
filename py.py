import os
inp = open('plik1.txt', 'r').read()
lines = inp.split('\n')

for line in lines:
	halp = line.split("\t")
	halp[0].strip
	name = halp[0].replace(" ","_")
	os.system("esearch -db protein -query 'TNRC6A[Gene Name] AND ("+halp[0]+"[ORGN] AND refseq[filter])' | efetch -format fasta > "+name+".txt")


