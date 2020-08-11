import random
a = []
for i in range(1, 14):
    a.append(("🔶", i))

for i in range(1, 14):
    a.append(("♠️ ", i))

for i in range(1, 14):
    a.append(("❤️", i))

for i in range(1, 14):
    a.append(("♣️", i))
random.shuffle(a)

p1 = []
p2 = []
system = []
p1_score = []
p2_score = []
last_pickup=0

def vlaue_of_house(house_index):
    sum = 0
    deck = system[house_index]
    for card in deck:
        sum = sum + card[1]
    return sum



for i in range(4):
    system.append([a.pop()])
    p1.append(a.pop())
    p2.append(a.pop())

print("p1    =     ",p1)

bid = int(input("if none of  card is greater than 8 input 0  \n "))
if bid == 0:
    exit()
print("system   =   ",system)


choice = input("choose - pick,house,throw")
if choice == "pick":
    p1_score.append(p1.pop(int(input("index of card  in your  hand  \n "))))
    pick = input("index of cards to be picked")
    # check
    q = 0
    for i in range(len(pick)):
        p1_score.append([system.pop(int(pick[i - q]))][0])
        q = q + 1
    last_pickup=p1_score
    if len(system) == 0:
        p1_score.append(("sweep", 25))

elif choice == "throw":
    card = int(input("index of card to be thrown"))
    system.append([p1.pop(card)])



elif choice == "house":
    card = int(input("index of your card"))
    system_cards=input("index of system cards")
    s=p1[card][1]
    for i in range(len(system_cards)):
        s=s+system[int(system_cards[i])][0][1]
    print(s/bid)
    if (s/bid) == 1.0 or 2.0 or 3.0 or 4.0:
        house=[]
        house.append(p1.pop(card))
        for i in range(len(system_cards)):
            house.append(system[int(system_cards[i])][0])
        q=0
        for i in range(len(system_cards)):
            system.pop(int(system_cards[i])-q)
            q=q+1
        system.append(house)
    else:
        print("no")
        #check case

# #distribte again
# for i in range(8):
#     p1.append(a.pop())
#     p2.append(a.pop())



def players_turn(player, score_card):
    print("your cards are \n ", player)
    print("system cards are \n", system)
    if len(system) == 0:
        # if no card is there player have to throw a card
        system.append([player.pop(int(input("index of card to be thrown")))])


    else:
        choice = input("choose - pick,house,throw")

        if choice == "pick":
            card = int(input("index of your card \n "))
            score_card.append(player.pop(card))
            deck = input("index of cards to be picked")
            # check
            if len(deck)>1:
                q = 0
                for i in range(len(deck)):
                    score_card.append([system.pop(int(deck[i])-q)][0])
                    q = q + 1
            else:
                for i in range(len(system[int(deck[0])])):
                    score_card.append(system[int(deck[0])][i])
                system.pop(int(deck))
            last_pickup = score_card
            if len(system) == 0:
                score_card.append(("sweep", 50))

        elif choice == "throw":
            card = int(input("index of card to be thrown"))
            system.append([player.pop(card)])



        elif choice == "house":
            house = int(input(" to create pakka house choose 1 \n to create kaccha house choose 2  \n"
                              "  to contribute to pakka house choose 3 \n to contribute to kaccha house choose 4 \n"))
            if house == 1:
                your_card = int(input("index of your card"))
                system_deck = int(input("index of deck in system"))
                # check case
                system[system_deck].append(player.pop(your_card))

            elif house == 2:
                your_card = int(input("index of your card"))
                system_deck = int(input("index of deck in system"))
                # check case
                system[system_deck].append(player.pop(your_card))


            elif house == 3:
                card = int(input("index of your card"))
                system_deck = int(input("index of house in system"))

                if vlaue_of_house(system_deck)/player[card][1]==1.0 or 2.0 or 3.0 or 4.0:
                    system[system_deck].append(player.pop(card))
                else:

                    system_cards = input("index of system cards")
                    s = player[card][1]
                    for i in range(len(system_cards)):
                        s = s + system[int(system_cards[i])][0][1]
                        print(s)
                    if s==vlaue_of_house(system_deck):
                        system[system_deck].append(player.pop(card))
                        for i in range(len(system_cards)):
                            system[system_deck].append(system[int(system_cards[i])][0])
                        q = 0
                        for i in range(len(system_cards)):
                            system.pop(int(system_cards[i]) - q)
                            q = q + 1

            elif house == 4:
                card = int(input("index of your card"))
                system_deck = int(input("index of house in system"))
                system_cards = input("index of losse cardsif you want to include else -1 ")
                if int(system_cards)==-1 and 8 < (player[card][1] + vlaue_of_house(system_deck)) < 14:
                    system[system_deck].append(player.pop(card))
                elif vlaue_of_house(system_deck)/player[card][1]==1.0 or 2.0 or 3.0 or 4.0 :
                    system[system_deck].append(player.pop(card))
                else:
                    system_cards = input("index of system cards")
                    s = player[card][1]
                    for i in range(len(system_cards)):
                        s = s + system[int(system_cards[i])][0][1]
                        print(s)
                    if s == vlaue_of_house(system_deck):
                        system[system_deck].append(player.pop(card))
                        for i in range(len(system_cards)):
                            system[system_deck].append(system[int(system_cards[i])][0])
                        q = 0
                        for i in range(len(system_cards)):
                            system.pop(int(system_cards[i]) - q)
                            q = q + 1
            print(player, "\n", score_card, "\n", system)
while p1 and p2:
    players_turn(p2, p2_score)
    players_turn(p1, p1_score)
players_turn(p2, p2_score)

# for i in range(12):
#     p1.append(a.pop())
#     p2.append(a.pop())

while p1 and p2:
    players_turn(p1, p1_score)
    players_turn(p2, p2_score)

print(system,"\n",p1_score,"\n",p2_score)

def remaining_cards(score_card):
    for i in range(len(system)):
        for j in range(len(system[i])):
            score_card.append(system[i][j])

if last_pickup==p1_score:
    remaining_cards(p1_score)
else:
    remaining_cards((p2_score))
system=[]

def count_score(score_card):
    s=0
    for card in score_card:
        if card[0]=="♠️":
            s=s+card[1]
        if card[1]==1 and card[0]!="♠️":
            s=s+1
        if card[0]=="🔶" and card[1]==10:
            s=s+6
        if card[0]=="seep":
            s=s+card[1]

    return s
s1=count_score(p1_score)
s2=count_score(p2_score)
# print(p1,p2,system)
print(s1,s2)
if s1>s2:
    print("player 1 is winner")
else:
    print("player 2 is winner")
