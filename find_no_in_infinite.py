# #let the length of array infinite
# #we dont know mid or last element
# low =0
# #high =?
# if arr[0]==find:
#     print(0)
# if arr[1]==find:
#     print(1)
# if arr[2]==find:
#     print(2)
# if arr[10]==find
#from binary_recursive import binarySearch
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

arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170, 171, 172, 173, 174, 175, 176]
def find_no(array,to_find):
       if arr[0]==to_find:
              print(0)
       else:
              low=1
              while arr[low]<to_find:
                     low = 2*low #or we can multiply by 10,100,1000 etc. assuming that length of array is infinite
              low=low//2
              high = 2*low
              restult =binarySearch(arr,low,high,to_find)
              print(restult)
find_no(arr,100)


