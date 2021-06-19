from tkinter import *
window = Tk()
window.title("Sum program.")
window.geometry("400x300")

label = Label(text = "Enter the number : ")
label.place(x = 30, y =30)

enter_num = Entry(text = 0 )
enter_num.place(x = 140, y = 30, width = 50, height = 20)

def click():
    summation = enter_num.get()
    summation = int(summation)
    answer = output_box["text"]
    answer = int(answer)
    total = summation + answer
    output_box["text"] = total

def reset():
    output_box["text"] = 0
    enter_num.delete(0, END)
    enter_num.focus()

button1 = Button(text = "Add", command = click)
button1.place(x = 200, y = 30, height = 20)

button2 = Button(text = "Reset", command = reset)
button2.place(x = 240, y = 30, height = 20)

output_box = Message(text = 0)
output_box.place(x = 30 , y = 60, width = 100 , height = 30)
output_box["bg"] = "white"
output_box["fg"] = "blue"

window.mainloop()
