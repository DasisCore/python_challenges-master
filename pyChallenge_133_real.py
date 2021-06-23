from tkinter import *
window = Tk()
window.title("Names")
window.geometry("400x350")
window.wm_iconbitmap(r"C:\Users\jaeyoung\Desktop\snowman.ico")
logo = PhotoImage(file = r"C:\Users\jaeyoung\Desktop\temi.gif")
logolabel = Label(image = logo)
logolabel.place(x = 60, y = 20, width = 280, height = 200)
#def part-----------------------------------------------------------------------
def click():
    names = name.get()
    message = str('Hello, ' + names)
    message1["text"] = message
    # message1["bg"] = "white"
#-------------------------------------------------------------------------------
label = Label(text = "Enter your name : ")
label.place(x = 30, y = 240)
label["bg"] = "sky blue"

name = Entry("")
name.place(x = 135, y = 240, width = 205, height = 23)
name["justify"] = "center"
name.focus()

message1 = Message(text = "", width = 100)
message1.place(x = 135, y = 280, width = 205, height = 23)

button = Button(text = "Press me!", command = click)
button.place(x = 33, y = 280, width = 80, height = 23)
window.configure(background = "sky blue")

window.mainloop()
