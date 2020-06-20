#let the speed is k
#check if the monkey can finish banans with this speed
def check_speed(piles, hour, k):
    pile = piles[:]       #a local variable is intoduced
    i = 0
    while i < hour:
        if len(pile) == 0:
            break
        else:
            pile[0] = pile[0] - k
            if pile[0] <= 0:
                pile.pop(0)
        i = i + 1
    if len(pile) == 0:
        return 1
    else:
        return 0



#assumuming minimum speed is 1 and max speed is max no of banans in pile

def binary_search(left, right):
    if right >= left:
        mid = left + (right - left) // 2
        if check_speed(piles,hour,mid) == 1:# if checked speed is sufficient to complete bananas check in left half
            if check_speed(piles, hour, mid - 1) == 0:
                return mid
            else:
                return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)






def speed(piles,hour):
    if len(piles)==hour:
        return max(piles)
    else:
        return binary_search(1,max(piles))
# piles =[30,11,23,4,20]
# hour =5
#ans: 30
# piles =[30,11,23,4,20]
# hour =6
#ans: 23
piles =[3,6,7,11]
hour =8
#ans: 4
print(speed(piles,hour))


