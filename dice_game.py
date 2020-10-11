import random
players=[]
no_of_palyers=int(input('enter the no of players'))
target=int(input('enter the points to win'))
score=[0]*no_of_palyers
for player  in range(no_of_palyers):
    players.append(f"p{player+1}")
random.shuffle(players)

no_of_1s={}
for player in range(no_of_palyers):
    no_of_1s[f"p{player+1}"]=0


print(players)
# print(score)

def dice():
    p= random.randint(1,6)
    if p!=6:
        print(f"you have scored {p}")
        return p
    else:
        input("wow it is a six press enter to roll again")
        p= p + dice()
        print(f"you have  total scored {p}")
        return p


rank = 1
winners = []
rank_list=[]
while players:

    for i in range(len(players)):
        if no_of_1s[players[i]]==2:
            print(f"{players[i]} have two consecuative 1s so your turn is skipped")
            no_of_1s[players[i]] = 0
            continue
        input(f"it is your turn {players[i]}!! press enter to continue")
        point_on_dice=dice()
        if point_on_dice==1:
            no_of_1s[players[i]]= no_of_1s[players[i]]+1
        else:
            no_of_1s[players[i]] = 0
        score[i] = score[i] + point_on_dice
        if score[i] >= target:
            print(f"you have completed the target your rank is {rank}")
            rank_list.append(f"rank {rank} - {players[i]}")

            rank = rank + 1
            winners.append(i)

        print(players)
        print(score)
        print(rank_list)

    # print(winners)
    poped = 0
    while len(winners) != 0:
        score.pop(winners[0] - poped)
        players.pop(winners.pop(0) - poped)
        poped = poped + 1
