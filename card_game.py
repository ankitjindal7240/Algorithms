import random
a=[]
for i in range(1,14):
    a.append(("diamonds",i))

for i in range(1,14):
    a.append(("spades",i))

for i in range(1,14):
    a.append(("hearts",i))

for i in range(1,14):
    a.append(("clubs",i))
random.shuffle(a)


p1=[]
p2=[]
system=[]
# distribute all cards initially
for i in range(4):
    system.append(a.pop())
while a:
    p1.append(a.pop())
    p2.append(a.pop())
print(system)

p1_score=[]
p2_score=[]
def players_turn(player,score_card):
    for card in system:
        for cards in player:
            if card[1]==cards[1]:
                score_card.append(player.pop(player.index(cards)))
                score_card.append(system.pop(system.index(card)))
                return
    # not so intelligent  players😅
    system.append(player.pop())


while p1 and p2:
    players_turn(p1, p1_score)
    players_turn(p2, p2_score)


# print(system)
# print(p2_score)
# print(p1_score)

s1=0
s2=0

def count_score(score_card):
    s=0
    for card in score_card:
        if card[0]=="spades":
            s=s+card[1]
        if card[1]==1 and card[0]!="spades":
            s=s+1
        if card[0]=="diamonds" and card[1]==10:
            s=s+6

    return s
s1=count_score(p1_score)
s2=count_score(p2_score)
print(s1,s2)
if s1>s2:
    print("player 1 is winner")
else:
    print("player 2 is winner")