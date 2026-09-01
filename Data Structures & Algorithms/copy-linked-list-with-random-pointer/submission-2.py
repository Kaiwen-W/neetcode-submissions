"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        list_map = {None: None} # copied node -> original node

        if not head:
            return None

        new_head = Node(x=head.val)
        list_map[head] = new_head

        node = head.next
        while node:
            list_map[node] = Node(x=node.val)
            node = node.next
        
        node = head
        new_head.next = list_map[head.next]
        new_head.random = list_map[head.random]
        while node:
            # next logic
            list_map[node].next = list_map[node.next]

            # random logic
            list_map[node].random = list_map[node.random]
        
            node = node.next

        return new_head
            