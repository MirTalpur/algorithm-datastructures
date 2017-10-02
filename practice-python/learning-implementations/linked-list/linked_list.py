from node import Node

class LinkedList(object):
  """docstring for LinkedList"""
  def __init__(self):
    self.head = None
    self.counter = 0

  #O(N) traverses through a linked list and prints
  def traverseList(self):
    actualNode = self.head
    while actualNode is not None:
      print(actualNode.data)
      actualNode = actualNode.nextNode

  # constant time complexity
  # O(1)
  def insertStart(self, data):
    self.counter += 1
    newNode = Node(data)

    if not self.head:
      self.head = newNode
    else:
      newNode.nextNode = self.head
      self.head = newNode

  #O(1)
  def size(self):
    return self.counter

  #O(N)
  def insertEnd(self):
    self.counter += 1
    newNode = Node(data)
    actualNode = self.head

    #iterate through the nodes
    while actualNode.nextNode is not None:
      actualNode = actualNode.nextNode

    actualNode.nextNode = newNode

  #O(N)
  def remove(self, data):
    #head we need to get rid of
    self.counter -= 1
    if self.head:
      if data == self.head.data:
        self.head = self.head.nextNode
      else:
        self.head.remove(data, self.head)
    