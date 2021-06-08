import random
num1 = random.randint(1, 10)
answer = False
while answer == False:
    num2 = int(input('"Enter the number 1 between 10" : '))
    if num1 == num2:
        answer = True
