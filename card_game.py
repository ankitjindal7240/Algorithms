import random

a = []
for i in range(1, 14):
    a.append(("diamonds", i))

for i in range(1, 14):
    a.append(("spades", i))

for i in range(1, 14):
    a.append(("hearts", i))

for i in range(1, 14):
    a.append(("clubs", i))
random.shuffle(a)

p1 = []
p2 = []
system = []
p1_score = []
p2_score = []


def vlaue_of_house(house_index):
    sum = 0
    deck = system[house_index]
    for card in deck:
        sum = sum + card[1]
    return sum


# distribute_4-4_cards_initially
for i in range(4):
    system.append([a.pop()])
    p1.append(a.pop())
    p2.append(a.pop())
print(p1)

bid = int(input("if none of  card is greater than 8 input 0  \n "))
if bid == 0:
    exit()
print(system)

match = input("if there is match input yes else no \n")
if match == "no":
    throw = int(input("if card is not matched enter the index of card you have to throw"))
    # check
    system.append([p1.pop(throw)])
else:
    p1_score.append(p1.pop(int(input("index of card  in your  hand  \n "))))
    pick = input("index of card matched with your card")

    q = 0
    for i in range(len(pick)):
        p1_score.append([system.pop(int(pick[i - q]))][0])
        q = q + 1

# print(p1_score,"\n",system,"\n")
if len(system) == 0:
    p1_score.append(("sweep",25))

# distribute cards again
for i in range(8):
    p1.append(a.pop())
    p2.append(a.pop())


# print(system)
def players_turn(player, score_card):
    print("your cards are \n ", player)
    if len(system) == 0:
        # if no card is there player have to throw a card
        system.append([player.pop(int(input("index of card to be thrown")))])



    else:
        print("system cards are \n", system)
        choice = input("choose - pick,house,throw")

        if choice == "pick":
            # add choice to pickup more than one deck
            deck = int(input("give the index of deck to be picked"))
            card = int(input("index of your card "))
            score_card.append(player.pop(card))
            for i in range(len(system[deck])):
                score_card.append(system[deck][i])
            system.pop(deck)
            # print(system,"\n",player,"\n",score_card,"\n")
            #add seep


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
                your_card = int(input("index of your card"))
                system_deck = int(input("index of house in system"))

                if player[your_card][1] == vlaue_of_house(system_deck):
                    system[system_deck].append(player.pop(your_card))
                else:
                    card_from_system = int(input("index of card from system to put in house"))
                    if len(system[card_from_system]) == 1 and player[your_card][1] + system[card_from_system][0][
                        1] == vlaue_of_house(system_deck):
                        system[system_deck].append(player.pop(your_card))
                        system[system_deck].append(system[card_from_system][0])
                        system.pop(card_from_system)
                    # check case

            elif house == 4:
                your_card = int(input("index of your card"))
                system_deck = int(input("index of house in system"))
                if 8 < (player[your_card][1] + vlaue_of_house(system_deck)) < 14:
                    system[system_deck].append(player.pop(your_card))
                elif player[your_card][1] == vlaue_of_house(system_deck):
                    system[system_deck].append(player.pop(your_card))
                else:
                    card_from_system = int(input("index of card from system to put in house"))
                    if len(system[card_from_system]) == 1 and player[your_card][1] + system[card_from_system][0][
                        1] == vlaue_of_house(system_deck):
                        system[system_deck].append(player.pop(your_card))
                        system[system_deck].append(system[card_from_system][0])
                        system.pop(card_from_system)
                    # check case
    # print(player,"\n",score_card,"\n",system)


while p1 and p2:
    players_turn(p2, p2_score)
    players_turn(p1, p1_score)
players_turn(p2, p2_score)

"""
 cases of house:
1. create pakka house
   -> throw same card as a card in system between(9,13) 
2. create kaccha house
   -> throw a card on another single card in system to make the sum between 9,13
3.contribute to pakka house
   -> throw a card of same value as of house 
               or 
   -> 1 card from player and 1 single card from system where sum is equal to value of house

4.contribute to kaccha house 
   -> add one card to kaccha house to increase its value
               or 
   -> throw your card same as house value to make it pakka house
               or 
   -> 1 card from player and 1 single card from system where sum is equal to value of house and make it pakka house
"""

# include last pickup
# include house option for first player
#include multiple deck pickup for players
#include again distribution of cards
#complete the game


# s1=0
# s2=0
#
# def count_score(score_card):
#     s=0
#     for card in score_card:
#         if card[0]=="spades":
#             s=s+card[1]
#         if card[1]==1 and card[0]!="spades":
#             s=s+1
#         if card[0]=="diamonds" and card[1]==10:
#             s=s+6
#
#     return s
# s1=count_score(p1_score)
# s2=count_score(p2_score)
# print(p1,p2,system)
# print(s1,s2)
# if s1>s2:
#     print("player 1 is winner")
# else:
#     print("player 2 is winner")
