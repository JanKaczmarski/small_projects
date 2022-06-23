import random
from enum import Enum
print("""Rules:
1. Use only small letters(Do not capitalize)
""")






def chestPrizeRandom(value, howManyTimes = 1):
    i = 0
    while  howManyTimes > i:
        lowestValue = value - 0.1 * value
        highestValue = value + 0.1 * value
        print(random.randint(lowestValue, highestValue))
        i = i + 1
         
    
    















Colours = Enum("Colours", ["Green","Orange","Purple","Gold"])

chestColoursDiciotionary = {
                            Colours.Green : 0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                            }
chestColoursTuple = tuple(chestColoursDiciotionary.keys())
chestColoursPropability = tuple(chestColoursDiciotionary.values())

rewardsForChests = {
                    chestColoursTuple[reward]: (reward + 1) * (reward + 1) * 1000
                    for reward in range (len(chestColoursTuple))
                    }

chestPrizeList = ["green", "orange", "purple", "gold"]
meetingChestChanceList = ["Trafiłes skrzynke", "Nie trafiłeś na skrzynkę"]
eventPropability = [40, 60]
chestValuePropability = [75, 20, 4, 1]
i = 0
gameLenth = 5
sumGold = 0

while i < gameLenth:
    gameChoice = input("Do you want to move further? ")
    if (gameChoice == 'yes'):
        drawnEvent = random.choices(meetingChestChanceList, eventPropability)[0]
        if (drawnEvent == 'Trafiłes skrzynke'):
            print("You aproached a chest!")
            openChestChoose = input("Do you want to open the chest?")
            if (openChestChoose == 'yes'):
                drawnColour = random.choices(chestPrizeList, chestValuePropability)
                if (drawnColour[0] == 'green'):
                    randomPrizeContainer = chestPrizeRandom(1000)
                    print("You droped a GREEN chest!")
                    sumGold = sumGold + randomPrizeContainer
                elif(drawnColour[0] == 'orange'):
                    randomPrizeContainer = chestPrizeRandom(4000)
                    print("You droped an ORANGE chest!")
                    sumGold = sumGold + randomPrizeContainer
                elif(drawnColour[0] == 'purple'):
                    randomPrizeContainer = chestPrizeRandom(9000)
                    print("You droped a PURPLE chest!")
        
                    sumGold = sumGold + randomPrizeContainer
                elif(drawnColour[0] == 'gold'):
                    randomPrizeContainer = randomPrizeContainer(16000)
                    print("You droped a GOLD chest!")
                    sumGold = sumGold + randomPrizeContainer
                
            else:
                print("You missed your chance")
        else:
            print("You didn't found a chest, try your luck in the next part of the chamber.")
    else:
        print("You can only move forward guy.")
        continue
        

    i +=1
    
print("You won:", sumGold)


