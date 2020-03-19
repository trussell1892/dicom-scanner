from tkinter import *

window = Tk()

window.title("Scan DICOMs tool")

btn = Button(window, text = "Scan DICOMs")
btn.grid(column=1, row=1)

lbl = Label(window, text="Patient Name:")
lbl.grid(column=1, row=2)

txt = Entry(window, width = 25)
txt.grid(column=2, row=2)

window.geometry("350x250")
window.mainloop()
