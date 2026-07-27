# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        values = []
        current = head
        
        # 1. Walk the whole list and save the values
        while current:
            values.append(current.val)
            current = current.next
            
        # 2. Reset back to the start
        current = head
        
        # 3. Walk it again, popping values off the end of our array
        # .pop() automatically removes and returns the last item
        while current:
            current.val = values.pop()
            current = current.next
            
        # The structure hasn't changed, but all the values are reversed
        return head
