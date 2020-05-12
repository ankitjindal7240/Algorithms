#1.
arr = [1,5,5,6,6,9,9]
i=0
if arr[len(arr)-1]==arr[len(arr)-2]:                        #checking the last element
    while i<=(len(arr)-2):                                  #-2 is because we are increasing 2 in i
        if arr[i]==arr[i+1]:
            i=i+2
        else:                                                #jis element ka pair nhi mila return kar do
            print(arr[i])
            break
else:
    print(arr[len(arr)-1])                                  #agar last element single ho

#2 merge sort method
arr2 = [1,5,5,6,6,9,9]
def find_single(array):
    if len(array)==3:                                       #kyoki jab aaray ki lenght 3 ho jati hai usko break karne ke chakkar me infinite recurssion ho jate hai
        if array[0]==array[1]:                             #beech wale element ka pair jarur hoga
            print(array[2])
        else:print(array[0])

    else:
        mid = len(array) // 2
        a=(len(array)-1)/2                                 #mid element nikalne ke baad dono arrays me kitne kitne element bache
        if a%2==1:                                         #bache hue aaray me agar odd no of element ho to ye
            if array[mid]==array[mid-1]:                   #agar mid element ka pair left side me hai to
                find_single(array[mid-1:len(array)])       # mid -1 isliye kara hai kyoki jo pair hai mid ka use bhi include karna hai
            elif array[mid]==array[mid+1]:                 #agar mid element ka pair right side me hai to
                find_single(array[:mid+2])                 # mid +2 islye kara hai kyoki mid aur mid ke pair dono ko lena hai
            else:
                print( array[mid])
        else:                                              #dono side agar even no of elments ho to
            if array[mid]==array[mid+1]:                   #agar mid element ka pair right side me hai to
                find_single(array[mid:len(array)])
            elif array[mid]==array[mid-1]:                 #agar mid element ka pair left side me hai t
                find_single(array[:mid+1])                 #mid+1 kypki mid ko bhi include karna hai
            else:
                print( array[mid])
find_single(arr2)
