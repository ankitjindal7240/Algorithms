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

def reverse_list(l1):
    l1=l1.head
    temp1=l1.next           #2
    if temp1 is None:
        return
    temp2=temp1.next        #3
    l1.next=None            # 1.next =NONE
    while temp2:
        temp1.next=l1       #2.next=1
        l1=temp1            #linklist starts fron 1
        temp1=temp2
        temp2=temp2.next
    temp1.next=l1           #for last digit
    l1=temp1
    temp1=temp2
    result=linklist()
    result.head=l1
    return result
l= reverse_list(l1)
print_list(l)




# dry run

# temp=l1 #1
# temp2=temp.next#5
# temp3=temp2.next #9
# l1.next.next=l1#5->1
# l1=l1.next
# temp=temp2
#
# temp=temp3.next
# temp3.next=l1
# l1=temp3
#
# temp2=temp.next
# temp.next=l1
# l1=temp
#
# temp=temp2.next
# temp2.next=l1
# l1=temp2
#
# temp=l1
# print(temp.data)
# while temp!=None:
#     print(temp.data)
#     temp=temp.next



# temp.next=l1
# l1=temp
# temp=temp2
# temp2=temp2.next
#
#
# temp.next=l1
# l1=temp
# temp=temp2
# temp2=temp2.next
#
# temp.next=l1
# l1=temp
# temp=temp2
# temp2=temp2.next
#
# temp.next=l1
# l1=temp
# temp=temp2