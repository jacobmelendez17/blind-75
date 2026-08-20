# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

# In this two pointer solution, we have a slow pointer and a fast pointer
# The slow pointer moves one step at a time and the fast pointer moves two
# If there is a cycle, the fast pointer will eventually meet the slow pointer