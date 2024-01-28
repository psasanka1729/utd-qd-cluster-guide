#!/usr/bin/env python

import subprocess;
import sys;

started=0;

for line in open(sys.argv[1],'r'):
    if started==0 and line[0].isdigit():
        started = 1;
    if started==1:
        str = line.split('.')[0];
        print 'qdel ' + str;
        args=['qdel',str];
        subprocess.call(args);
        
