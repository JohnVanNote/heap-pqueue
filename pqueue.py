#!/usr/bin/env python
#
# Created by John Van Note
# Created on 2/14/12
#
# Makin' Priority Queues from Heaps
#

from heap import *

class PQueue():
  # Default constructor
  # A heap is used to keep structure of priority
  # ... which maps to a dictionary for its 
  # ... corresponding element
  def __init__( self ):
    self.heap = []
    self.pq = {}

  # Checks to see if pqueue is empty
  # @return true if empty, false if not
  def is_empty( self ):
    if self.heap == [] or self.heap == None:
      return True
    return False

  # Inserts an element in the pqueue
  # @elem is the element to be inserted
  # @priority is its level of priority
  # if there is already an element with the same level
  # ...of priority, the old element is given on level
  # ...higher of priority to maintain structure
  def insert( self, elem, priority=0 ):
    if self.pq.has_key( priority ):
      already_there = self.pq[priority]
      self.pq[ priority ] = elem
      return self.insert( already_there, priority+1 )
    insert( self.heap, priority )
    self.pq[priority] = elem

  # Remove the element with the highest priority
  def remove_max( self ):
    maxheap = self.heap[0]
    maxpq = self.pq[maxheap]
    delete( self.heap, maxheap )
    del self.pq[ maxheap ]
    return maxpq

  # Helper function for testing
  def printpq( self ):
    print self.heap
    print self.pq

def main():
  a = PQueue()
  if a.is_empty():
    print "True"
  a.insert( "John", 100 )
  a.insert( "Julia", 200 )
  a.insert( "Yench", 3 )
  a.insert( "Austin", 75 )
  a.insert( "Frankie", 300 )
  a.insert( "Woody", 125 )
  a.insert( "BOOOM", 301 )
  a.insert( "Hope this works", 300 )
  a.printpq()
  x = a.remove_max()
  if a.is_empty():
    print "True"
  a.printpq()
  

if __name__ == "__main__":
  main()
