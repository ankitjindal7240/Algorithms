# 1st rectangle l1,r1
#2nd rectangle l2,r2
x1=1
y1=2
x2=3
y2=4

x3=5
y3=6
x4=7
y4=8
if (x2 - x1)>(x4 - x3) and (y2 - y1)>(y4 - y3):
    if x1 < x3 <x2 or x1 < x4 < x2:
        if y1 < y3 < y2 or y1 < y4 < y2:
            print("overlap")
    else:print("no overlaping")
else:
    if x3 < x1 <x4 or x3 < x2 < x4:
        if y3 < y1 < y4 or y3 < y2 < y4:
            print("overlap")
    else:print("no overlaping")
