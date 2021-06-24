from tkinter import *
import random

ran_num1 = random.randint(10, 50)
ran_num2 = random.randint(10, 50)

window = Tk()
window.title("Number Quiz")
window.geometry("400x350")
window.wm_iconbitmap(r"C:\Users\jaeyoung\Desktop\snowman.ico")
label = Label(text = "Guess the problem!")
label.place(x = 30, y = 20)
#def part-----------------------------------------------------------------------
def submission():
    num1 = variable1["text"]
    num1 = int(num1)
    num2 = variable2["text"]
    num2 = int(num2)
    y_answer = answer.get()
    y_answer = int(y_answer)
    q_answer = num1 + num2
    if q_answer == y_answer:
        f_temi = Label(image = win)
        f_temi.place(x = 80, y = 80)
    else:
        f_temi = Label(image = lose)
        f_temi.place(x = 80, y = 80)
        submission()

def next():
    answer.delete(0, END)
    num1 = random.randint(10, 50)
    num2 = random.randint(10, 50)
    variable1["text"] = num1
    variable2["text"] = num2
    f_temi = Label(image = logo)
    f_temi.place(x = 80, y = 80)
#-------------------------------------------------------------------------------
win = PhotoImage(file = r"C:\Users\jaeyoung\Desktop\goodanswer.gif")
lose = PhotoImage(file = r"C:\Users\jaeyoung\Desktop\notanswer.gif")
logo = PhotoImage(file = r"C:\Users\jaeyoung\Desktop\temi.gif")
f_temi = Label(image = logo)
f_temi.place(x = 80, y = 80)#, width = 250, height = 250)

variable1 = Label(text = ran_num1)
variable1.place(x = 30, y = 50)
add = Label(text = "+")
add.place(x = 58, y = 50)
variable2 = Label(text = ran_num2)
variable2.place(x = 80, y = 50)
is1 = Label(text = "=")
is1.place(x = 105, y = 50)

answer = Entry(text = "")
answer.place(x = 130, y = 50, width = 60, height = 20)
answer["justify"] = "center"
answer.focus()

submission = Button(text = "Submission", command = submission)
submission.place(x = 200, y = 50, width = 100, height = 20)

next = Button(text = "Next", command = next)
next.place(x = 310, y = 50, width = 50, height = 20)

window.mainloop()
