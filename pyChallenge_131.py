from tkinter import *
import csv
window = Tk()
window.title("Age")
window.geometry("300x100")

def click():
    file = open("Personal information.csv", "a")
    name = namebox.get()
    age = agebox.get()
    record = name + ',' + age + "\n"
    file.write(str(record))
    namebox.delete(0, END)
    agebox.delete(0, END)
    namebox.focus()

label1 = Label(text = "Name")
label1.place(x = 30, y = 20)

namebox = Entry()
namebox.place(x = 30, y = 40, width = 100, height = 25)
namebox["justify"] = "center"
namebox.focus()

label2 = Label(text = "Age")
label2.place(x = 160, y = 20)

agebox = Entry()
agebox.place(x = 160, y = 40, width = 50, height = 25)
agebox["justify"] = "center"

button = Button(text = "Save", command = click)
button.place(x = 220, y = 40, width = 50, height = 25)


window.mainloop()
