# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head

        dumy = ListNode(None)
        dumy.next = head 
        curr = dumy
        left = curr.next
        right = left
        
        while 1:
            count = 0
            
            while(count < k and right is not None):
                count += 1
                right = right.next 
            if count == k:
                # reverse
                # next_list = right.next
                pre = right
                cur = left
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                curr.next = right 
                curr = left 
                left = right

            else:
                return dumy.next
        