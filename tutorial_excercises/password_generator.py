import string
import random



choice = input("""You can choose how strog the password should be by pressing:
1. Very weak password
2. soft password
3. very strong password
""")
passwordLenght = int(input("How many letters does your password need, can't be less than 3 letters:"))



def veryWeakPassword(passwordLenght = 8):
    lowerCaseList = list(string.ascii_lowercase)
    password = ''
    for i in range(passwordLenght):
        password += random.choice(lowerCaseList)
    return password


def softPassword(passwordLenght = 8):
    upperCaseList = list(string.ascii_uppercase)
    lowerCaseList = list(string.ascii_lowercase)
    #upperCaseList.extend(lowerCaseList)
    finalSignsList = lowerCaseList + upperCaseList
    password = ''
    for i in range(passwordLenght):
        password += random.choice(finalSignsList)
    return(password)    
    


def veryStrongPassword(passwordLenght = 8):
    upperCaseList = list(string.ascii_uppercase)
    extraSigns = ["!","@","%","^","&","*"]
    lowerCaseList = list(string.ascii_lowercase)
    finalSignsList = lowerCaseList + extraSigns + upperCaseList
    password = ''
    for i in range(passwordLenght):
        password += random.choice(finalSignsList)
    return password
while(True):
    if(passwordLenght > 3 ):
        if(choice == '1'):
            print("This is your password:", veryWeakPassword(passwordLenght))
        elif(choice == '2'):
            print("This is your password:", softPassword(passwordLenght))
        elif(choice == '3'):
            print("This is your password:", veryStrongPassword(passwordLenght))
        break
    
    else:
        print("You have choosen to small number of letters, try again")
        passwordLenght = int(input())
        continue
