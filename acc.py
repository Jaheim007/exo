from cProfile import label
from pydoc import text
from tkinter import *
import sqlite3
from turtle import heading

def connect():            
    connexion = Tk()
    connexion.geometry("700x700")
    connexion.resizable(FALSE, FALSE)
    connexion.configure(bg="#349beb")
    connexion.attributes('-alpha', 0.9)

    frame = Frame(connexion, highlightthickness=3, highlightbackground="black")
    frame.pack(side=TOP, expand=YES, ipadx=50, ipady=50)
    frame.configure(bg="grey")

    Username = Label(frame, text= "Username", font="Roboto 20", fg="white", bg="grey")
    Username.pack(pady=15)
    Username_entry = Entry(frame)
    Username_entry.pack(ipadx=15, ipady=3)

    mdp = Label(frame, text= "Mot De Passe", font="Roboto 20", bg="grey", fg="white")
    mdp.pack(pady=15)
    mdp_entry = Entry(frame)
    mdp_entry.pack(ipadx=15, ipady=3)

    btn = Button(frame, text="Sumbit", font="Roboto 16")
    btn.pack(ipadx=10, ipady=3, pady=20)
    
    connexion.mainloop()
