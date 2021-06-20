from tkinter import *
window = Tk()
window.title("Enter the name. <^오^>")
window.geometry("400x200")

def click():
    name = names_box.get()
    name_list.insert(END, name)


label1 = Label(text = "Enter the your name : ")
label1.place(x = 0, y = 20, width = 200, height = 20)

name_box = Entry(text = "")
names_box.place(x = 160, y = 20, width = 80, height = 20)

button = Button(text = "Enter")#,  command = )
button.place(x = 250, y = 20, width = 50, height = 20)

namelist = Message(text = "")
namelist.place(x = 35, y = 40)

window.mainloop()
