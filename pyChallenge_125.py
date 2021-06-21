from tkinter import *
import random

r_num = random.randint(1, 6)

def click():
    message["bg"] = "black"
    message["fg"] = "yellow"
    message["text"] = r_num

window = Tk()
window.title("Roll the dice")

button = Button(text = "Roll", command = click)
button.place(x = 100, y = 20, width = 50)

label = Label(text = "Roll the dice!")
label.place(x = 20, y = 23)

message = Message(text = "")
message.place(x = 20, y = 50, width = 100, height = 25)

window.mainloop()
