#arr = [2, 4, 6, 8, 12]
#arr = [2,6,8,10,12]
#arr = [2,4,6,10,12]
#arr = [2,4,6,8,10,14]
#arr = [2,6,8,10,12,14]
arr=[1, 6, 11, 16, 21, 31]
diff = (arr[-1] - arr[0]) / len(arr)
def missing_1(array):
    for i in range(len(arr)-1):
        if (arr[i+1]-arr[i])!=diff:
            print(arr[i]+diff)
            break
missing_1(arr)





def missing(array):
    mid =len(array)//2
    midth_term = array[0] + (mid) * diff
    if array[mid] == midth_term:
        if (array[mid + 1] - array[mid]) != diff:
            print(array[mid] + diff)
            return exit()
        else:
            missing(array[mid:])
    if array[mid]>midth_term:
        if (array[mid]-array[mid-1])!=diff:
            print (array[mid]-diff)
            return exit()
        else:
            missing(array[:mid+1])
missing(arr)