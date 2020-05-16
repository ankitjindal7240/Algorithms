def find_single(array):
    if len(array)==3:                                       #kyoki jab aaray ki lenght 3 ho jati hai usko break karne ke chakkar me infinite recurssion ho jate hai
        if array[0]==array[1]:                             #beech wale element ka pair jarur hoga
            print(array[2])
        else:
           print(array[0])
    elif len(array)==1:
        print(array[0])
    else:
        mid = len(array)//2
        if array[mid]==array[mid+1]:
            l = mid%2
            r = (len(array)-mid-2)%2
            if l == 1:
                find_single(array[:mid])
            if r == 1:
                find_single(array[mid + 2:])
        elif array[mid]==array[mid-1]:
            l = (mid-1)%2
            r = (len(array)-mid-1)%2
            if l == 1:
                find_single(array[:mid - 1])
            if r == 1:
                find_single(array[mid + 1:])
        else: print( array[mid])
arrs = [[5,5,6,6,1,9,9,8,8],[5,5,6,6,9,9,8,8,1],[4,4,5,5,6,6,9,9,8,8,1],[1,5,5,6,6,9,9,8,8],[1,5,5,6,6,9,9,8,8,7,7],[5,5,6,6,9,9,1,8,8],[5,5,6,6,9,9,1,8,8,7,7],]
for arr in arrs:
    find_single(arr)