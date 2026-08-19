# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# In this recursive solution, we compare the heads of each sorted linked list and set it as the new head
# Every time we do this, we call the function again with the selected head being shifted to its next node

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next; cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next; cur = cur.next
        if list1 or list2:
            cur.next = list1 if list1 else list2
        
        return dummy.next

# In this iterative solution, we use a two pointer solution that uses a dummy to return the head of a new linked list
# cur is used to iterate through the values of the linked lists, find the greater value, and shift the nodes