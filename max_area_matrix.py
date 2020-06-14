def max_area_histogram(a):
    max_area=0
    i=0
    stack =[]
    while i<len(a):
        if len(stack)==0:
            stack.append(i)
            i+=1
        elif len(stack)!=0 and a[stack[-1]]<=a[i]:
            stack.append(i)
            i += 1
        elif a[stack[-1]]>a[i]:
            highest_value=a[stack.pop()]
            #stack.pop()
            if len(stack)!=0:
                area = highest_value * (i - stack[-1] - 1)
            else:area =highest_value*(i)

            max_area=max(area,max_area)
    while len(stack) != 0:
        highest_value=a[stack.pop()]
        if len(stack)!=0:
            area = highest_value * (i - stack[-1] - 1)
        else:
            area = highest_value * (i)

        max_area = max(area, max_area)
    return max_area




def max_area_matrix(input):
    max_area_m=0
    no_of_rows=len(input)
    no_of_columns= len(input[0])
    i=0
    for i in range(1,no_of_rows):# skipping first row because its elements are its hight
        for j in range(no_of_columns):
            if input[i][j]==1: # if ith row's jth element is 1 then we add the totla no of previous ones
                input[i][j] =input[i][j] + input[i-1][j]   # i.e. hight of elemrnt of same column element in previous element
        temp_max_area=max_area_histogram(input[i-1])        # i-1 is because we have to find area of first row also
        if temp_max_area>max_area_m:
            max_area_m=temp_max_area
    temp_max_area=max_area_histogram(input[i])              #this is for the last row
    if temp_max_area>max_area_m:
        max_area_m=temp_max_area
    print(max_area_m)






input= [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
input=[[1]]
input=[[1],[1]]
input=[[1,1]]
input=[[0,1]]
input=[[0,1],[1,0]]
input=[1,1,1],[1,1,1]
input=[1,1,1],[1,0,1]
max_area_matrix(input)
