def remove_sorted(a):
    i = 0
    j = len(a) - 1
    while i < len(a)-1:
        if a[i+1] > a[i]:
            break
        i = i + 1
    while j > 0:
        if a[j] > a[j - 1]:
            break
        j = j - 1
    a = a[i:j + 1]
    return a

def max_benifit(a):
    a = remove_sorted(a)
    if len(a)==0:
        return
    maximum=max(a[:])
    i=a.index(maximum)
    minimum=min(a[:i+1])
    max_arr.append(maximum-minimum)
    if i==len(a)-1:
        return
    else:max_benifit(a[i+1:])


# driver code
stocks=[[7,1,5,3,6,4],[3,5,7,1,5],[6,9,1,5],[7,6,5,4],[5,5,5],[5],[0,0,1,0,0,2],[1,2,3,4,5],[1,2,3,4,1,2,14,63,63,63,53,5,3,3,24,4,42,4,345,42,4,4,224,3,3]]
for stock in stocks:
    max_arr = []
    max_benifit(stock)
    if len(max_arr)==0:
        print("no profit")
    else:
        print(max(max_arr))



