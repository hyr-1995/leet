# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
                print(right.val)
                right = right.next 
            print("!!!!!!",left.val, right.val)
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
                curr.next = pre #!!!!!!!!!!!!
                curr = left 
                left = right

            else:
                return dumy.next


def main():
    
    temp = ListNode(1)
    inputs = head = temp
    for i in range(2,10):
        temp.next = ListNode(i)
        temp = temp.next

    while(head is not None):
        print(head.val)
        head = head.next
        
    print("=================================")
    s = Solution()
    res = s.reverseKGroup(inputs, 2)

    while(res.next is not None):
        print(res.val)
        res = res.next
        

if __name__ == '__main__':
    main()
        