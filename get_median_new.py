arr1 = [5,6,9,15,16]
arr2 = [2,4,7,13]
a = (len(arr1)+ len(arr2))%2
b = (len(arr1)+ len(arr2))//2
c = b+1
i=0
j=0
k=0

while i < len(arr1) and j < len(arr2) and k<=c:
    if arr1[i]<arr2[j]:
        i=i+1
        k=k+1
        if a==0:
            if k==b:
                x  =arr1[i-1]
            if k==c:
                y= arr1[i-1]
        if a==1:
            if k==c:
                x = arr1[i - 1]
    else:
        j=j+1
        k=k+1
        if a==0:
            if k==b :
                x=arr2[j-1]
            if  k==c:
                y=arr2[j-1]
        if a==1:
            if k==c:
                x = arr2[j-1]

if a==1 and k<c:
    if len(arr1)<=i:
        x = arr2[j+(c-k)-1]
    if j>=len(arr2)  :
        x = arr1[i+(c-k)-1]
if a==0 and k<c:
    if i>=len(arr1):
       x= arr2[j+(b-k)-1]
       y= arr2[j+(b-k)]
    if j>=len(arr2) :
        x=arr1[i+(b-k)-1]
        y= arr1[i+(b-k)]

if a==0:
        print((x+y)/2)
else:
        print(x)

"""
results:
1.
arr1 = [5,6,9,15,16]
arr2 = [2,4,7,13]
ans- 7

2.
arr1 = [5,6,9,15,16]
arr2 = [2,4,7,13,88]
ans - 8

3.
arr1 = [9,13,16,17,18]
arr2 = [2]
ams - 14.5
4.
arr2 = [9,13,16,17,18]
arr1 = [2]
ans - 14.5

5.
arr2 = [9,13,16,17]
arr1 = [2]
ans - 13

6.
arr2 = [9,13,16,17]
arr1 = [99]
ans - 13
7.
arr2 = [9,13,16,17,18]
arr1 = [99]
ans- 16.5
8.


"""


