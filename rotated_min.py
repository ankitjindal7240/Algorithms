arr = [3,4,5,1,2]
for i in range(len(arr)):
    if arr[i+1]<arr[i]:
        print(arr[i+1])
        break
