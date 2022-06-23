

import time


start = time.perf_counter()
setContainer = {i for i in range(1000)}
wybor = int(input("Podaj liczbe do sprawdzenia: "))
wyborContainer = {wybor}

setContainer_Wybor = setContainer|wyborContainer


if (setContainer_Wybor == setContainer):
    print("Liczba znajduje sie w zbiorze.")
else:
    print("Liczba nie znajduje się w zbiorze")

end = start = time.perf_counter()
print(end-start)
