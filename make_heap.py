#!usr/bin/python

class Heap:
  def __init__( self ):
    self.heap = []

  def __init__( self, heap ):
    if heap == [] or None:
      self.heap = []
      return
    for items in heap:
      self.heap.insert( items )
