import random
r_num = random.randint(1, 10)
answer = False
while answer == False:
    a_num = int(input('"Enter the number 1 between 10" : '))
    if r_num > a_num:
        print('"Too low, Enter the number again."\n')
    elif r_num < a_num:
        print('"Too high, Enter the number again."\n')
    else:
        print('"Well done"')
        answer = True
