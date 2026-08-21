# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        
# In this solution we reverse all the pointers from pointing from right to left
# 1 -> 2 -> 3 -> becomes 1 <- 2 <- 3
# We set a null pointer at the beginning of the list and work on the head
# The next node is stored in a temporary variable and then we have the current node point to prev behind it
# Then we shift our variables to work on the next node
# We return prev since it will eventually be the new head