import csv
print("1) Add to file")
print("2) View all records")
print("3) Delete a record")
print("4) Quit program")

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

def delete():
    file = open("Salaries.csv", 'r')
    tmp = []
    for i in file:
        tmp.append(i)
    file.close()
    x = 0
    for i in tmp:
        print(x, i)
        x = x + 1
    rowdelete = int(input("Which row do you want to delete? : "))
    del tmp[rowdelete]
    file = open("Salaries.csv", 'w')
    for i in tmp:
        file.write(i)
    file.close()

tryagain = True
while tryagain:
    num = input("Enter the number of your selection : ")
    if num == '1':
        add()
    elif num == '2':
        view()
    elif num == '3':
        delete()
    elif num == '4':
        tryagain = False
    else:
        print("Invaild input")
