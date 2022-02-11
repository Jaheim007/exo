from cProfile import label
from curses import window
from pydoc import text
from tkinter import *
import sqlite3
from turtle import heading

window = Tk()

window.configure(bg="#349beb")

btn =Button(text="Connexion", )
btn.pack()

btn2 = Button(text="Inscription")
btn2.pack()



window.mainloop()