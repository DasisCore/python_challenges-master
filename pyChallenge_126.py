from tkinter import *
window = Tk()
window.title("Enter the number!")
window.geometry("400x200")

def click():
    num = enter.get()
    num = int(num)
    nums = result["text"]
    nums = int(nums)
    answer = num + nums
    result["text"] = answer

def delete():
    result["text"] = 0
    enter.delete(0, END)
    enter["justify"] = "center"
    enter.focus()

label = Label(text = "Enter the number : ")
label.place(x = 30, y = 32)

enter = Entry(text = "")
enter.place(x = 140, y = 30, width = 50, height = 25)
enter["justify"] = "center"
enter.focus()

button = Button(text = "Enter" , command = click )
button.place(x = 200, y = 30, width = 50, height = 25)

reset_button = Button(text = "Reset", command = delete)
reset_button.place(x = 260, y = 30, width = 50, height = 25)

result = Message(text = 0, width = 300)
result.place(x = 30 , y = 60)

window.mainloop()
