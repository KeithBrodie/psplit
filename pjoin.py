#!/usr/bin/python

import os
import sys

chunk = 65536

files = os.listdir()

files = [f for f in files if os.path.isfile(f)]
#print(files)

root = sys.argv[1]

file_count = 1

jlist = []

while 1:

    test_name = root + ".split.{}".format(file_count)
    #print (test_name)

    if test_name in files:
        print (test_name)
        file_count += 1
        jlist.append(test_name)

    else:

        break

print ('Join List')
print (jlist)

with open(root,'wb') as of:

    for jfname in jlist:

        with open(jfname, 'rb') as jf:

            while 1:

                data = jf.read(chunk)

                if len(data):

                    of.write(data)

                if len(data) < chunk:

                    break