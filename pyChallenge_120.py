import random

def enter_1():
    r1_num = random.randint(5, 20)
    r2_num = random.randint(5, 20)
    quiz = r1_num + r2_num
    print(r1_num, " + ", r2_num)
    answer = int(input("Enter the answer : "))
    print("Your answer is ",answer, ", Real answer is ", quiz)
    answers = (quiz, answer)
    return answers

def enter_2():
    r1_num = random.randint(25, 50)
    r2_num = random.randint(1, 25)
    quiz = r1_num - r2_num
    print(r1_num, " - ", r2_num)
    answer = int(input("Enter the answer : "))
    print("Your answer is ",answer, ", Real answer is ", quiz)
    answers = (quiz, answer)
    return answers

def confirm(quiz, answer):
    if quiz == answer:
        print("'Correct'")
    else:
        print("'Incorrect, the answer is ", quiz, "'")

def main():
    choice = int(input("1) Addition\n2) Subtraction\nEnter 1 or 2 : "))
    if choice == 1:
        quiz, answer = enter_1()
        confirm(quiz, answer)
    elif choice == 2:
        quiz, answer = enter_2()
        confirm(quiz, answer)
    else:
        print("Invaild input")

main()
