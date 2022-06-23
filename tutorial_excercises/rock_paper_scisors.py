
scisorsWinning1 = [3,1]
scisorsWinning2 = [1,3]
paperWinning1 = [1,2]
paperWinning2 = [2,1]
rockWinning1 = [2,3]
rockWinning2 = [3,2]
draw1 = [1,1]
draw2 = [2,2]
draw3 = [3,3]
choosenMoves = []
wonRounds1 = 0
wonRounds2 = 0
roundsNeededToWin = 3


while(True):
    if(wonRounds1 == roundsNeededToWin):
        print("Gracz pierwszy wygrywa")
        continueGameChoice1 = int(input("Czy chcesz grac ponownie? 1 - tak, 2 - nie"))
        if (continueGameChoice1 == 1):
            continue
        else:
            break
    elif(wonRounds2 == roundsNeededToWin):
        print("Gracz drugi wygrywa")
        continueGameChoice1 = int(input("Czy chcesz grac ponownie? 1 - tak, 2 - nie"))
        if (continueGameChoice1 == 1):
            continue
        else:
            break
    else:
        chooseFirstPlayer1 = int(input("Gracz1 wybiera: 1 - papier, 2 - kamień, 3 - nożyce, 4 - zakończ gre"))
        if(chooseFirstPlayer1 == 4):
            break
        chooseFirstPlayer2 = int(input("Gracz2 wybiera: 1 - papier, 2 - kamień, 3 - nożyce, 4 - zakończ gre"))
        if(chooseFirstPlayer2 == 4):
            break
        choosenMoves.append(chooseFirstPlayer1)
        choosenMoves.append(chooseFirstPlayer2)
        if(choosenMoves == scisorsWinning1):
            print("Gracz pierwszy wygrywa rundę")
            wonRounds1 += 1
            choosenMoves.clear()
        elif(choosenMoves == scisorsWinning2):
            print("Gracz drugi wygrywa rundę")
            wonRounds2 += 1
            choosenMoves.clear()
        elif(choosenMoves == paperWinning1):
            print("Gracz pierwszy wygrywa rundę")
            wonRounds1 += 1
            choosenMoves.clear()
        elif(choosenMoves == paperWinning2):
            print("Gracz drugi wygrywa rundę")
            wonRounds2 += 1
            choosenMoves.clear()
        elif(choosenMoves == rockWinning1):
            print("Gracz pierwszy wygrywa rundę")
            wonRounds1 += 1
            choosenMoves.clear()
        elif(choosenMoves == rockWinning2):
            print("Gracz drugi wygrywa rundę")
            wonRounds2 += 1
            choosenMoves.clear()
        elif(choosenMoves == draw1):
            print("Remis")
            choosenMoves.clear()
        elif(choosenMoves == draw2):
            print("Remis")
            choosenMoves.clear()
        elif(choosenMoves == draw3):
            print("Remis")
            choosenMoves.clear()
            
            
        

