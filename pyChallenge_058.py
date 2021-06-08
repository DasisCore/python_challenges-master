import random
score = 0
for i in range(1, 6):
    r_num1 = random.randint(1, 50)
    r_num2 = random.randint(1, 50)
    answer = r_num1 + r_num2
    print(r_num1, '+', r_num2, '= ?')
    reply = int(input('Your answer? : '))
    if reply == answer:
        print('"Well done!"\n')
        score = score + 1
    else:
        print('"Wrong answer."\n')
print('There are ', score, 'correct answers.')
