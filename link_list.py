class node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
def insert(self,value):
    new_node=node(value)
    if self.head==None:
        self.head=new_node
    else:
        temp =self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
def delete_node(self,value):
    temp =self.head
    node_to_be_deleted=node(value)
    # if node_to_be_deleted.next==None:
    #     temp=self.head
    #     while temp.next
    while temp.next!=(node_to_be_deleted or None):
        tempt=temp.next
    if temp.next==None:
        return
    if node_to_be_deleted.next == None:
        temp.next=None
    else:
        temp.next=temp.next.next
def insert_after_a_node(self,insert_after,value):
    new_node=node(value)
    after=node(insert_after)
    temp=self.head
    while temp.next!=after:
        temp=temp.next
    x=temp.next.next
    after.next=new_node
    new_node.next=x



