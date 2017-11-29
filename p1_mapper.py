#!/usr/bin/env python

import sys
import os

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    datas = line.split()
    # access to AVG column
    if float(datas[7]) > -9999. and (float(datas[7]) > 27. or float(datas[7]) < -1.):
        filename = os.environ['mapreduce_map_input_file']
        splitfilename = filename.split('/')
        filename = splitfilename[-1]
        splitfilename = filename.split('-')
        filename = splitfilename[-1]
        splitfilename = filename.split('_')
        city = splitfilename[1]
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (city, datas[7])
