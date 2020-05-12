arr1 = [1,3,5,7,9,11]
arr2 = [2,4,6,8,10,12]
a = (len(arr1)+ len(arr2))%2
b = (len(arr1)+ len(arr2))//2
c = b+1
i=0
j=0
k=0
if a==0:
    while i < len(arr1) and j < len(arr2) and k<=b:
        if arr1[i]<arr2[j]:
            i=i+1
            k=k+1
            if k==b or k==c:
                print(arr1[i-1])

        else:
            j=j+1
            k=k+1
            if k==b or k==c:
                print(arr2[j-1])

    print((arr1[i-1]+arr2[j-1])/2)
else:
    while i < len(arr1) and j < len(arr2) and k<=c:
        if arr1[i] < arr2[j]:
            i = i + 1
            k = k + 1
            if k==c:
                print(arr1[i-1])
        else:
            j = j + 1
            k = k + 1
            if k == c:
                print(arr2[j-1])

