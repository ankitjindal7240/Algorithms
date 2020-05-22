# (x1,y1)=(1,2)
# (x2,y2)=(3,4)
# (x3,y3)=(5,6)         #no overlapping       
# (x4,y4)=(7,8)

# (x1,y1)=(0,0)
# (x2,y2)=(2,3)
# (x3,y3)=(0,0)        #Overlapping
# (x4,y4)=(1,2)

# (x1,y1)=(0,0)
# (x2,y2)=(6,7)
# (x3,y3)=(8,9)        # Not Overlapping
# (x4,y4)=(9,10)

#(x1,y1)=(-2,-1)
# (x2,y2)=(3,3)
# (x3,y3)=(-5,4)        # no Overlapping
#(x4,y4)=(-3,7)

(x1,y1)=(-2,0)
(x2,y2)=(1,2)
(x3,y3)=(-4,-2)        # Not Overlapping
(x4,y4)=(-3,1)

if (x2 - x1)>(x4 - x3) and (y2 - y1)>(y4 - y3):
    if x1 < x3 <x2 or x1 < x4 < x2:
        if y1 < y3 < y2 or y1 < y4 < y2:
            print("overlap")
    else:print("no overlaping")
else:
    if x3 < x1 <x4 or x3 < x2 < x4:
        if y3 < y1 < y4 or y3 < y2 < y4:
            print("overlapping")
    else:print("no overlapping")

