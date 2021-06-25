from tkinter import *
window = Tk()
window.title("Gif checker")
window.geometry("300x400")
#def part-----------------------------------------------------------------------
def click():
    num = enter.get()
    if num == "1":
        logolabel = Label(image = gif_1)
        logolabel.place(x = 30, y = 30, width = 240, height = 240)
        label1["text"] = "1.gif was displayed."
        enter.delete(0, END)
    elif num == "2":
        logolabel = Label(image = gif_2)
        logolabel.place(x = 30, y = 30, width = 240, height = 240)
        label1["text"] = "2.gif was displayed."
        enter.delete(0, END)

    elif num == "3":
        logolabel = Label(image = gif_3)
        logolabel.place(x = 30, y = 30, width = 240, height = 240)
        label1["text"] = "3.gif was displayed."
        enter.delete(0, END)
    else:
        logolabel = Label(image = logo)
        logolabel.place(x = 30, y = 30, width = 240, height = 240)
        label1["text"] = "Invalid input."
#-------------------------------------------------------------------------------
label = Label(text = "Enter the number 1 ~ 3")
label.place(x = 30, y = 280)

label1 = Label(text = "")
label1.place(x = 30, y = 310)

enter = Entry(text = "")
enter.place(x = 170, y = 280, width = 40, height = 20)
enter["justify"] = "center"
enter.focus()

button = Button(text = "Check", command = click)
button.place(x = 220, y = 280, width = 50, height = 20)


logo = PhotoImage(file = r"C:\Users\jaeyoung\Desktop\python_challenges-master\checker.gif")
gif_1 = PhotoImage(file = r"C:\Users\jaeyoung\Desktop\python_challenges-master\1.gif")
gif_2 = PhotoImage(file = r"C:\Users\jaeyoung\Desktop\python_challenges-master\2.gif")
gif_3 = PhotoImage(file = r"C:\Users\jaeyoung\Desktop\python_challenges-master\3.gif")
logolabel = Label(image = logo)
logolabel.place(x = 30, y = 30, width = 240, height = 240)

window.mainloop()
