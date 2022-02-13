from cProfile import label
from curses import window
from pydoc import text
from tkinter import *
import sqlite3
from turtle import heading

def connect():    
    frame.place_forget()
    frame2.pack(pady=10)

window = Tk()
window.configure(bg="#349beb")

frame = Frame(window, highlightbackground="black", highlightthickness=3)
frame.place(x=100, y=100)

btn = Button(frame, text="Connexion", command= connect)
btn.pack()

btn2 = Button(frame, text="Inscription")
btn2.pack()

frame2 = Frame(window, highlightbackground="black", highlightthickness=3)

noml = Label(frame2,text="NOM").pack()
nome = Entry(frame2).pack()

last1= Label(frame2, text="Last").pack()
last3 = Entry(frame2).pack()

btn = Button(frame2, text="Connect").pack()


window.mainloop()