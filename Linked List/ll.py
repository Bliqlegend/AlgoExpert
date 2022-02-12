class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
# Next is just a pointer
# Data is what we pass while calling
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

def lengthofLL(head):
    curr = head
    l = 0
    while curr is not None:
        l+=1
        curr = curr.next
    return l


def printLL(head):
    curr = head
    while curr is not None:
        print(str(curr.data)+'->',end=' ')
        curr = curr.next
    print("None")
    return

def StakeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode 
    return head

def OtakeInput():
    # TC :O(n^2)
    inputList = [int(ele) for ele in input().split()]
    head = None
    
    for currData in inputList:
        if currData == -1:
            break    
        newNode = Node(currData)
        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode 

    return head
# input a list and move over it converting each element to a node adding to the linked list
# when -1 is entered it automatically breaks the pattern

# a = StakeInput()
# printLL(a)