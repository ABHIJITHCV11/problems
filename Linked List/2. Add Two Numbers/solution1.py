# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        dummy = ListNode(0,None)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            
            if l1: digit1 = l1.val
            else : digit1 = 0

            if l2: digit2 = l2.val
            else: digit2 = 0 

            total = digit1 + digit2 + carry

            digit = total % 10
            carry = total // 10

            temp = ListNode(digit,None)
            curr.next = temp

            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next