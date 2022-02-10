from cProfile import label
from pydoc import text
from tkinter import *
import sqlite3
from turtle import heading

inscription = Tk()
inscription.configure(bg="#349beb")
inscription.attributes('-alpha', 0.9)

frame = Frame(inscription, highlightthickness=3, highlightbackground="black")
frame.pack(side=TOP, expand=YES, ipadx=50, ipady=50)
frame.configure(bg="grey")
heading = Label(frame, text= "Inscription", font="Helvetica 22 underline", fg="white", bg="grey",  )
heading.pack(pady=35)

NomLabel = Label(frame, text= "Nom", font="Roboto 15", fg="white", bg="grey")
NomLabel.pack(pady=15)
Nom_entry = Entry(frame)
Nom_entry.pack(ipadx=15, ipady=3)
nom = Nom_entry.get()

PrenomLabel= Label(frame, text= "Prenom", font="Roboto 15", bg="grey", fg="white")
PrenomLabel.pack(pady=15)
Prenom_entry = Entry(frame)
Prenom_entry.pack(ipadx=15, ipady=3)
prenom = Prenom_entry.get()

EmailLabel = Label(frame, text= "Email", font="Roboto 15", fg="white", bg="grey")
EmailLabel.pack(pady=15)
Email_entry = Entry(frame)
Email_entry.pack(ipadx=15, ipady=3)
email = Email_entry.get()

mdpLabel= Label(frame, text= "Mot de passe ", font="Roboto 15", fg="white", bg="grey")
mdpLabel.pack(pady=15)
mdp_entry = Entry(frame, show="•")
mdp_entry.pack(ipadx=15, ipady=3)
mdp = mdp_entry.get()

cmdpLabel= Label(frame, text= "Confirme mot de passe ", font="Roboto 15", fg="white", bg="grey")
cmdpLabel.pack(pady=15)
cmdp_entry = Entry(frame, show="•")
cmdp_entry.pack(ipadx=15, ipady=3)
cmdp = cmdp_entry.get()

def lite():
    conn  = sqlite3.connect("database.db")
    
    d = {
    "nom": Nom_entry.get(),
    "prenom": Prenom_entry.get(),
    "email": Email_entry.get(),
    "mdp" : mdp_entry.get(),
    "cmdp" : cmdp_entry.get()
    }
    
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS informations(   
            nom text,
            prenom text,
            email text, 
            mdp text, 
            confirm text 
        )""")
   


    c.execute("INSERT INTO informations VALUES(:nom, :prenom, :email, :mdp, :cmdp)", d)

    Nom_entry.delete(0,END)
    Prenom_entry.delete(0, END)
    Email_entry.delete(0, END)
    mdp_entry.delete(0, END)
    cmdp_entry.delete(0, END)
    
    conn.commit()
    conn.close()

btn = Button(frame, text="Sumbit",command=lite ,  font="Roboto 16")
btn.pack(ipadx=10, ipady=3, pady=20)


inscription.mainloop()
