
def push(stack,item):
    stack.append(item)
def operation(operator,stack):
    if operator=="c":
        if len(stack)>0:
            stack.pop()
        else:
            print("invalid expression")
            exit()
    if operator=="d":
        if len(stack)>0:
            push(stack,2*stack[-1])
        else:
            print("invalid expression")
            exit()
    if operator=="+":
        if len(stack)>1:
            push(stack,stack[-1]+stack[-2])
        else:
            print("invalid expression")
            exit()



def baseball(expression):
    stack=[]
    for i in range(len(a)):
        if a[i].isnumeric():
            push(stack,int(a[i]))
        else:
            operation(a[i],stack)
    print(sum(stack))
    print(stack)
a=["5","2","c","d","+"]#30
a = ["10", "20", "d","d","d","+"]#550
a = ["10","20","d","d","d","+","c","c"]#150
a=["10","20","c","d","c","+","d","10"]#invalid expression
a=["5","2","c","d","+"]#30
baseball(a)