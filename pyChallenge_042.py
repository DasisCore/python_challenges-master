total = 0
num = int(input('Enter the number : '))
for i in range(0, 5):
    choice = input("Do you want this number included? y/n : ")
    if choice == "y":
        total = total + num
print(total)
