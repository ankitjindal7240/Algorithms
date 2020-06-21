
def sun_facing_buildings(buildings):
    i=1
    j=0
    stack=[]
    stack.append(buildings[0])
    while i<len(buildings):
        if buildings[i]>buildings[j]:
            stack.append(buildings[i])
            j=i
        i=i+1
    print(len(stack))
# a=[1,2,3,4,5]
# a=[5,4,3,2,1]
# a=[5,4,3,2,1,6,7,8,9]
a=[7,4,8,2,9]
sun_facing_buildings(a)