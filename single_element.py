#1.
arr = [1,5,5,6,6,9,9]
i=0
if arr[len(arr)-1]==arr[len(arr)-2]:
    while i<=(len(arr)-2):
        if arr[i]==arr[i+1]:
            i=i+2
        else:
            print(arr[i])
            break
else:
    print(arr[len(arr)-1])

#2 merge sort method
arr2 = [1,5,5,6,6,9,9]
def find_single(array):
    if len(array)==3:
        if array[0]==array[1]:
            print(array[2])
        else:print(array[0])

    else:
        mid = len(array) // 2
        a=(len(array)-1)/2
        if a%2==1:
            if array[mid]==array[mid-1]:
                find_single(array[mid-1:len(array)])
            elif array[mid]==array[mid+1]:
                find_single(array[:mid+2])
            else:
                print( array[mid])
        else:
            if array[mid]==array[mid+1]:
                find_single(array[mid:len(array)])
            elif array[mid]==array[mid-1]:
                find_single(array[:mid+1])
            else:
                print( array[mid])
find_single(arr2)
