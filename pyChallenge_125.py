from tkinter import *
import random
window = Tk()
window.title("Dice program.")
window.geometry("500x250")

r_num = random.randint(1, 6)

label = Label(text = "Dice eye")
label.place(x = 50, y = 20)

def eye():
    eye_display = Label(text = r_num)
    eye_display.place(x = 120, y = 20,  width = 30, height = 20)
    eye_display["bg"] = "black"
    eye_display["fg"] = "white"

button = Button(text = "roll the dice", command = eye )
button.place(x = 50, y = 50, width = 100, height = 30)

window.mainloop()
