from node import Node

class BST(object):
  """docstring for BST"""
  def __init__(self):
    self.root = None

  def getMin(self, parent_node):
    if parent_node.left is None:
      return parent_node.data
    else:
      return  self.getMin(parent_node.left)

  def _remove(self, value, parent_node, temp_node):
    if value < parent_node.data:
      if parent_node.left is not None:
        self._remove(value, parent_node.left, parent_node)
    elif value > parent_node.data:
      if parent_node.right is not None:
        self._remove(value, parent_node.right, parent_node)
    else:
      if parent_node.left is not None and parent_node.right is not None:
        parent_node.data = self.getMin(parent_node.right)
        self._remove(parent_node.data, parent_node.right, parent_node)
      elif temp_node.left == parent_node:
        if parent_node.left is not None:
          temp = parent_node.left
        else:
          temp = parent_node.right
        temp_node.left = temp
      elif temp_node.right == parent_node:
        if parent_node.left is not None:
          temp = parent_node.left
        else:
          temp = parent_node.right
        temp_node.right = temp

  def remove(self, value):
    if self.root is not None:
      if self.root.data == value:
        temp_node = Node(None)
        temp_node.left = self.root
        self._remove(value, self.root, temp_node)
      else:
        self._remove(value, self.root, None)

  def _insert(self, value, parent_node):
    if value < parent_node.data:
      if parent_node.left is None:
        parent_node.left = Node(value)
      else:
        self._insert(value, parent_node.left)
    else:
      if parent_node.right is None:
        parent_node.right = Node(value)
      else:
        self._insert(value, parent_node.right)

  def insert(self, value):
    if self.root is None:
      new_node = Node(value)
      self.root = new_node
    else:
      self._insert(value, self.root)

  # traver in order from lowest to highest values in BST
  def _traverse_tree(self, parent_node):
    if parent_node.left is not None:
      self._traverse_tree(parent_node.left)
    print(parent_node.data)
    if parent_node.right is not None:
      self._traverse_tree(parent_node.right)

  def traverse_tree(self):
    if self.root is not None:
      self._traverse_tree(self.root)

bst = BST()
bst.insert(2)
bst.insert(3)
bst.remove(3)
bst.traverse_tree()