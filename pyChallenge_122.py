import csv
print("1) Add to file")
print("2) View all records")
print("3) Quit program")

def add():
    file = open("Salaries.csv", "a")
    name = input("What is your name? : ")
    salary = int(input("What is your salary? : "))
    newValue = name + "," + str(salary) + '\n'
    file.write(str(newValue))
    file.close()

def view():
    file = open("Salaries.csv", "r")
    for i in file:
        print(i)
    file.close()

tryagain = True
while tryagain:
    num = input("Enter the number of your selection : ")
    if num == '1':
        add()
    elif num == '2':
        view()
    elif num == '3':
        tryagain = False
    else:
        print("Invaild input")
