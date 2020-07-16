array = [4,3,2,1]

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
l1=create_list_using_array(l1,array)

def insert_2(linklist,node):
    if linklist.head==None:
        linklist.head = node
        linklist.last = linklist.head

def merge(l1,l2):
    l3 = linklist()
    l1=l1.head
    l2=l2.head
    if l1==None:
        return l2
    if l2==None:
        return l1
    temp=None
    if l1.data<l2.data:
        temp=l1
        l1=l1.next
    else:
        temp=l2
        l2=l2.next
    l3.head=temp
    while l1 and l2:
        if l1.data<l2.data:
            temp.next=l1
            l1=l1.next
        else:
            temp.next=l2
            l2=l2.next
        temp=temp.next
    if l1:
        temp.next=l1
    if l2:
        temp.next=l2
    return l3

def merge_sort(l1):
    if l1.head is None:
        return l1
    if l1.head.next is None:
        return l1
    mid =l1.head
    fast=l1.head
    while fast and fast.next:
        if fast.next.next is None:
            break
        mid=mid.next
        fast=fast.next.next
    left=l1

    right=linklist()
    temp=mid.next
    right.head=temp
    mid.next=None

    l=merge_sort(left)
    r=merge_sort(right)
    return merge(l,r)
l1=merge_sort(l1)
print_list(l1)