from cProfile import label

import email 
from pydoc import text
from tkinter import *
import sqlite3
from tkinter import font
import tkinter
import hashlib
from turtle import heading
from cryptography.fernet import Fernet 
import hashlib
from tkinter import messagebox
import re



def connect():    
    frame.pack_forget()
    frame2.pack(pady=100, ipady=350, ipadx=50)

def sign():
    frame.pack_forget()
    frame3.pack(pady=200, ipady=50, ipadx=50)
   
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
#regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

window = Tk()
window.configure(bg="#4271b3")
window.title("Formulaire")

frame = Frame(window, highlightbackground="black", highlightthickness=3)
frame.configure(bg= "#606873")
frame.pack(pady=200, ipady=50,ipadx=50)

heading1 = Label(frame, text="Formulaire", font="Arial 17 underline", bg="#606873")
heading1.pack(pady=20)

btn = Button(frame, text="Inscription", command= connect,font="Arial 14", bd=0 )
btn.pack(pady=5)

btn2 = Button(frame, text="Connexion", font="Arial 14", bg="#4271b3" ,command=sign, relief=RIDGE)
btn2.pack(pady=10)

btn3 = Button(frame, text="Deconnexion", command=window.quit, font="Arial 14", bg="#4271b3" ,relief=RIDGE)
btn3.pack(pady=10)


frame2 = Frame(window, highlightbackground="black", highlightthickness=3)
frame2.configure(bg="#606873")

heading2 = Label(frame2, text="Page D'Inscription", font="Arial 17 underline", bg="#606873")
heading2.pack(pady=10)

nomlabel = Label(frame2, text="Nom", font="Arial 15", bg="#606873")
nomlabel.pack(pady=10)
nomentry = Entry(frame2)
nomentry.pack(pady=10)

prenomlabel= Label(frame2, text="Prenom", font="Arial 15", bg="#606873")
prenomlabel.pack(pady=10)
prenomentry = Entry(frame2)
prenomentry.pack(pady=10)

emaillabel= Label(frame2, text="Email", font="Arial 15", bg="#606873")
emaillabel.pack(pady=10)
emailentry = Entry(frame2)
emailentry.pack(pady=10)

mdplabel= Label(frame2, text="Mot de passe", font="Arial 15", bg="#606873")
mdplabel.pack(pady=10)
mdpentry = Entry(frame2, show="•")
mdpentry.pack(pady=10)

cmdplabel= Label(frame2, text="Confirme mot de passe ", font="Arial 15", bg="#606873")
cmdplabel.pack(pady=10)
cmdpentry = Entry(frame2,show="•")
cmdpentry.pack(pady=10)

def lite():
    conn  = sqlite3.connect("database.db")

    # I used this to encryted the password
    #key = Fernet.generate_key()
    #fernet = Fernet(key)
    #encmdp = fernet.encrypt(mdpentry.get().encode())
    hash_mdp=cmdpentry.get().encode()
    d=hashlib.sha3_256(hash_mdp)
    hachage=d.hexdigest()

    d = {
    "nom": nomentry.get(),
    "prenom": prenomentry.get(),
    "email": emailentry.get(),
    "mdp" : hachage 
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
            c.execute("SELECT email,mdp FROM informations WHERE email=:email and mdp=:mdp", d)
            donnes = c.fetchone()
            print(donnes)

            nomentry.delete(0,END)
            prenomentry.delete(0, END)
            emailentry.delete(0, END)
            mdpentry.delete(0, END)
            cmdpentry.delete(0, END)

            conn.commit()
            conn.close()

      
    else: 
        messagebox.showerror("Error", "Merci de saisir votre adresse email au format : votreexemple@exemple.com") 

        nomentry.delete(0,END)
        prenomentry.delete(0, END)
        emailentry.delete(0, END)
        mdpentry.delete(0, END)
        cmdpentry.delete(0, END)
    
    frame2.pack_forget()
    frame3.pack(pady=200, ipady=50,ipadx=50)  
    
    
    

btn = Button(frame2, text="Sumbit",command=lite , font="Roboto 16", bg="#4271b3")
btn.pack(ipadx=10, ipady=3, pady=20)

frame3 = Frame(window, highlightbackground="black", highlightthickness=3)
frame3.configure(bg="#606873")

heading3 = Label(frame3, text="Page De Connexion", font="Arial 17 underline",bg="#606873")
heading3.pack(pady=10)

usernamelabel = Label(frame3, text="Username", font="Arial 15", bg="#606873")
usernamelabel.pack(pady=10)
usernameentry = Entry(frame3)
usernameentry.pack(pady=10)

mpdlabel = Label(frame3, text="Mot de passe", font="Arial 15", bg="#606873")
mpdlabel.pack(pady=10)
mpdentry2 = Entry(frame3)
mpdentry2.pack(pady=10)

enmdp1 = mpdentry2.get().encode()
unicode1=hashlib.sha3_256(enmdp1)
vote1= unicode1.hexdigest()
print("encrypted", enmdp1)

# vote1 = unicode1.hexdigest().decode



#key = Fernet.generate_key()
#fernet = Fernet(key)
#enmdp = fernet.encrypt(mdpentry.get().encode())
hash_mdp_co=mpdentry2.get().encode()
d=hashlib.sha3_256(hash_mdp_co)
hachee=d.hexdigest()

print(hachee)
def correct():
    global vote1
    connecte = sqlite3.connect('database.db')
    
    dictornary={
    "username": usernameentry.get(), 
    "mdp": hachee
    }
    
    print(dictornary)
    c = connecte.cursor()      
    c.execute("SELECT * FROM informations WHERE email=:username AND mdp=:mdp", dictornary)
    donnes = c.fetchall()
    print(donnes)
    for i in donnes:
        if  usernameentry.get() in i and hachee in i:
            messagebox.showinfo("info", "Vous etes connecte")
            break




    connecte.commit()
    connecte.close()

btn = Button(frame3, text="Vailde", command=correct, font="Roboto 16", bg="#4271b3" )
btn.pack(ipadx=10, ipady=3, pady=20)


window.mainloop()