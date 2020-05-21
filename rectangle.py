# 1st rectangle l1,r1
#2nd rectangle l2,r2
x_of_l1=1
y_of_l1=2
x_of_r1=3
y_of_r1=4

x_of_l2=5
y_of_l2=6
x_of_r2=7
y_of_r2=8
if (x_of_r1-x_of_l1)>(x_of_r2-x_of_l2) and (y_of_r1-y_of_l1)>(y_of_r2-y_of_l2):
    if x_of_l1 < x_of_l2 <x_of_r1 or x_of_l1 < x_of_r2 < x_of_r1:
        if y_of_l1 < y_of_l2 < y_of_r1 or y_of_l1 < y_of_r2 < y_of_r1:
            print("overlap")
    else:print("no overlaping")
else:
    if x_of_l2 < x_of_l1 <x_of_r2 or x_of_l2 < x_of_r1 < x_of_r2:
        if y_of_l2 < y_of_l1 < y_of_r2 or y_of_l2 < y_of_r1 < y_of_r2:
            print("overlap")
    else:print("no overlaping")
