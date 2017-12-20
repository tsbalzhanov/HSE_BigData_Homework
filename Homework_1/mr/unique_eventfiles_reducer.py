#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function
import sys

previous_antiNucleus = None
collected_eventfiles = []

def reduce(antiNucleus, values):
	n_unique_values = len(set(values))
	print('%s\t%i' % (antiNucleus, n_unique_values))

for line in sys.stdin:
	antiNucleus, eventFile = line.strip().split('\t')
	if antiNucleus != previous_antiNucleus:
		if previous_antiNucleus is not None:
			reduce(previous_antiNucleus, collected_eventfiles)
			collected_eventfiles = []
	collected_eventfiles.append(float(eventFile))
	previous_antiNucleus = antiNucleus

reduce(previous_antiNucleus, collected_eventfiles)
