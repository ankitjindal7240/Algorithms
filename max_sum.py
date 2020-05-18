arr=[-2,1,-3,4,-1,2,1,-5,4]
sum_arr=[]
for i in range (len(arr)):
    sub_arr = []
    for j  in range (i,len(arr)):
        sub_arr.append(arr[j])
        #print(sub_arr)
        sum = 0
        for k in range(len(sub_arr)):
            sum = sum +sub_arr[k]
        sum_arr.append(sum)


#print(sum_arr)
print(max(sum_arr))
