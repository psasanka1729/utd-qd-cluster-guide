#!/usr/bin/env python

import sys
import subprocess

if len(sys.argv) < 2:
	print 'Proper usage: qdel_run.py $RUN_NUMBER'
	sys.exit()

rn=sys.argv[1]
subprocess.call('qstat -u mkolodru > temp.temp', shell=True)

for line in open('temp.temp','r'):
	if line.find(rn) != -1:
		pnum=line.split('.')[0]
		cmd='qdel '+pnum
		print cmd
		subprocess.call(cmd,shell=True)

subprocess.call('rm temp.temp',shell=True)
