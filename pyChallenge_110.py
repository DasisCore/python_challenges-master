file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
names = input("Enter the number to be deleted. : ")
names = names + "\n"
for row in file:
    if row != names:
        file = open("Names2.txt", "a")
        newname = row
        file.write(newname)
        file.close()
file.close()
