def binary_search_first(arr,l,r,x):
    if r>=l:
        mid = l + (r - l) // 2
        if arr[mid]==x:
            if arr[mid]!=arr[mid-1]:
                return mid
            else:
                return binary_search_first(arr,l,mid-1,x)
        elif arr[mid] > x:
            return binary_search_first(arr, l, mid - 1, x)
        else:
            return binary_search_first(arr, mid + 1, r, x)
    else:
        return -1

def binary_search_last(arr,l,r,x):
    if arr[-1]==x:
        return len(arr)-1
    if r>=l:
        mid = l + (r - l) // 2
        if arr[mid]==x:
            if arr[mid]!=arr[mid+1]:
                return mid
            else:
                return binary_search_last(arr,l,mid-1,x)
        elif arr[mid] > x:
            return binary_search_last(arr, l, mid - 1, x)
        else:
            return binary_search_last(arr, mid + 1, r, x)
    else:
        return -1
arr = [0,0,0,0,2,5,5,5,6,6,8,8,9,9,9]
for i in range(10):
    print(binary_search_first(arr,0,len(arr)-1,i),binary_search_last(arr,0,len(arr)-1,i))
#result
# 0 3
# -1 -1
# 4 4
# -1 -1
# -1 -1
# 5 7
# 8 9
# -1 -1
# 10 11
# 12 14
