# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#    
             
#   实现优先队列
#   分治
#   

class ListNode:

    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


class SortedListNode(object):

    def __init__(self, value, node):
        self.val = value
        self.node = node
        self.next = None

class SortedList(object):

    def __init__(self):
        self.head = None

    def add(self, node):
        if self.head is None:
            self.head = node 
        else:
            temp = self.head
            while(temp.val < node.val and temp.next is not None):
                temp = temp.next
            next_node = temp.next
            temp.next = node 
            node.next = next_node
            

class PriorityQueue(object):

    def __init__(self):
        self.head = None

    def add(self, val, node):
        sort_node = SortedListNode(val, node)
        if self.head is None:
            self.head = sort_node
        else:
            temp = self.head
            if temp.val > sort_node.val:
                self.head = sort_node
                self.head.next = temp 
            else:
                while(temp.next is not None and temp.next.val < sort_node.val):
                    temp = temp.next
                next_node = temp.next 
                temp.next = sort_node 
                sort_node.next = next_node

    def pop(self):
        res = self.head
        self.head = self.head.next 
        return res.val, res.node

    def not_empty(self):
        if self.head is not None:
            return True
        else:
            return False

    def _string(self):
        temp = self.head
        while(temp and temp.next is not None):
            print(temp.val, temp.node)
            temp = temp.next
        print(temp.val, temp.node)

class Solution:
    def mergeKLists(self, lists):
        head = None
        s = None
        p = PriorityQueue()
        for item in lists:
            if item:
                p.add(item.val, item)

        while(p.not_empty()):
            val, node = p.pop()
            if head is None:
                # val, node = p.pop()
                head = ListNode(val)
                s = head
            else:
                
                s.next = ListNode(val)
                s = s.next
            if node.next is not None:
                node = node.next
                p.add(node.val, node)

        return head

def main():
    import random
    p = PriorityQueue()
    for i in range(10):
        p.add(random.randint(1,100), i)

    # p._string()
    while(p.not_empty()):
        val, node = p.pop()
        print(val, node)

if __name__ == '__main__':
    main()