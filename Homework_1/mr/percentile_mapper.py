#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function
import sys

for line in sys.stdin:
	line = line.strip().split(', ')
	antiNucleus, prodTime = line[0], line[10]
	print("%s\t%s\t" % (antiNucleus, prodTime))
