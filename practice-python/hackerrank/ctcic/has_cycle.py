"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
def has_cycle(head):
    if head.next is None:
        return False
    else:
        slow = head
        fast = head
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
        else:
            return False
        if slow is None or fast is None:
            return False
        if slow is fast:
            return True 
