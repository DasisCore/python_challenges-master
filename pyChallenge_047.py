answer = 'y'
num1 = int(input('Enter a fitst number : '))
total = num1
while answer == "y":
    num2 = int(input('Enter a another number : '))
    total = num2 + total
    answer = input('Do you want to add another number? (y/n) : ')
print('The total is', total)
