import random

def request_num():
    low_num = int(input('Enter the low number : '))
    high_num = int(input('Enter the high number : '))
    comp_num = random.randint(low_num, high_num)
    return comp_num

def quiznum():
    input_num = int(input("I am thinking of a number..... "))
    return input_num

def check_num(comp_num, input_num):
    tryagain = True
    while tryagain:
        if comp_num == input_num:
            print("Correct, you win!")
            tryagain = False
        elif comp_num > input_num:
            input_num = int(input("The number entered is too small. : "))
        elif comp_num < input_num:
            input_num = int(input("The number entered is too big. : "))

def main():
    comp_num = request_num()
    input_num = quiznum()
    check_num(comp_num, input_num)

main()
