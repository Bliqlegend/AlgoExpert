from ll import *

def removefromEnd(head,k):
    n = lengthofLL(head)
    slow =head
    fast = head
    cslow = 0
    cfast = 0
    while fast.next is None and fast.next.next is None:
        if cfast == n - k:
            deleteNode(fast,1)
        elif cslow == n-k:
            deleteNode(slow,1)
        elif cfast == n- k+1:
            deleteNode(fast,0)
        elif cslow == n - k +1:
            deleteNode(slow,0)
        slow = slow.next
        fast = fast.next.next
    return head


head = StakeInput()
n = int(input())
head = removefromEnd(head,n)
printLL(head)