from tkinter import *
window = Tk()
window.title("Remind")
window.geometry("300x200")
window.configure(background = "pink")
# window.wm_iconbitmap(r"‪C:\Users\jaeyoung\Desktop\snack.ico")
logo = PhotoImage(file = ".\snack.gif")
imagelabel = Label(image = logo)
imagelabel.place(x = 30, y = 20, width = 150, height =200)

window.mainloop()
