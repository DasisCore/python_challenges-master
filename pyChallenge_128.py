from tkinter import *
window = Tk()
window.title("Kilometers to miles converter")
window.geometry("400x180")

label0 = Label(text = "Kilometers to miles converter!")
label0.place(x = 25, y = 18)
label0.configure(font=("Courier", 15, "roman"))
#def part-----------------------------------------------------------------------
def km_to_mi():
    answer1 = km.get()
    answer1 = float(answer1)
    result1 = answer1 * 0.621
    answer_mi["text"] = result1
    km.delete(0, END)

def mi_to_km():
    answer2 = mi.get()
    answer2 = int(answer2)
    result2 = answer2 * 1.609
    answer_km["text"] = result2
    mi.delete(0, END)

#-------------------------------------------------------------------------------
labelkm = Label(text = " Km                       mi ")
labelkm.place(x = 60, y = 50)

km = Entry()
km.place(x = 30, y = 75, width = 90, height = 20)
km["justify"] = "center"
km.focus()

button1 = Button(text = "Conversion", command = km_to_mi)
button1.place(x = 250, y = 75, width = 70, height = 22)

answer_mi = Message(text = 0)
answer_mi.place(x = 138, y = 75, width = 90, height = 22)
#-------------------------------------------------------------------------------
labelmi = Label(text = " mi                       Km  ")
labelmi.place(x = 60, y = 105)

mi = Entry()
mi.place(x = 30, y = 130, width = 90, height = 20)
mi["justify"] = "center"

button2 = Button(text = "Conversion", command = mi_to_km)
button2.place(x = 250, y = 130, width = 70, height = 22)

answer_km = Message(text = 0)
answer_km.place(x = 138, y = 130, width = 90, height = 22)

window.mainloop()
