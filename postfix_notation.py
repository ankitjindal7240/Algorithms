def push(stack,item):
    stack.append(item)
def operation(operator,n1,n2):
    if operator=="+":
        return n1+n2
    if operator=="-":
        return n1-n2
    if operator=="*":
        return n1*n2
    if operator=="%":
        return n1/n2
a="24+46+*"
def polish_notation(expression):
    stack=[]
    for i in range(len(a)):
        if a[i].isnumeric():
            push(stack,a[i])
        else:
            if len(stack)>=2:
                n1=float(stack.pop(0))
                n2=float(stack.pop((0)))
                ans=operation(a[i],n1,n2)
                push(stack,ans)
            else:
                print("invalid expression")
                return
    if len(stack)==1:
        print(stack.pop(0))
    else:print("invalid expression")
polish_notation(a)




