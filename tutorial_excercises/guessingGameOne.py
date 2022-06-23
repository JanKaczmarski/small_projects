import random
def GuessingGameOne():
    numberOfTryies = 0
    endGameChoice = '1'
    randomlyCoosenNumber = random.choice(range(10))
    while(endGameChoice == '1'):
        
        numberChoosenByPlayer = int(input("Podaj Numer od 1 do 9: "))
        if(randomlyCoosenNumber == numberChoosenByPlayer):
            randomlyCoosenNumber = random.choice(range(10))
            print("You guessed correctly.")
            numberOfTryies += 1
            print("You needed", numberOfTryies, "tryies to guess correctly.\n Type 1 to continue or 'exit' to leave")
            endGameChoice = input()
            numberOfTryies = 0
        elif(randomlyCoosenNumber > numberChoosenByPlayer):
            print("The number is too small.")
            numberOfTryies += 1
        elif(randomlyCoosenNumber < numberChoosenByPlayer):
            print("The number is too big.")
            numberOfTryies += 1
        elif(endGameChoice == 'exit'):
            break

print(GuessingGameOne())
