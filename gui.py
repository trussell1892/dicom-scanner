from tkinter import *

window = Tk()

window.title("Scan DICOMs tool")

btn = Button(text = "Scan DICOMs")
btn.grid(column=1, row=1)

window.geometry("350x250")
window.mainloop()
