import csv
import random

# file = open("Mathquiz.csv", "W")
# file = close()

file = open("Mathquiz.csv", "a")
name = input("Enter the your name : ")


def entry():
    newValue = name + ',' + "Question : " + question + ',' + "Your answer :" + str(answer) + ',' +"number of correct answers: " + str(count) + '\n'
    file.write(newValue)

count = 0
for i in range(0, 2):
    quiz_num1 = random.randint(0, 100)
    quiz_num2 = random.randint(0, 100)
    solution = quiz_num1 + quiz_num2
    question = str(quiz_num1) + ' + ' + str(quiz_num2)
    print(question)
    answer = int(input("Please enter the correct answer. : "))
    if answer == solution:
        print("Correct answer!")
        count = count + 1
        entry()
    else:
        print("Wrong answer")
        entry()
file.close()
