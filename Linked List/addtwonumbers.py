from ll import *

def add2nums(head1,head2):
    result = Node(0)
    result_tail = result
    carry = 0

    curr1 = head1
    curr2 = head2

    while curr1 or curr2 or carry:
        val1 = (curr1.data if curr1 else 0)
        val2 = (curr2.data if curr2 else 0)

        carry,out = divmod(val1+val2+carry,10)
        result_tail.next  = Node(out)
        result_tail = result_tail.next

        curr1 = (curr1.next if curr1 else None)
        curr2 = (curr2.next if curr2 else None)
    return result.next