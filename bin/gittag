#!/usr/bin/env python

import subprocess

cmd = 'git log > gittag.temp'
subprocess.call(cmd, shell=True)
with open('gittag.temp', 'r') as f:
    firstline = f.readline()
print(firstline.split()[-1])