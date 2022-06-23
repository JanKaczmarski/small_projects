def calc_year(a, p:float, n:int):
    return round(a * (1+p/100)**n, 2)

def calc_month(a:int, p:float, n:int, m:int, years:float):
    return round(a * (1+p/m/100)**n, 2)

wynik = 0
for i in range(1,11):
    wynik += 200 * 1.05**i
print(wynik)