# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.revreseSol(head)
        # self.brutforce(head)

    def revreseSol(slef, head: ListNode | None) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse from slow till end of the list
        

        prev,curr = None, slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # fix the pointers

        start, end = head, prev

        # print('slow',slow)
        # print('prev',prev)
        # print('--')

        while end.next:
            temp_start = start.next
            temp_end = end.next

            start.next = end
            end.next = temp_start
            
            start = temp_start
            end = temp_end