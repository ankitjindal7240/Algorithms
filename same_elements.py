def binarySearch(arr, l, r, x):
    if r >= l:

        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        return -1

def first_index(array,x):
    if array[0]==x:
        return 0
    else:
        result = binarySearch(array, 0, len(array) - 1, x)
        if result == -1: return -1
        while array[result]==x:
            result=result-1
        return result +1
def last_index(array,x):
    if array[-1]==x:
        return len(array)-1
    else:
        result = binarySearch(array, 0, len(array) - 1, x)
        if result==-1:return -1
        while array[result]==x:
            result=result+1
        return result-1

arr = [0,0,0,0,2,5,5,5,6,6,8,8,9,9,9]
for i in range(10):
    print(first_index(arr,i),last_index(arr,i))
