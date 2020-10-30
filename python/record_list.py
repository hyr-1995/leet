def recordlist(self, head):

    # 1. find the middle point
    
    slow = head 
    fast = head 

    while (fast.next is not None and fast.next.next is not None):
        slow = slow.next 
        fast = fast.next.next 

    middle = slow 

    # 2. reverse the behind of middle
    
    rev_pre = None
    rev_cur = middle.next

    while (rev_cur is not None):
        temp = rev_cur.next 
        rev_cur.next = rev_pre 
        rev_pre = rev_cur
        rev_cur = temp 

    middle.next = None 

    while rev_pre is not None:
        temp = head.next
        head.next = rev_pre 
        temp2 = rev_pre.next 
        rev_pre.next = temp 

        head = temp 
        rev_pre = temp2 

    return head

