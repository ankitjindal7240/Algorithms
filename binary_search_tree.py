class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def insert(root,value):
    if root is None:
        root=node(value)

    else:
        if root.value > value:
            if root.left is None:
                root.left=node(value)
            else:
                insert(root.left,value)
        else:
            if root.right is None:
                root.right=node(value)
            else:
                insert(root.right, value)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

a=[5,4,6,3,2,1,7,8,9]

def indert_from_array(array):
    root = node(array[0])
    for i in range(1,len(array)):
        insert(root,array[i])
    return root

r=indert_from_array(a)

inorder(r)