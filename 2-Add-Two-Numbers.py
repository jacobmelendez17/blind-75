# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        result = dummy
        total = carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1: 
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return result.next

# In this solution, we create a dummy node to hold the result of the addition of the two numbers held in linked lists
# We also create a result pointer to hold the head of our resulted linked list
# For every digit/node, we add the values of both lists if they exist. The remainder of the total is put into that node
# And the carry is calculated by integer division