def count(*number):
    sum = 0
    
    for secondaryNumber in number:
        sum = sum + secondaryNumber
    return sum

print(count(2,4,1,2,4,5, 10))
