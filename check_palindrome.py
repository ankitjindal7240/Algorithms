a1=[1,2,3,4,3,2,1]
#1->2->3->4<-3<-2<-1
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






def reverse_list(l1):
    temp1=l1.next
    if temp1 is None:
        return
    temp2=temp1.next
    l1.next=None
    while temp2:
        temp1.next=l1
        l1=temp1
        temp1=temp2
        temp2=temp2.next
    temp1.next=l1
    l1=temp1
    temp1=temp2
    l3=linklist()
    l3.head=l1
    return l3



def find_mid(linklist):
    temp=linklist.head
    if temp :
        if temp.next:
            temp2=temp.next
        else:
            return 0
    else:
        return 0
    while temp and temp2:
        if temp2.next:
            temp2=temp2.next.next
        else:

            return temp
        temp = temp.next
    return temp
# m=find_mid(l1)
# r=reverse_list(m)
# print(l1.head.next.data)
# print("")
# print(r.head.next.data)
def check_palindrome(l1):
    m=find_mid(l1)
    if m:
        r=reverse_list(m)
    else:
        return "not a palindrome"
    temp=l1.head
    temp2=r.head
    while temp:
        if temp.data==temp2.data:
            temp2=temp2.next
            temp=temp.next
        else:
            return "not a palindrome"

    return "it is a palindrome"
print(check_palindrome(l1))