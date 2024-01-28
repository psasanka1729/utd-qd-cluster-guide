#!/usr/bin/env python3

import glob
import subprocess

def filecmp(a):
    return int(a[:-5].split('_')[-1])

fileList = glob.glob('*.qsub')
fileList.sort(key=filecmp)

for file in fileList:
    cmd = 'qsub ' + file
    subprocess.call(cmd, shell=True)