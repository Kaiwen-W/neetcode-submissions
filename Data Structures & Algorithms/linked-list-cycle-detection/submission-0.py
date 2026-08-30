# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {} # node -> index
        node = head

        i = 0
        while node:
            seen[node] = i
            i += 1

            node = node.next
            if node in seen:
                return True
        
        return False


        