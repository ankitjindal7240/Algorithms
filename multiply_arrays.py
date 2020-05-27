arr1 =[9,0,9]
arr2=[5,5]
def sum_arr_1(arrays): #if we have multiple no arrays of diffrent length and we have to find sum
    lengths = []
    for array in arrays:
        lengths.append(len(array))
    answer=[]
    carry=0
    for j in range(1,max(lengths)+1):
        sum = 0 + carry
        carry=0
        for array in arrays:
            if j <=len(array):
                sum = sum +array[-j]
        if sum>9:
            carry=sum//10
            sum=sum%10
            answer.insert(0,sum)
        else:
            carry=0
            answer.insert(0,sum)
    if carry!=0:
        answer.insert(0, carry)
    print(answer)
def multiply(array1,array2):
    arrays=[]
    for i in reversed(range(0,len(arr2))):
        multiplier=arr2[i]
        new_array=[]
        carry = 0
        for j in reversed(range(0,len(arr1))):
            elememt =arr2[i]*arr1[j]+carry
            carry=0
            if elememt>9:
                carry=elememt//10
                elememt=elememt%10

                new_array.insert(0,elememt)
            else:
                carry=0
                new_array.insert(0, elememt)
        if carry!=0:
            new_array.insert(0,carry)
        new_array = new_array+[0]*(len(arr2)-i-1)
        arrays.append(new_array)
    sum_arr_1(arrays)
multiply(arr2,arr1)






