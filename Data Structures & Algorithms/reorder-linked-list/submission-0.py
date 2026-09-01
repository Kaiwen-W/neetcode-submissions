# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# keep head at the same place
# last, first, second last, second, etc

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []

        node = head
        while node:
            nodes.append(node)
            node = node.next
        
        l = 0
        r = len(nodes) - 1

        while l < r:
            nodes[l].next = nodes[r]

            l += 1

            nodes[r].next = nodes[l]
            
            r -= 1
        
        nodes[l].next = None
