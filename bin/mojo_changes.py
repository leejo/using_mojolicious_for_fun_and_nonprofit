#!/usr/bin/python

import numpy as np
import pylab as plt
import sys

from optparse import OptionParser
from dateutil.parser import parse
from matplotlib.dates import date2num, num2date


parser = OptionParser()
parser.add_option( "-c",dest="changes",help="Changes file" )

( options,args ) = parser.parse_args()

infile   = options.changes;
changes  = {}
keywords = {
	'Updated'    : 'white',
	'Fixed'      : 'white',
	'Improved'   : 'white',
	'Relaxed'    : 'white',
	'Added'      : 'white',

	'Changed'    : 'black',
	'Replaced'   : 'black',
	'Merged'     : 'black',
	'Deprecated' : 'black',
	'Removed'    : 'black',
}

with open( infile ) as inf:

	for line in inf:

		line = line.rstrip( '\n' )
		words = line.split( " " )

		if len( words ) > 1:

			if words[0] != "":
				version = words[0]
				date    = date2num( parse( words[2] ) )

				if '2013' in words[2]:
					break
				changes[date] = {}

			elif words[2] == "-":
				change = words[3]
				if change in changes[date].keys():
					changes[date][change] = changes[date][change] + 1
				else:
					changes[date][change] = 1

last_plot = []
plots     = []
keys      = []

for keyword in sorted(keywords.keys()):

	print keyword
	keys.append( keyword )

	for date in changes.keys():
		if keyword not in changes[date].keys():
			changes[date][keyword] = 0

	this_plot = [ changes[date][keyword] for date in sorted(changes.keys()) ]

	if len( last_plot ) == 0:
		last_plot = [ 0 for date in changes.keys() ]

	print this_plot

	plots.append( plt.bar(
		[ num2date( date ) for date in sorted(changes.keys()) ],
		this_plot,
		bottom=last_plot,
		color=keywords[keyword]
	) )

	last_plot=this_plot

plt.title('Mojolicious Changes (since start of year)')
plt.show()
