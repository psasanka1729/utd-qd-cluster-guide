#!/usr/bin/env python

import subprocess;
import sys;
import os

started=0;
toskip=[];

if os.path.exists('skip.dat'):
	for line in open('skip.dat','r'):
		if len(line) > 1:
			toskip.append(int(line))
			
for line in open(sys.argv[1],'r'):
    if started==0 and line[0].isdigit():
        started = 1;
    if started==1:
        str = line.split('.')[0];
        if not (int(str) in toskip):
            cmd='qjobs ' + str + ' > temp2.temp'
            subprocess.call(cmd, shell=True)
            cmd='cat temp2.temp | head -2 | tail -1'
            subprocess.call(cmd, shell=True)
        
