#! /usr/bin/env python3

import sys
import glob
import shutil

if len(sys.argv) < 3:
	print('Proper usage: replace.py $init $final [$files]')
	sys.exit()

init=sys.argv[1]
fin=sys.argv[2]
if len(sys.argv) < 4:
	file_list=glob.glob("*"+init+"*")
	file_list.extend(glob.glob('*.dat'))
	file_list.extend(glob.glob('*.py'))
else:
	file_list=glob.glob(sys.argv[3])
	for j in range(4,len(sys.argv)):
		file_list.extend(glob.glob(sys.argv[j]))

for fname in file_list:
    try:
        with open(fname,"r") as f:
            val=f.read()
        with open(fname,"w") as f:
            f.write(val.replace(init, fin))
        shutil.move(fname, fname.replace(init, fin))
    except:
        pass