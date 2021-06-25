from tkinter import *
window = Tk()
window.title("Add the listbox")
window.geometry("320x250")
window.wm_iconbitmap(r"C:\Users\jaeyoung\Desktop\test.ico")
window.configure(background = "pink")
#def part-----------------------------------------------------------------------
def add():
    add_name = name.get()
    add_name = str(add_name)
    name.delete(0, END)
    add_gender = gender.get()
    add_gender = str(add_gender)
    in_put = add_name + ', ' + add_gender + "\n"
    listbox.insert(END, in_put)
    file = open("listbox.txt", "a")
    file.write(in_put)
    file.close()

def view():
    file = open("listbox.txt", "r")
    print(file.read())


#-------------------------------------------------------------------------------
label = Label(text = "Enter the your name ")
label.place(x = 20, y = 20)
label["bg"] = "pink"

label2 = Label(text = "Choose your gender. ")
label2.place(x = 20, y = 55)
label2["bg"] = "pink"

name = Entry()
name.place(x = 140, y = 20, width = 160, height = 18)
name["justify"] = "center"
name.focus()

gender = StringVar(window)
gender.set("Gender")
genderlist = OptionMenu(window, gender, "male", "female", "unknown")
genderlist.place(x = 140, y = 50, width = 100, height = 30)

button = Button(text = "Add", command = add)
button.place(x = 250, y = 50, width = 50, height = 30)

button2 = Button(text = "View", command = view)
button2.place(x = 140, y = 90, width = 160, height = 23)

listbox = Listbox()
listbox.place(x = 20, y = 120 , width = 280, height = 120 )
window.mainloop()
