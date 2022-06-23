def number_multiplied_by_itself_generator():
    number = 1
    while True:
        yield number*number
        number += 1
        
generatedNumbers = []
numbers_generator = number_multiplied_by_itself_generator()
for k in range(20):
    generatedNumbers.append(next(numbers_generator))

print(generatedNumbers)

for k in range (30):
    generatedNumbers.append(next(numbers_generator))
    
    
print(generatedNumbers)

