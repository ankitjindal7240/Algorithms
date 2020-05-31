def water_traping(array):
    max_element = max(array)
    ans = i = z = 0
    j = len(array) - 1
    for k in range(max_element):
        if len(array) > 1:                              #if length of array is 1 ans =0
            while i < j and array[i] < array[i + 1]:    # jab tak  array aage se sorted hai
                i = i + 1
            while j > i and array[j] < array[j - 1]:    #jab tak  array peeche se sorted hai
                j = j - 1
            while array[i] < k+1:                       #jis level pe check kar rhe hai usse kam level ke element chod denge ,from starting
                i = i+1
            while array[j] < k+1:                       #from end
                j = j-1
            array = array[i:j + 1]
            i = 0
            j = len(array) - 1
            for z in range(0,k+1):                      #counting aal element below the level
                ans = ans + array.count(z)
    print(ans)
arrs=[[0,1,0,1,2,4,4,2,1,0,0,0,2,1],[1,2,3,4,5],[5,4,3,2,1],[1,2,3,4,5,4,3,2,1],[0,1,0,2,1,0,1,3,2,1,2,1],[1,1,1,2,0,0,0,5,5,4,3,2,3,4,5,7]]
for arr in arrs:
    water_traping(arr)