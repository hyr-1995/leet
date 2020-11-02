def remove_ele(head, val):
    st = pre = ListNode(val=None, next=head)

    cur = head 
    

    while cur is not None:
        if cur.val == val:
            pre.next = cur.next 
        else:
            pre = cur
        cur = cur.next    
        
    return st.next
