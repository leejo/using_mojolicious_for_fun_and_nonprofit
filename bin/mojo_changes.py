#!/usr/bin/python

import numpy as np
import matplotlib.pylab as plt

fig = plt.figure()
ax  = fig.add_subplot( 111 )

changes = {}

ax.bar(
	sorted( months.keys() ),
	[ i for i in months.values() ],
)

plt.title('Mojolicious Changes (Last 6 Months)')
plt.xticks( x + w,  (sorted(months.keys())) )
plt.show()
