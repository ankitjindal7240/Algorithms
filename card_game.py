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
p1_score=[]
p2_score=[]



# distribute_4-4_cards_initially
for i in range(4):
    system.append([a.pop()])
    p1.append(a.pop())
    p2.append(a.pop())
print(p1)

bid=int(input("if no card is greater than 8 input 0"))

if bid==0:
    exit()
print(system)


match=input("if there is match input yes else no")
if match=="no":
    throw=int(input("enter the index of card"))
    system.append([p1.pop(throw)])
else:
    p1_score.append(p1.pop(int(input("give matched card index"))))
    pick=input("index of picked card")
    q=0
    for i in range(len(pick)):
        p1_score.append([system.pop(int(pick[i-q]))][0])
        q=q+1
print(p1_score,"\n",system,"\n")
if len(system)==0:
    p1_score.append(("sweep,25"))


for i in range(8):
        p1.append(a.pop())
        p2.append(a.pop())

# print(system)
def players_turn(player,score_card):
    print("your cards are",player)
    if len(system)==0:
        system.append([player.pop(int(input("index of card to be thrown")))])
    else:
        print("system cards are",system)
        choice=input("choose - pick,cement,kaccha")
        print(choice)
        if choice=="pick":
            pass
        elif choice=="cement":
            pass
        elif choice=="kaccha":
            pass

players_turn(p2,p2_score)
