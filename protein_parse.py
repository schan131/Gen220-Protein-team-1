#!/usr/bin/python

import sys

for line in open(sys.argv[1]):
    if line.startswith(">U"):
        line = line.split()
        print line[0]
    elif line.startswith(">"):
        line = ">" + line.split("|")[1]
        print line
    else:
        print line.strip()
