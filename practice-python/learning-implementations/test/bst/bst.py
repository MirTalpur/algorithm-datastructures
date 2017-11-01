from node import Node

class BST(object):
  """docstring for BST"""
  def __init__(self):
    self.root = None

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
bst.insert(1)
bst.traverse_tree()