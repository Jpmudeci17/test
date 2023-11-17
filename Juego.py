
import time
from tkinter import *
from tkinter import ttk

palabras = open("Palabras.txt")
pa1 = palabras.readlines(1)
pa2 = palabras.readlines(1)
pa1 = pa1[0].split(',')
pa2 = pa2[0].split(',')

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("juego")
root.resizable(0,0)
root.geometry("520x480")
for linea in pa1:
    ttk.Label(frm, text = linea).grid(column=1, row=0)
    root.mainloop()
    time.sleep(1)
    root.destroy()
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)