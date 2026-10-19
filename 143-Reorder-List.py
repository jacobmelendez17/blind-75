# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None

        head1, head2 = head, prev
        while head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp

# In this solution, we use a slow and fast pointer, and linked list reversal to reorder the linked list
# We start by getting the middle with a slow and fast pointer. Starting after that middle, we reverse the second half
# We then merge the two lists by alternating between them starting with the first half of the original list