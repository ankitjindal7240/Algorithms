import time

arr = [6,8,55,4,9,21,2,13]
def insertion(array):
    for i in range(1,len(array)):
        corr_val = array[i]
        j = i-1
        while j>=0 and corr_val < array[j]:
            # right shift the elements which are greater than current element
            array[j+1] = array[j]
            j -=1 # j = j -1
        array[j+1] = corr_val
    print(array)
insertion(arr)


