#!/usr/bin/env python

import sys
import subprocess
import numpy

if len(sys.argv) < 2:
	print 'Proper usage: qdel_done.py $RUN_NUMBER'
	sys.exit()

rn=sys.argv[1]
subprocess.call('qstat -u mkolodru > temp.temp', shell=True)

vdone=[]
stats_lst=numpy.loadtxt('stats_section.dat',dtype=int)
for row in xrange(len(stats_lst)):
	if stats_lst[row,1]!=-1:
		vdone.append(stats_lst[row,0])


for line in open('temp.temp','r'):
	rnind=line.find(rn)
	if rnind != -1:
		pnum=line.split('.')[0]
		vnum=int(line[(rnind+len(rn)+1):].split('.')[0])
		for item in vdone:
			if item==vnum:
				print 'About to delete vnum='+str(vnum)
				cmd='qdel '+pnum
				print cmd
				subprocess.call(cmd,shell=True)
				break

subprocess.call('rm temp.temp',shell=True)
