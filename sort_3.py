arr =[0,1,2,0,1,2]
#arr =[2,1,0,1,2,0,1,2,1,0,2,2,2,2]
#arr =[2,1,0,1,2,0,1,2,1,0]
# arr =[2,0,0,1,0]
# arr =[2,0,0,0]
# arr =[0,2]
# arr =[2,0]
# arr =[2,0]
# arr=[0,1,2]
# arr=[0,2,1]
left =0
right =len(arr)-1
i = 0
if len(arr)==1:
    print("array is sorted")
else:
    while i <=right:
        while arr[right] == 2:
             right=right-1
        if arr[left]==0:
            left=left+1
            i = i+1
        if arr[i]==0:
            arr[i],arr[left]=arr[left],arr[i]
            i = i-1
        if arr[i]==2 and right>i:
            arr[i], arr[right] = arr[right], arr[i]
            i = i-1
        if left>=right:
            break
        i = i+1
    print(arr)