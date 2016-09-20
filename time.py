#!usr/bin/python
#
# Times the make_heap algorithm
#

import timeit
import random
import heap
import math

f = open( "mydata.txt", "w" )
ns = [ 10, 20, 30, 40,  50, 100, 200, 500, 1000, 10000 ]

print "n\tT(n)\tT(n)/nlgn"

for n in ns:
  L = random.sample(xrange(1,n+1), n)
  heap_time = timeit.Timer( "make_heap( L )", "from heap import make_heap; from __main__ import L")
  t = str( heap_time.timeit( 1 ))
  print str( n ) + "\t" + t
  f.write( str( n ) + "\t" + t + t/(n*math.log(n,2) ))

f.close()
