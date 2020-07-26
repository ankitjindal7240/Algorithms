a1=[1,1,2,3,4,5,6,7,8,9,10]
#3-2-1 -6-5-4- 9-8-7-
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

def reverse_list(l1, group):
    i=group
    prev=None
    curr=l1
    start =curr
    next=l1.next
    if next is None:
        return curr
    while i and next:
        curr.next=prev
        prev=curr
        curr=next
        next=next.next
        i=i-1
    if next is None  and i!=0:
        curr.next = prev
        prev = curr
        start.next=None
        return prev
    else:
        start.next=reverse_list(curr, group)
        return prev



l=linklist()
l.head= reverse_list(l1.head,4)
print_list(l)



