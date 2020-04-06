from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height = 720)
miFrame.pack()

txt_email = Entry(miFrame)
txt_email.grid(row=0, column=1)

lb_email = Label(miFrame, text="Email:")
lb_email.grid(row=0, column=0)

raiz.mainloop()