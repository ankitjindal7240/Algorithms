a1=[1,2,3,4,5,6]
class node:
    def __init__(self,data):
        self.data =data
        self.next= None
class linklist:
    def __init__(self):
        self.head=None
        self.last=None

def insert(linklist,value):
    if linklist.head==None:
        linklist.head = node(value)
        linklist.last = linklist.head
    else:
        linklist.last.next = node(value)
        linklist.last = linklist.last.next

def create_list_using_array(l,array):
    for i in range(len(array)):
        insert(l,array[i])
    return l

def print_list(linklist):
    temp=linklist.head
    while temp!=None:
        print(temp.data)
        temp=temp.next
l1=linklist()
l1=create_list_using_array(l1,a1)



# main

def reverse_using_recursion(prev, current):
    if current is None:
        return prev
    next=current.next

    current.next=prev
    prev=current
    current=next
    if next:
        next=next.next
    return reverse_using_recursion(prev, current)
l2=linklist()
l2.head=reverse_using_recursion(None, l1.head)
print_list(l2)
