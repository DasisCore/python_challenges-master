file = open("Names.txt", "a")
newname = input("Enter a name to add. : ")
file.write(newname + "\n")
file.close()

file = open("Names.txt", "r")
print(file.read())
file.close()
