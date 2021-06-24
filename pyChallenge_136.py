from tkinter import *
window = Tk()
window.title("Add the listbox")
window.geometry("320x200")
window.wm_iconbitmap(r"C:\Users\jaeyoung\Desktop\test.ico")
window.configure(background = "pink")
#def part-----------------------------------------------------------------------
def add():
    add_name = name.get()
    add_name = str(add_name)
    name.delete(0, END)
    add_gender = gender.get()
    add_gender = str(add_gender)
    in_put = add_name + ', ' + add_gender
    listbox.insert(END, in_put)

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

listbox = Listbox()
listbox.place(x = 20, y = 100 , width = 280, height = 80 )
window.mainloop()
