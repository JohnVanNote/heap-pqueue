#!usr/bin/python
# 
# Created by John Van Note
# Creadted on 2/11/12
#
# Heaps and whatnot
#

import random
import timeit

# Stupid main function
def main():
  n = 30
  L = random.sample(xrange(1,n+1), n)
  heap = make_heap(L)

# Creates a heap
# @param elems is list
# @return is a heap (list)
def make_heap( nHeap ):
  if len( nHeap ) == 0:
    return
  heap = []
  for elem in nHeap:
    insert( heap, elem )
  nHeap = heap
  return nHeap

# Inserts an element in a heap
# @param heap is the heap (list)
# @param elem is an integer to be inserted
def insert( heap, elem ):
  heap.append( elem )
  up_heap( heap, len(heap)-1 )

# Deletes an item from heap
# @param heap is the heap (list)
# @elem is the elem to be delete
def delete( heap, elem ):
  if not find( heap, elem ): return
  index = heap.index( elem )
  heap[index] = heap[len(heap)-1]
  heap.pop(len(heap)-1)
  down_heap( heap, index )
  
# Makes sure the structure of a heap stays in tack
# @param heap is the heap(list)
# @index is the index of item being checked
def up_heap( heap, index ):
  if index == 0: return
  if heap[index] > heap[parent(index)]:
    temp = heap[index]
    heap[index] = heap[parent(index)]
    heap[parent(index)] = temp
    up_heap( heap, parent( index ))

# Makes sure the structure of the heap stays in tack
# @param heap is the heap (list)
# @param index is the index of item being checked
def down_heap( heap, index ):
  if left(index) > len(heap)-1: 
    if right(index) > len(heap)-1:
      return
    else:
      if heap[right(index)] > heap[index]:
        temp = heap[index]
        heap[index] = heap[right(index)]
        heap[right(index)] = temp
  elif right(index) > len(heap)-1:
    if heap[left(index)] > heap[index]:
      temp = heap[index]
      heap[index] = heap[left(index)]
      heap[left(index)] = temp
  else:
    if heap[left(index)]>heap[right(index)] or right(index)>len(heap)-1:
      if heap[left(index)] > heap[index]:
        temp = heap[index]
        heap[index] = heap[left(index)]
        heap[left(index)] = temp
        down_heap( heap, left( index ))
    else:
      if heap[right(index)] > heap[index]:
        temp = heap[index]
        heap[index] = heap[right(index)]
        heap[right(index)] = temp
        down_heap( heap, right( index ))

# Finds an item in a heap
# @param heap is the heap (list)
# @param elem is the elem to be searched (int)
# returns true if the elem is in the list, false if not
def find( heap, elem ):
  for item in heap:
    if item == elem:
      return True
  return False 


# finds the parent of index
def parent( i ):
  return (i-1)/2

# Finds the left child of index
def left( i ):
  return 2*i+1

# Finds the right child in index
def right( i ):
  return 2*i+2

if __name__ == "__main__":
  main()
