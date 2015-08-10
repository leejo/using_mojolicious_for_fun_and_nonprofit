#!/usr/bin/python

import numpy as np
import pylab as plt
import sys

from optparse import OptionParser
from dateutil.parser import parse
from matplotlib.dates import date2num, num2date

parser = OptionParser()
parser.add_option( "-c",dest="changes",help="Changes file" )
parser.add_option( "-v",dest="version",help="Start Version" )

( options,args ) = parser.parse_args()

infile   = options.changes;
if options.version:
	version = options.version;
else:
	version = 0.2
changes  = {}

keywords = {
	'Updated'    : 'green',
	'Fixed'      : 'green',
	'Improved'   : 'green',
	'Relaxed'    : 'green',
	'Added'      : 'green',
	'Simplified' : 'green',
	'Cleaned'    : 'green',
	'Reduced'    : 'green',
	'Increased'  : 'green',
	'Refactored' : 'green',
	'Optimized'  : 'green',
	'Rewrote'    : 'green',
	'Modernized' : 'green',

	'Deprecated' : 'orange',

	'Moved'      : 'red',
	'Disabled'   : 'red',
	'Combined'   : 'red',
	'Changed'    : 'red',
	'Replaced'   : 'red',
	'Merged'     : 'red',
	'Removed'    : 'red',
	'Renamed'    : 'red',
}

latest_version = 0

with open( infile ) as inf:

	for line in inf:

		line = line.rstrip( '\n' )
		words = line.split( " " )

		if len( words ) > 1:

			if words[0] != "":
				change_version = words[0]
				date    = date2num( parse( words[2] ) )

				if change_version == version:
					break
				changes[date] = {}

			elif words[2] == "-":
				if latest_version == 0:
					latest_version = change_version
				change = words[3]
				if change in changes[date].keys():
					changes[date][change] = changes[date][change] + 1
				else:
					changes[date][change] = 1

version   = change_version
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

	#print this_plot
	#print last_plot

	plots.append( plt.bar(
		[ num2date( date ) for date in sorted(changes.keys()) ],
		this_plot,
		bottom=last_plot,
		color=keywords[keyword]
	) )

	for i in range( len( this_plot ) ):
		last_plot[i] = last_plot[i] + this_plot[i]

plt.title('Mojolicious Changes (version %s to %s)' % ( version,latest_version ))
plt.show()
