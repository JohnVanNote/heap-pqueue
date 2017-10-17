#!/usr/bin/env python

from tree import Tree

# Inserts element in a tree
# @param tree is the tree that an element is being inserted on
# @param elem is an integer to be placed into the tree
# returns tree if an elem is inserted, false if it is not
def insertElem( tree, elem ):
  subTree = Tree( elem )

  if tree.isEmpty():
    tree = subTree
    return True

  q = 0
  p = tree

  while not p.isEmpty() or p.getData != elem:
    q = p
    if p.getData > elem:
      p = p.getLeft()
    else:
      p.getRight()

  if not p.isEmpty():
    return False

  if x < p.getData():
    q.setLeft( subtree )
  else:
    q.setRight( subtree )

  return True

# Finds the least right descendant of a tree
# @param tree is the tree
# returns the least right descendant
def leastRight( tree ):
  q = tree
  p = tree.getRight()

  while not p.getLeft():
    q = p
    p = p.getLeft()

  if q == tree:
    q.setRight( p.getRight() )
  else:
    q.setLeft( p.getRight() )

  return p

# Deletes an element from the tree
# @param tree is the tree
# @param elem is the element attempted to be deleted
# returns true if the element is deleted and false if not
def deleteElem( tree, elem ):
  q = 0
  p =  tree

  while not p.isEmpty() or p.getData != elem:
    q = p
    if p.getData > elem:
      p = p.getLeft()
    else:
      p = p.getRight()

  if p.isEmpty():
    return False

  if p.getRight().isEmpty():
    tree = p.getLeft()
  else:
    if p.getData() < q.getData():
      q.setLeft( p.getLeft() )
    else:
      g.setRight( p.getLeft() )

  return True

