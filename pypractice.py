from tkinter import *

window = Tk()
window.title("What's your name?")
window.geometry("500x250")

def click():
    name = entry_box.get()
    hi_name = Label(text = "Hello!" + name)
    hi_name.place(x = 100, y = 100, width = 100, height = 20)
    hi_name["bg"] = "black"
    hi_name["fg"] = "white"

request = Label(text = "Enter the your name : ")
request.place(x = 50, y= 50)

button1 = Button(text = "Press me!", command = click)
button1.place(x = 300, y = 50, width = 100, height = 20)

entry_box = Entry(text = "")
entry_box.place(x = 175, y = 50, width = 120, height = 20)
entry_box["justify"] = "center"
entry_box.focus()
window.mainloop()
