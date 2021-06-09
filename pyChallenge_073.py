food = {}
food[1] = input('Enter your first favorite food. : ')
food[2] = input('Enter your second favorite food. : ')
food[3] = input('Enter your third favorite food. : ')
food[4] = input('Enter your fourth favorite food. : ')
print(food)
num = int(input('Got a number you want to remove? : '))
del food[num]
print(sorted(food.values()))
