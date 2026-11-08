class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.bruteforce(head)

    def bruteforce(self, head: ListNode | None) -> None:
        if not head or not head.next:   # 0 or 1 node: nothing to reorder
            return

        start = head
        end = head
        cnt = 0

        while end.next:   # safe now: end is guaranteed non-None
            end = end.next
            cnt += 1

        while cnt > 0:
            end = start
            temp = start.next

            for _ in range(cnt):
                end = end.next

            start.next = end
            end.next = temp
            start = temp

            cnt -= 2

        start.next = None   # cut leftover pointer / self-loop