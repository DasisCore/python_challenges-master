from tkinter import *
import csv
window = Tk()
window.title("Age")
window.geometry("350x300")

def click():
    file = open("Personal information.csv", "a")
    name = namebox.get()
    age = agebox.get()
    record = name + ',' + age + "\n"
    file.write(str(record))
    namebox.delete(0, END)
    agebox.delete(0, END)
    namebox.focus()

def load():
    file = open("Personal information.csv", "r")
    reader = csv.reader(file)
    tmp = []
    for i in file:
        tmp.append(i)
    for data in tmp:
        pi_list.insert(END, data)

def clear():
    pi_list.delete(0, END)

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

button1 = Button(text = "Save", command = click)
button1.place(x = 220, y = 40, width = 50, height = 25)

button2 = Button(text = "Load", command = load)
button2.place(x = 280, y = 40, width = 50, height = 25)

button3 = Button(text = "Clear", command = clear)
button3.place(x = 220, y = 10, width = 110, height = 20)

pi_list = Listbox()
pi_list.place(x = 30, y = 70, width = 300, height = 200)


window.mainloop()
