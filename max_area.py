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



