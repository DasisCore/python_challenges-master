from tkinter import *
import csv

window = Tk()
window.title("Personal information")
window.geometry("400x310")
#def part-----------------------------------------------------------------------
def add():
    nam = name.get()
    ag = age.get()
    plus = str(nam), ",", int(ag)
    pi_list.insert(END, plus)
    name.delete(0, END)
    age.delete(0, END)
    name.focus()

def delete():
    pi_list.delete(0)
    name.delete(0, END)
    age.delete(0, END)
    name.focus()

def save():  #여기 수정해야 함!
    file = open("Personal information.csv" , "w")
    tmp = []
    tmp = pi_list.get(0, END)
    for i in tmp:
        record = str(i) + "\n"
        file.write(str(record))
    file.close()

#-------------------------------------------------------------------------------
label = Label(text = "Please enter your name and age. ")
label.place(x = 30, y = 30)

label1 = Label(text = "Name")
label1.place(x = 30, y = 60)

name = Entry(text = "")
name.place(x = 70, y = 60, width = 90, height = 22)
name["justify"] = "center"
name.focus()

label2 = Label(text = "Age")
label2.place(x = 170, y = 60)

age = Entry(text = "")
age.place(x = 200, y = 60, width = 30, height = 22)
age["justify"] = "center"

add_button = Button(text = "Add", command = add)
add_button.place(x = 250, y = 30, width = 50, height = 22)

del_button = Button(text = "Delete", command = delete)
del_button.place(x = 310, y = 30, width = 50, height = 22)

csv_button = Button(text = "Save the csv file", command = save)
csv_button.place(x = 250, y = 60, width = 110, height = 22)

pi_list = Listbox()
pi_list.place(x = 30, y = 90, width = 330, height = 200)

window.mainloop()
