from tkinter import messagebox
from cryptography.fernet import Fernet
from cProfile import label
from pydoc import text
from tkinter import *
import sqlite3
from turtle import heading
import re
from tkinter import *
def toggle():
    if label.winfo_ismapped():
        button['text']='unmap'
        label.pack_forget()
    else:
        button['text']='map'
        label.pack()

root = Tk()

button = Button(text="Push me", command=toggle)
button.pack()

label = Label(text="Helo")
label.pack()

root.wait_window()