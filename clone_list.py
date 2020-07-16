class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.random=None
# class linklist:
#     def __init__(self):
#         self.head=None

l1=node(1)
l1.next=node(2)
l1.next.next=node(3)
l1.next.next.next=node(4)
l1.next.next.next.next=node(5)



# random pinters
l1.random = l1.next.next

l1.next.random = l1
l1.next.next.random = l1.next.next.next.next

l1.next.next.next.random = l1.next.next.next.next

l1.next.next.next.next.random = l1.next

def print_list(l1):
    while l1:
        print(l1.data)
        l1=l1.next

def print_random(l1):
    while l1:
        if l1.random:
            print(l1.random.data)
        else:
            print("null")
        l1=l1.next


def clone_list(l1):
    clone=node(l1.data)
    temp1=l1.next
    temp2=clone
    while temp1:
        temp2.next=node(temp1.data)
        temp1=temp1.next
        temp2=temp2.next
    temp1=l1
    temp2=clone
    while temp1 and temp2:
        temp_of_temp1=temp1.next
        temp1.next=temp2
        temp2.random=temp1

        temp2=temp2.next
        temp1=temp_of_temp1

    temp2=clone

    while temp2:
        temp2.random=temp2.random.random.next
        temp2=temp2.next

    return clone

c=clone_list(l1)
print_random(c)