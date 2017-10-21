from node import Node

class LinkedList(object):
  """docstring for ClassName"""
  def __init__(self):
    self.head = None
    self.size = 0

  def merge_list(self, l1,l2):
    temp = None
    if l1 is None:
      return l2
    if l2 is None:
      return l1
    if l1.value <= l2.value:
      temp = l1
      temp.next = self.merge_list(l1.next, l2)
    else:
      temp = l2
      temp.next = self.merge_list(l1,l2.next)
    return temp

  def merge_sort(self, head):
    if head is None or head.next is None:
      return head
    l1,l2 = self.divide_list(head)
    l1 = self.merge_sort(l1)
    l2 = self.merge_sort(l2)
    head = self.merge_list(l1,l2)
    return head

  def merge_sort(self, head):
    if head is None or head.next is None:
      return head
    l1,l2 = self.divide_list(head)
    l1 = self.merge_sort(l1)
    l2 = self.merge_sort(l2)
    head = self.merge_list(l1,l2)
    return head

  def divide_list(self,head):
    fast = head
    slow = head
    detach_node = None
    if fast.next:
      fast = fast.next
    while fast is not None:
      detach_node = slow
      slow = slow.next
      if fast.next:
        fast = fast.next
      else:
        fast = None
    front = head
    detach_node.next = None
    back = slow
    return front,back

  def reverse(self):
    if self.head is None or self.head.next is None:
      return head
    prev = None
    current = self.head
    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

  # Move last element to front of a given Linked List
  def move_last(self):
    previous_node = self.head
    current = self.head
    if self.head.next:
      current = current.next
    while current.next is not None:
      current = current.next
      previous_node = previous_node.next
    current.next = self.head
    self.head = current
    previous_node.next = None

  def insertInBeginning(self, value):
    if self.head is None:
      newNode = Node(value)
      self.head = newNode
      self.size += 1
    else:
      newNode = Node(value)
      newNode.next = self.head
      self.head = newNode
      self.size += 1

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
linked.insertInBeginning(4)
linked.insertInBeginning(5)
linked.insertInBeginning(6)
linked.insertInBeginning(1)
linked.insertInBeginning(100)
linked.insertInBeginning(-1)
linked.reverse()
# linked.insertAtTail(4)
# linked.insertAtTail(5)
# linked.insertAtTail(1)
# linked.insertAtTail(5)
# linked.insertAtTail(6)
# linked.merge_sort(linked.head)
# linked.move_last()
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