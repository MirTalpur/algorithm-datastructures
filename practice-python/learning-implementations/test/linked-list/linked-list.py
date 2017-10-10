from node import Node

class LinkedList(object):
  """docstring for ClassName"""
  def __init__(self):
    self.head = None
    self.size = 0
  
  def insertAtTail(self, value):
    if self.head is None:
      newNode = Node(value)
      self.head = newNode
      self.size = self.size + 1
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      newNode = Node(value)
      current.next = newNode
      self.size = self.size + 1

  def traverse(self):
    if self.head is None:
      print('No nodes in the linked list')
      return
    else:
      nodeIterator = self.head
      while nodeIterator.next is not None:
        print(nodeIterator.value)
        nodeIterator = nodeIterator.next
      print(nodeIterator.value)

  def list_size(self):
    return self.size

  def sort_using_array(self):
    current = self.head
    list_to_array = []
    while current.next is not None:
      list_to_array.append(current.value)
      current = current.next
    list_to_array.append(current.value)
    list_to_array.sort()
    # keep a copy of the current linked list
    copy = self.head
    # Set the head of the new sorted linked List
    self.head = Node(list_to_array[0])
    # set the rest of the linked list
    for value in list_to_array[1:]:
      self.insertAtTail(value)

    # delete the original linked list
    while copy.next is not None:
      temp = copy
      copy = copy.next
      del temp.value
      del temp.next

  def remove(self, value):
    if self.head.value is value:
      newHead = self.head.next
      del self.head.value
      del self.head.next
      self.head = newHead
      self.size -= self.size
    else:
      if self.head is not None:
        if self.list_size() > 2:
          newNode = self.head.next.next
          previousNode = self.head.next
          if previousNode.value is value:
            self.head.next = newNode
            del previousNode.value
            del previousNode.next
            del previousNode
            self.size -= 1
          else:
            while newNode.value is not value:
              previousNode = previousNode.next
              newNode = newNode.next

            previousNode.next = newNode.next
            del newNode.next
            del newNode.value
            del newNode
            self.size -= 1
        else:
          if self.list_size() is 2:
            newNode = self.head.next
            if newNode.value is value:
              self.head.next = None
              del newNode.value
              del newNode.next
              del newNode
              self.size -= 1
            else:
              print('Value not in list')
          else:
            if self.head.value is not value:
              print('Value not in list')

linked = LinkedList()
linked.insertAtTail(3)
linked.insertAtTail(4)
linked.insertAtTail(5)
linked.insertAtTail(1)
linked.insertAtTail(5)
linked.insertAtTail(6)
linked.sort_using_array()
linked.traverse()
# print(linked.list_size())
# linked.remove(4)
# print(linked.list_size())
# linked.remove(5)
# print(linked.list_size())
# linked.insertAtTail(4)
# linked.insertAtTail(4)
# linked.remove(4)
# linked.traverse()
# print(linked.list_size())