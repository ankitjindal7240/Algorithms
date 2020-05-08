array = [6,8,55,4,99,9,21,2,13,17]
mid = len(array)//2
i=0
while i<= mid:
    array[i],array[len(array)-i-1]=array[len(array)-i-1],array[i]
    i=i+1
print(array)




