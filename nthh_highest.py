arr =[2,4,5,3,44,5,66,77,77,55]
#arr =[0,0,0,0]
#arr =[-1,-1,-2]
#arr =[-1]
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
def kth_highest(arr,low,high,k):
    pi = partition(arr, low, high)
    if pi==len(arr)-k:
        print( arr[pi])
    if pi<len(arr)-k:
        kth_highest(arr,pi+1,high,k)
    if  pi > len(arr)-k:
        kth_highest(arr,low,pi-1,k)
k = int(input("enter the vakue of k"))
ans =kth_highest(arr,0,len(arr)-1,k)




