class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_number(l1, l2):
    pass

def add_one(lnode1=ListNode(0), lnode2=ListNode(0), plus=0):
    
    val1 = lnode1.val if lnode1 is not None else 0
    val2 = lnode2.val if lnode2 is not None else 0
    val = val1 + val2 + plus

    digit_one = val % 10
    digit_ten = val // 10

    new_node = ListNode(val=digit_one)

    return new_node, digit_ten

def add_two_number(l1, l2):
    head = res = ListNode(None)
    plus = 0
    while (l1 is not None or l2 is not None or plus > 0):
        node, plus = add_one(l1, l2, plus)
        l1 = l1.next if l1 is not None else l1
        l2 = l2.next if l2 is not None else l2
        res.next = node 
        res = res.next 
    return head.next



if __name__ == '__main__':
    s = 21/10  
    print(s)
