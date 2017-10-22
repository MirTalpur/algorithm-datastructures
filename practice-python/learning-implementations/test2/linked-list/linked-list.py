from node import Node

class linkedList(object):
  """docstring for linkedList"""
  def __init__(self):
    self.head = None
    self.size = 0

  def insert(self, value):
    if self.head is None:
      new_node = Node(value)
      self.head = new_node
      return
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

  def remove(self, value):
    current = self.head
    prev = None
    while current is not None:
      if current.value is value:
        if prev is not None:
          prev.next = current.next
        else:
          self.head = current.next
      prev = current
      current = current.next

  def divide_list(self, head):
    slow = head
    fast = head
    split_node = None
    if fast.next:
      fast = fast.next
    while fast is not None:
      split_node = slow
      slow = slow.next
      if fast.next:
        fast = fast.next
      else:
        fast = None
    front = head
    split_node.next = None
    back = slow
    return front,back

  def merge(self, l1, l2):
    if l1 is None:
      return l2
    if l2 is None:
      return l1
    if l1.value <= l2.value:
      temp = l1
      temp.next = self.merge(l1.next, l2)
    else:
      temp = l2
      temp.next = self.merge(l1, l2.next)
    return temp

  def merge_sort(self, head):
    if head is None or head.next is None:
      return head
    # divide the list
    # call merge_sort on the divided list and recursively
    # merge
    # and merge the two divided lists together
    l1,l2 = self.divide_list(head)
    l1 = self.merge_sort(l1)
    l2 = self.merge_sort(l2)
    head = self.merge(l1, l2)
    return head

  def reverse(self):
    if self.head is None or self.head.next is None:
      return
    prev = None
    current = self.head
    while current is not None:
      temp = current.next
      current.next = prev
      prev = current
      current = temp
    self.head = prev

  def reverse_util(self, current, prev):
    if current.next is None:
      current.next = prev
      self.head = current
      return
    temp = current.next
    current.next = prev
    self.reverse_util(temp, current)

  def reverse_recursively(self):
    if self.head is None or self.head.next is None:
      return
    self.reverse_util(self.head, None)

  # move last element to the front
  def move_last(self):
    if self.head is None or self.head.next is None:
      return
    current = self.head
    prev = None
    while current.next is not None:
      prev = current
      current = current.next
    current.next = self.head
    self.head = current
    prev.next = None

  def traverse(self):
    current = self.head
    while current is not None:
      print(current.value)
      current = current.next

linked = linkedList()
linked.insert(5)
linked.insert(4)
linked.insert(10)
linked.insert(-5)
# linked.move_last()
# linked.remove(6)
# linked.remove(5)
linked.traverse()
    