from tkinter import *
window = Tk()
window.title("Change the color!")
window.geometry("290x100")
window.wm_iconbitmap(r"C:\Users\jaeyoung\Desktop\test.ico")
window.configure(background = "sky blue")
#def part-----------------------------------------------------------------------
def click():
    color = selectlist.get()
    window.configure(background = color)
#-------------------------------------------------------------------------------

selectlist = StringVar(window)
selectlist.set("Select List")
colorlist = OptionMenu(window, selectlist, "sky blue" , "pink" , "yellow", "red", "white")
colorlist.place(x = 30, y = 30)

button = Button(text = "Click me!", command = click)
button.place(x = 150, y = 30, width = 100, height = 30)
window.mainloop()
