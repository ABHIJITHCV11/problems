"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy_real = Node(0,head,None)
        curr_real = dummy_real.next
        
        dummy_new = Node(0,None,None)
        curr_new = dummy_new

        d1 = {}

        while curr_real:
            temp = Node(curr_real.val,None,None)
            curr_new.next = temp
            d1[curr_real] = temp

            curr_new = curr_new.next
            curr_real = curr_real.next

        # print(dummy_new.val)
        # print(dummy_new.next.val)
        # print(d1) 

        curr_real = dummy_real.next
        x = dummy_new.next

        while curr_real:

            if curr_real.random is None:
                x.random = None
            else:    
                x.random = d1[curr_real.random]
            
            x = x.next
            curr_real = curr_real.next

        return dummy_new.next