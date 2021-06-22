from tkinter import *
window = Tk()
window.title("Number")
window.geometry("400x310")
#def part-----------------------------------------------------------------------
def add():
    num = number.get()
    if num.isdigit() == True:
        integer.insert(END, num)
        number.delete(0, END)
        number.focus()
    else:
        number.delete(0, END)
        number.focus()

def delete():
    integer.delete(0)
    number.delete(0, END)
    number.focus()
#-------------------------------------------------------------------------------
label = Label(text = "Enter the number : ")
label.place(x = 30, y = 30)

label1 = Label(text = "[It is added only if it is an integer.]")
label1.place(x = 160, y = 60)

number = Entry(text = 0)
number.place(x = 140, y = 30, width = 100, height = 22)
number["justify"] = "center"
number.focus()

add_button = Button(text = "Add", command = add)
add_button.place(x = 250, y = 30, width = 50, height = 22)

del_button = Button(text = "Delete", command = delete)
del_button.place(x = 310, y = 30, width = 50, height = 22)

integer = Listbox()
integer.place(x = 30, y = 90, width = 330, height = 200)

window.mainloop()
