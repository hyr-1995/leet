def rotate_list(head, k):
    cur = head 
    lens = 0
    if k == 0:
        return head
    while(cur is not None):
        tail = cur
        cur = cur.next
        lens += 1

    if lens <= 1:
        return head 

    if k > lens:
        k = k % lens

    x1 = lens - k

    count = 0
    cur = head
    if x1<lens and x1>0:
        while count< x1:
            point = cur
            cur = cur.next
            
            count += 1


        tail.next = head 
        point.next= None 
    return cur