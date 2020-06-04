#stack
stack = [1,2,3,4,5]


def if_empty(stack):
    if stack==[]:
        return True
    else:
        return False
if_empty(stack)


def Push(stack,item):
    stack.append(item)
    print(stack)
Push(stack,6)


def Pop(stack):
        if if_empty(stack):
            print("no element found")
        else:
            print("top element is",stack.pop())
Pop(stack)


def display(stack):
    if stack==[]:
        print("Empty stack")
    else:
            print(stack[::-1])
display(stack)
