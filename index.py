#Added all my imports from tkinter.
from tkinter import messagebox
from cryptography.fernet import Fernet
from cProfile import label
from pydoc import text
from tkinter import *
import sqlite3
from turtle import heading
import re

"""Created The Inscription page And added a simple database but
I still have to encrypt the password"""

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

inscription = Tk()
inscription.configure(bg="#349beb")
inscription.attributes('-alpha', 0.9)

#Created the First Window Frame Which is the main Principle Frame
frame = Frame(inscription, highlightthickness=5, highlightbackground="black")
frame.pack(side=TOP, expand=YES, ipadx=50, ipady=50)
frame.configure(bg="grey")
heading = Label(frame, text= "Inscription", font="Helvetica 22 underline", fg="white", bg="grey",  )
heading.pack(pady=35)

#Created the Last Name Label and input.
NomLabel = Label(frame, text= "Nom", font="Roboto 15", fg="white", bg="grey")
NomLabel.pack(pady=15)
Nom_entry = Entry(frame)
Nom_entry.pack(ipadx=15, ipady=3)


#Created the First Name Label and input.
PrenomLabel= Label(frame, text= "Prenom", font="Roboto 15", bg="grey", fg="white")
PrenomLabel.pack(pady=15)
Prenom_entry = Entry(frame)
Prenom_entry.pack(ipadx=15, ipady=3)


#Created the Email Label and input.
EmailLabel = Label(frame, text= "Email", font="Roboto 15", fg="white", bg="grey")
EmailLabel.pack(pady=15)
Email_entry = Entry(frame)
Email_entry.pack(ipadx=15, ipady=3)


#Created the password Label and input.
mdpLabel= Label(frame, text= "Mot de passe ", font="Roboto 15", fg="white", bg="grey")
mdpLabel.pack(pady=15)
mdp_entry = Entry(frame, show="•")
mdp_entry.pack(ipadx=15, ipady=3)


#Created the confrim password Label and input.
cmdpLabel= Label(frame, text= "Confirme mot de passe ", font="Roboto 15", fg="white", bg="grey")
cmdpLabel.pack(pady=15)
cmdp_entry = Entry(frame, show="•")
cmdp_entry.pack(ipadx=15, ipady=3)


"""Created a file named "database.db" using the sqlite database method 
and I was able to add all elements within the table all that is leftf is to add an encryption
to the password and the confirm password.
"""

def lite():
    
    conn  = sqlite3.connect("database.db")
    
    # I used this to encryted the password
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encmdp = fernet.encrypt(mdp_entry.get().encode())
    
    d = {
    "nom": Nom_entry.get(),
    "prenom": Prenom_entry.get(),
    "email": Email_entry.get(),
    "mdp" : encmdp 
    }
    
    if Nom_entry.get() == "" or Prenom_entry.get()== "" or Email_entry.get() =="" or mdp_entry.get()=="":    
        messagebox.showerror("Error", " Veuillez saisir les champs ") 
        
        Nom_entry.delete(0,END)
        Prenom_entry.delete(0, END)
        Email_entry.delete(0, END)
        mdp_entry.delete(0, END)
        cmdp_entry.delete(0, END)
            
    
    elif Nom_entry.get().isspace() == "" and Prenom_entry.get().isspace() == "": 
        messagebox.showerror("Error", " Veuillez saisir les champs ") 
        
        Nom_entry.delete(0,END)
        Prenom_entry.delete(0, END)
        Email_entry.delete(0, END)
        mdp_entry.delete(0, END)
        cmdp_entry.delete(0, END)
             
        
    elif cmdp_entry.get() != mdp_entry.get():   
        messagebox.showerror(" Error ", " Les mots de passe ne correspondent pas et  ")
        
        Nom_entry.delete(0,END)
        Prenom_entry.delete(0, END)
        Email_entry.delete(0, END)
        mdp_entry.delete(0, END)
        cmdp_entry.delete(0, END)
            
         
    elif Email_entry.get():
        if(re.fullmatch(regex, Email_entry.get())):
            messagebox.showinfo("Info", "Vous êtes inscrit ") 
         
            c = conn.cursor()
            c.execute(""" CREATE TABLE IF NOT EXISTS informations (   
                    nom text,
                    prenom text,
                    email text, 
                    mdp text
                )""")
        
            c.execute("INSERT INTO informations VALUES(:nom, :prenom, :email, :mdp)", d)

            Nom_entry.delete(0,END)
            Prenom_entry.delete(0, END)
            Email_entry.delete(0, END)
            mdp_entry.delete(0, END)
            cmdp_entry.delete(0, END)
            
            conn.commit()
            conn.close()

        else: 
            messagebox.showerror("Error", "Merci de saisir votre adresse email au format : votreexemple@exemple.com") 
            
            Nom_entry.delete(0,END)
            Prenom_entry.delete(0, END)
            Email_entry.delete(0, END)
            mdp_entry.delete(0, END)
            cmdp_entry.delete(0, END)
            

btn = Button(frame, text="",command=lite , font="Roboto 16")
btn.pack(ipadx=10, ipady=3, pady=20)

inscription.mainloop()

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
    
    # if Username not in 

    btn = Button(frame, text="Sumbit", font="Roboto 16")
    btn.pack(ipadx=10, ipady=3, pady=20)
    
    
    connexion.mainloop()
