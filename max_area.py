a=[6,2,5,4,5,1,6]
# a=[1]
# a=[1,2]
# a=[1,2,3]
# a=[1,2,3,4,5 ]
# a=[9,8]
# a=[9,8,7]
# a=[1,2,3,4,5,4,3,2,1]
# a=[1,1,1,1]
max_area=0

for i in range(len(a)):
    left_index=i
    right_index=i
    while left_index>=0 and a[left_index]>=a[i]:
        left_index-=1
    left_index= left_index + 1
    while right_index <= len(a)-1 and a[right_index] >= a[i]:
        right_index= right_index + 1
    right_index= right_index - 1
    temp_max_area=a[i]*(right_index - left_index + 1)
    if temp_max_area>max_area:
        max_area=temp_max_area
print(max_area)
