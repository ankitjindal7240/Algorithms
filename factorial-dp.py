# 1.
def factorial_1(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return n*(factorial_1(n-1))
# print(factorial_1(5))

#2.
def factorial_2(n):
    if n==0:
        return 1
    ans=1
    for i in range(1,n+1):
        ans = i*ans
    return ans

# print(factorial_2(5))

# 3. using dp
arr =[1]
def fatorial_3(n):
    if len(arr)>=n+1:
        return arr[n]
    for i in range(len(arr),n+1):
        arr.append(i*arr[i-1])
    return arr[-1]
print(fatorial_3(6))
print(fatorial_3(7))

