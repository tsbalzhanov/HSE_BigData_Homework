#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function
import sys

previous_key = None
collected_values = []

def reduce(key, prodTimes):
	percentile_5 = prodTimes[len(prodTimes) // 20]
	percentile_95 = prodTimes[19 * len(prodTimes) // 20]
	print('%s\t%f\t%f' % (key, percentile_5, percentile_95))

for line in sys.stdin:
	key, prodTime = line.strip().split('\t')
	if key != previous_key:
		if previous_key is not None:
			reduce(previous_key, collected_values)
			collected_values = []
	collected_values.append(float(prodTime))
	previous_key = key

reduce(previous_key, collected_values)
