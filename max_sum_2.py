#if more than one sub arrays give same sum

import sys
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
#arr = [-2, -3, -4, -1]
#arr = [1,2,3,4,5]
#arr = [1,2,3,4,5,-99]
#arr = [1,2,3,4,5,-99,199]
#arr = [1,2,3,4,5,-99,99]
#arr = [299,1,2,3,4,5,-99,199]
#arr =[1,2,3,4,5,-99,4,5,6,-199,5,10,-299]
#arr =[1,2,3,4,5,-99,4,5,6,-199,5,10,-299,599]

max_sum = -sys.maxsize - 1
print(max_sum)
curr_sum = 0
start_index =0
j=0
for i in range(len(arr)):
    curr_sum = curr_sum + arr[i]
    if curr_sum >= max_sum:
        max_sum = curr_sum
        end_index = i
        start_index=j
    if curr_sum < 0:
        curr_sum = 0
        j= i+1
print(max_sum)
curr_sum1 =0
start_index=0
z =0
for k in range(len(arr)):
    curr_sum1 = curr_sum1 + arr[k]
    if curr_sum1 == max_sum:
        end_index = k
        start_index = z
        print("max giving  sub array =", arr[start_index:end_index + 1])
    if curr_sum1 < 0:
        curr_sum1 = 0
        z = k + 1
