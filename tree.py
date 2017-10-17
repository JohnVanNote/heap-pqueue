#!/usr/bin/env python

class Tree:
  def __init__( self ):
    self.data = None
    self.left = None
    self.right = None

  def __init__( self, parent ):
    self.data = parent
    self.left - None
    self.right = None

  def setLeft( self, left ):
    self.left = left

  def setRight( self, right ):
    self.right = right

  def getData( self ):
    return self.data 

  def getLeft( self ):
    return self.left

  def getRight( self ):
    return self.right

  def isEmpty( self ):
    if self.data == None:
      return True
    return False
