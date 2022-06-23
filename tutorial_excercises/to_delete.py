from random import randint
#from random import choice
lista = []
lista2 = []



for i in range(50):
    if i > 50:
        lista.append(randint(0,200))


def randomize(lista):
    for i in lista:
        if i >= 50:
            lista2.append(i)
        else:
            continue

