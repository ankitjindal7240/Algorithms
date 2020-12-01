import time
# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
arr = [6,8,2,55,4,99,9,21,2,13]

def insertion(array):
    initial = time.time()
    for i in range (0,len(array)-1):
        for j in range(0,len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    print(array)
    print(time.time()-initial)

insertion(arr)

a =[1,3]
b=[2,5]
c = a+b
print(c)
