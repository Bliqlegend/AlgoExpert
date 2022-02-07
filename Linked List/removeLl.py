from ll import *

def deleteNode(head,index):
    curr = head
    prev = None
    count = 0
    if head is None:
        return None
    if index == 0:
        return head.next
    while curr is not None:
        if count == index:
            if curr.next is None:
                curr = prev
                prev.next = None
            else:
                prev.next = curr.next
                curr = curr.next.next
        count+=1
        prev = curr
        curr = curr.next
    return head


def duplicate(head):
    hash = {}
    curr = head
    count = 0
    hash[curr.data] = True
    while curr is not None:
        if curr.data in hash:
            deleteNode(curr,count)
            curr = curr.next
        else:
            hash[head] = True
            curr = curr.next
        count+=1
    return head


head = StakeInput()
head = duplicate(head)
printLL(head)
