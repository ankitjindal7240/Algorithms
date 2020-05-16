arrs = [[6,8,55,4,9,21,2,13],[2,3,4,5,1,6],[1,1,-1,-2,5,5,6,0]]
def insertion_sort(array):
    for index in range (1,len(array)):
        current_index = index
        current_value = array[index]
        while current_index>0 and current_value< array[current_index-1]:
            array[current_index]=array[current_index-1]
            current_index = current_index-1
        array[current_index]=current_value
    print(array)
for arr in arrs:
     insertion_sort(arr)