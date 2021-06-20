from tkinter import *
window = Tk()
window.title("Hello, world!")
window.geometry("300x250")

def click():
    name = textbox1.get()
    message = str("Hello, " + name)
    textbox2["bg"] = "black"
    textbox2["fg"] = "white"
    textbox2["text"] = message

label = Label(text = "Enter the your name !")
label.place(x = 90, y = 70)

textbox1 = Entry(text = "")
textbox1.place(x = 90, y = 100, width = 120, height = 20)
textbox1["justify"] = "center"
textbox1.focus()

textbox2 = Message(text = "", width = 120)
textbox2.place(x = 90, y = 170, width = 120, height = 20)

button = Button(text = "Press me!", command = click)
button.place(x = 100, y = 130, width = 100, height = 30)

window.mainloop()
