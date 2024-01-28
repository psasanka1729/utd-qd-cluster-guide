#!/usr/bin/env py

import numpy
import subprocess
import sys

if len(sys.argv)<2:
	sys.stderr.write('Proper usage: invert_col.py $col_name\n')
	sys.exit()

col_name=sys.argv[1]
inv_col_name='1/'+col_name
versionmap=numpy.loadtxt('versionmap.dat',skiprows=1)
fin=open('versionmap.dat','r')
labels=fin.readline().split()
fin.close()
col_ind=labels.index(col_name)
inv_col=1.0/versionmap[:,col_ind]

#Add it to versionmap

linenum=0;

infile=open('versionmap.dat','r');
outfile=open('versionmap_backup.dat','w');
outval='';

for line in infile:
    outfile.write(line);
    if linenum == 0:
        outval+=line.rstrip();
        outval+='\t'+inv_col_name+'\n';
    else:
        outval+=line.rstrip()+'\t'+str(inv_col[linenum-1])+'\n'
    linenum+=1;

outfile.close();
outfile=open('versionmap.dat','w');
outfile.write(outval);


