from cProfile import label
import email
from pydoc import text
from tkinter import *
import sqlite3
from tkinter import font
import tkinter
from turtle import heading
from cryptography.fernet import Fernet 
from tkinter import messagebox
import re

def connect():    
    frame.pack_forget()
    frame2.pack(pady=100, ipady=350, ipadx=50)

def sign():
    frame.pack_forget()
    frame3.pack(pady=200, ipady=50, ipadx=50)
   
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

window = Tk()
window.configure(bg="#4271b3")
window.title("Formulaire")

frame = Frame(window, highlightbackground="black", highlightthickness=3)
frame.configure(bg= "#606873")
frame.pack(pady=200, ipady=50,ipadx=50)

heading1 = Label(frame, text="Formulaire", font="Arial 17 underline",fg="white" ,bg="#606873")
heading1.pack(pady=20)

btn = Button(frame, text="Connexion", command= connect,font="Arial 14" , fg="white",bg="#4271b3" ,relief=RIDGE)
btn.pack(pady=5)

btn2 = Button(frame, text="Inscription", font="Arial 14",fg="white",bg="#4271b3",command=sign, relief=RIDGE)
btn2.pack(pady=10)

btn3 = Button(frame, text="Deconnexion", command=window.quit, font="Arial 14",fg="white", bg="#4271b3" ,relief=RIDGE)
btn3.pack(pady=10)


frame2 = Frame(window, highlightbackground="black", highlightthickness=3)
frame2.configure(bg="#606873")

heading2 = Label(frame2, text="Page D'Inscription", font="Arial 17 underline",fg="white" ,bg="#606873")
heading2.pack(pady=10)

nomlabel = Label(frame2, text="Nom", font="Arial 15", fg="white" , bg="#606873")
nomlabel.pack(pady=10)
nomentry = Entry(frame2)
nomentry.pack(pady=10)

prenomlabel= Label(frame2, text="Prenom", font="Arial 15", fg="white", bg="#606873")
prenomlabel.pack(pady=10)
prenomentry = Entry(frame2)
prenomentry.pack(pady=10)

emaillabel= Label(frame2, text="Email", font="Arial 15", fg="white", bg="#606873")
emaillabel.pack(pady=10)
emailentry = Entry(frame2)
emailentry.pack(pady=10)

mdplabel= Label(frame2, text="Mot de passe", font="Arial 15", fg="white", bg="#606873")
mdplabel.pack(pady=10)
mdpentry = Entry(frame2, show="•")
mdpentry.pack(pady=10)

cmdplabel= Label(frame2, text="Confirme mot de passe ", font="Arial 15", fg="white", bg="#606873")
cmdplabel.pack(pady=10)
cmdpentry = Entry(frame2,show="•")
cmdpentry.pack(pady=10)

def lite():
    
    conn  = sqlite3.connect("database.db")

    # I used this to encryted the password
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encmdp = fernet.encrypt(mdpentry.get().encode())

    d = {
    "nom": nomentry.get(),
    "prenom": prenomentry.get(),
    "email": emailentry.get(),
    "mdp" : encmdp 
    }

    if nomentry.get() == "" or prenomentry.get()== "" or emailentry.get() =="" or mdpentry.get()=="":    
        messagebox.showerror("Error", " Veuillez saisir les champs ") 

        nomentry.delete(0,END)
        prenomentry.delete(0, END)
        emailentry.delete(0, END)
        mdpentry.delete(0, END)
        cmdpentry.delete(0, END)


    elif nomentry.get().isspace() == "" and prenomentry.get().isspace() == "": 
        messagebox.showerror("Error", " Veuillez saisir les champs ") 

        nomentry.delete(0,END)
        prenomentry.delete(0, END)
        emailentry.delete(0, END)
        mdpentry.delete(0, END)
        cmdpentry.delete(0, END)
        

    elif cmdpentry.get() != mdpentry.get():   
        messagebox.showerror(" Error ", " Les mots de passe ne correspondent pas et  ")

        nomentry.delete(0,END)
        prenomentry.delete(0, END)
        emailentry.delete(0, END)
        mdpentry.delete(0, END)
        cmdpentry.delete(0, END)

    elif emailentry.get():
        if(re.fullmatch(regex, emailentry.get())):
            messagebox.showinfo("Info", "Vous êtes inscrit ") 

            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS informations (   
                    nom text,
                    prenom text,
                    email text, 
                    mdp text
                )""")

            c.execute("INSERT INTO informations VALUES(:nom, :prenom, :email, :mdp)", d)

            nomentry.delete(0,END)
            prenomentry.delete(0, END)
            emailentry.delete(0, END)
            mdpentry.delete(0, END)
            cmdpentry.delete(0, END)

            conn.commit()
            conn.close()

        frame2.pack_forget()
        frame.pack(pady=200, ipady=50,ipadx=50)
    
    else: 
        messagebox.showerror("Error", "Merci de saisir votre adresse email au format : votreexemple@exemple.com") 

        nomentry.delete(0,END)
        prenomentry.delete(0, END)
        emailentry.delete(0, END)
        mdpentry.delete(0, END)
        cmdpentry.delete(0, END)

    

btn = Button(frame2, text="Sumbit",command=lite , font="Roboto 16", bg="#4271b3" , fg="white")
btn.pack(ipadx=10, ipady=3, pady=20)

frame3 = Frame(window, highlightbackground="black", highlightthickness=3)
frame3.configure(bg="#606873")

heading3 = Label(frame3, text="Page De Connexion", font="Arial 17 underline",fg="white" ,bg="#606873")
heading3.pack(pady=10)

usernamelabel = Label(frame3, text="Username", font="Arial 15", fg="white" , bg="#606873")
usernamelabel.pack(pady=10)
usernameentry = Entry(frame3)
usernameentry.pack(pady=10)

mpdlabel = Label(frame3, text="Mot de passe", font="Arial 15", fg="white" , bg="#606873")
mpdlabel.pack(pady=10)
mpdentry = Entry(frame3)
mpdentry.pack(pady=10)



btn = Button(frame3, text="Vailde", font="Roboto 16", bg="#4271b3" , fg="white")
btn.pack(ipadx=10, ipady=3, pady=20)


window.mainloop()