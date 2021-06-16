def add_name():
    add = input("Enter a name to add. : ")
    name_list.append(add)
    print(name_list , "\n")

def edit_name():
    num = 0
    for i in name_list:
        print(i,":",num)
        num = num + 1
    select = int(input("Enter the number of the person to be edited. : "))
    edit = str(input("What would you like to fix? : "))
    name_list[select] = edit
    print(name_list , "\n")

def delete_name():
    num = 0
    for i in name_list:
        print(i,":",num)
        num = num + 1
    del_name = int(input("Enter the number of the person to be deleted. : "))
    del name_list[del_name]
    print(name_list , "\n")

def show_name():
    for i in name_list:
        print(i)
    print("\n")

def end_namelist():
    print("Bye Bye~!")
    return exit()

def main():
    tryagain = True
    while tryagain:
        print("< MENU >")
        print("1) Add a name to the list.")
        print("2) Edit the name of the list.")
        print("3) Delete the name of the list.")
        print("4) Show all names in the list.")
        print("5) End the program")
        selection = input("Your Answer : ")
        if selection == '1':
            name_list = add_name()
        elif selection == '2':
            name_list = edit_name()
        elif selection == '3':
            name_list = delete_name()
        elif selection == '4':
            name_list = show_name()
        elif selection == '5':
            end_namelist()
        else:
            print("Invaild input.\n")
name_list = []
main()
