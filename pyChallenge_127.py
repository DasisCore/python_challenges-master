from tkinter import *

window = Tk()
window.title("Name list.")
window.geometry("400x300")

def add_name():
    name = enter.get()
    namelist.insert(END, name)
    enter.delete(0, END)
    enter.focus()

def clear():
    namelist.delete(0, END)
    enter.delete(0, END)
    enter.focus()

label = Label(text = "Enter the name : ")
label.place(x = 30, y = 30)

enter = Entry(text = 0)
enter.place(x = 128, y = 30, width = 100, height = 25)
enter["justify"] = "center"
enter.focus()

enter_button = Button(text = "Enter", command = add_name)
enter_button.place(x = 240, y = 30, width = 50, height = 25)

del_button = Button(text = "Delete", command = clear)
del_button.place(x = 300, y = 30, width = 50, height = 25)

namelist = Listbox()
namelist.place(x = 30, y = 60, width = 200, height = 200)

window.mainloop()
