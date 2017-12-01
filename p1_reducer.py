#!/usr/bin/env python

import sys

higher_city = ""
higher_temp = "0"
lower_city = ""
lower_temp = "0"

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # get datas
    datas = line.split()
    # city
    city = datas[0]
    temp = datas[1]
    # convert count (currently a string) to int
    if float(temp) > float(higher_temp):
        higher_city = city
        higher_temp = temp

    if float(temp) < float(lower_temp):
        lower_city = city
        lower_temp = temp

print 'Max Temp: %s\t%s' % (higher_city, higher_temp)
print 'Min Temp: %s\t%s' % (lower_city, lower_temp)
