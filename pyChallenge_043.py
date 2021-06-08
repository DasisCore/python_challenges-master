direction = input('What is the wanted count direction? (up/down) : ')
if direction == 'up':
    num1 = int(input('Enter the largest number you want. : '))
    for i in range(1, num1 + 1):
        print(i)
elif direction == 'down':
    num2 = int(input('Please enter any number under 20 you want. : '))
    for o in range(20, num2 - 1, -1):
        print(o)
else:
    print("I don't understand")
