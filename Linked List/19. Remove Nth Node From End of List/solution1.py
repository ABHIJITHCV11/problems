# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        return self.onePass(head,n)
        return self.twoPass(head,n)


    def twoPass(self, head: ListNode | None, n:int) -> ListNode | None:
        dummy = ListNode(0,head)
        
        last, cnt = dummy, 0
        
        while last.next:
            last = last.next
            cnt+=1

        steps = cnt-n

        curr = dummy

        for i in range(steps):
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next

    def onePass(self, head: ListNode | None, n:int) -> ListNode | None:    
        dummy = ListNode(0,head)
        slow, fast = dummy, head

        for i in range(n):
            fast = fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next    