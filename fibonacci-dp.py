# 1. bottom up approach
def fib(n):
    if n==0:
        return
    if n==1:
        return 0
    arr = [0] * n
    arr[0]=0
    arr[0]=0
    for i in range(2,n):
        arr[i]=arr[i-1]+arr[i-2]
    return arr

# 2. top down approach
def fib_(n):
    arr =[0,1]
    while len(arr)<n+1:
        arr.append(0)
    if n<=0:
        return "invalid input"
    if n==1:
        return 1
    if n==2:
        return 1
    arr[2]=1
    def fib2(n):
        if arr[n]:
            return arr[n]
        else:
            arr[n]=fib2(n-1)+fib2(n-2)

            return arr[n]
    return fib2(n)

print(fib_(2))
#0112358 13 21





