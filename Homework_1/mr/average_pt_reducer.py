#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function
import sys

previous_antiNucleus = None
collected_Pts = []

def reduce(antiNucleus, Pts):
	# calculate average Pt
	avg_Pt = sum([ x / len(Pts) for x in Pts ])
	print('%s\t%i' % (antiNucleus, avg_Pt))

for line in sys.stdin:
	antiNucleus, Pt = line.strip().split('\t')
	if antiNucleus != previous_antiNucleus:
		if previous_antiNucleus is not None:
			reduce(previous_antiNucleus, collected_Pts)
			collected_Pts = []
	collected_Pts.append(float(Pt))
	previous_antiNucleus = antiNucleus

reduce(previous_antiNucleus, collected_Pts)
