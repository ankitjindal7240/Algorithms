array = [6,8,2,55,4,99,9,21,2,13]
def max(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return(arr)
def nth_highest_value(arr):
    print("input the order of higest no you want.")
    n = input()
    if int(n)<len(array):

        for i in range(int(n)):
            max(arr)
        print(arr[len(arr)-int(n)])
    else:
        print("plese provide input in range of array")
nth_highest_value(array)











