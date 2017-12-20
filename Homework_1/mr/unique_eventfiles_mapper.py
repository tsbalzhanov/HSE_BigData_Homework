#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function
import sys

# load percentiles
with open('percentiles.csv', 'r') as f:
	_percentiles = f.readlines()
_percentiles = [ x.strip().split('\t') for x in _percentiles ]
# a dict of form: antiNucleus: (5-th percentile, 95-th percentile)
percentiles = {}
for x in _percentiles:
	percentiles[int(x[0])] = ( float(x[1]), float(x[2]) )
del _percentiles

for line in sys.stdin:
	line = line.strip().split(', ')
	antiNucleus, prodTime, eventFile = int(line[0]), float(line[10]), int(line[1])
	# filter on condition: prodTime lies between 5-th and 95-th percentiles
	if (prodTime >= percentiles[antiNucleus][0]) and (prodTime <= percentiles[antiNucleus][1]):
		print("%s\t%s" % (antiNucleus, eventFile))
