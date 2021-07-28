class Node:
    def __init__(self,value):
        self.info = value
        self.link = None
class SinglyLinkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        p = self.start
        if p == None:
            print("List Empty")
            return
        else:
            while p is not  None:
                print(p.info," ",end=' ')
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n+=1
            p = p.link
        print("No of Nodes in the list=  ",n)

    def search(self,x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, " is at position ",position)
                return True
            position+=1
            p = p.link
        else:
            print(x," is not found in the list")
            return False

    def insert_in_beg(self,data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_in_end(self,data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of "))
    def insert_before(self,data,x):
        pass
    def insert_after(self,data,x):
        pass
    def insert_at_position(self,data,k):
        pass