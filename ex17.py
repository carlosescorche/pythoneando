#!/usr/bin/env python3

# ex17: More Files

from sys import argv

script,file,file2 = argv

open(file2,'w').write(open(file).read())