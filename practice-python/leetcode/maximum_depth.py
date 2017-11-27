class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def _insert(self, parent_node, val):
        if val < parent_node.val:
            if parent_node.left is None:
                parent_node.left = TreeNode(val)
            else:
                self._insert(parent_node.left, val)
        else:
            if parent_node.right is None:
                parent_node.right = TreeNode(val)
            else:
                self._insert(parent_node.right, val)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)


# one way to do it is set current to root and go
# through the left and right nodes
def max_depth(root):
    if root.left is None and root.right is None:
        return None
    left_count = 0
    current = root
    while current.left is not None:
        left_count += 1
        current = current.left
    current = root
    right_count = 0
    while current.right is not None:
        right_count += 1
        current = current.right
    if right_count > left_count:
        return right_count
    else:
        return left_count


# other way to do it
def maximum_depth(root):
    if root is None:
        return 0
    else:
        return max(maximum_depth(root.left), maximum_depth(root.right)) + 1


b_tree = BST()
b_tree.insert(1)
b_tree.insert(2)
b_tree.insert(2)
b_tree.insert(3)
print maximum_depth(b_tree.root)
