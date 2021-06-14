menu = input("1) Create a new file\n2) Display the file\n3) Add a new item to the file\n Make a selection 1, 2, or 3 : ")
if menu == "1":
    subject = input("Please enter the subject name. :")
    file = open("Subject.txt", "w")
    file.write(subject + "\n")
    file.close()
elif menu == "2":
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
elif menu == "3":
    file = open("Subject.txt", "a")
    add_subject = input("Enter the subject name to be added. : ")
    file.write(add_subject + "\n")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
else:
    print('Invaild input')
