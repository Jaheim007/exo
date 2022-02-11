import sqlite3
import rsa
import tkinter
from tkinter import messagebox

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def display_recording():
    frame_main.grid(row=0, column=0, padx=3, pady=5) 
    frame_main.grid_remove()
    frame_recording.grid(row=0, column=0, padx=3, pady=5)

    
def check_recording():
    last_name = enter_last_name.get()
    firs_name = enter_firs_name.get()
    email = enter_email.get()
    password = enter_password.get()
    password_2 = enter_password_2.get()
    
    if last_name and firs_name and email and (password == password_2):
        # Le programme crype le mot de passe
        priv_key, pub_key = rsa.newkeys(512)
        print(priv_key)
        print(pub_key)
        password_encrypt = rsa.encrypt(password_2.encode(), pub_key)
        
        data_user = {
            "last_name": last_name,
            "firs_name": firs_name,
            "email": email,
            "password": password_encrypt
        }
        
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                last_name text,
                firs_name text,
                email text,
                password text
                )
            """
            )
            cursor.execute("INSERT INTO users VALUES (:last_name, :firs_name, :email, :password)", data_user)
            
            conn.commit()
            conn.close()
        except sqlite3.Error:
            print("Une erreur est survenu dans le scripte SQL")
        else:
            messagebox.showinfo("Inscription", "Vous venez de crée un compte")
            
    else:
        label_error["fg"] = "red"

    
def connection():
    try:
        get_data = cursor.execute("SELECT * FROM users")
        data_users = get_data.fetchall()
        
        conn.commit()
        conn.close()
    except sqlite3.Error:
        print("Une erreur est survenu dans le scripte SQL")
    else:
        email = input("Veuillez entrer vôtre email: ")
        password = input("Veuillez entrer vôtre mot de passe: ")
        
        for user in data_users:
            if user[2] == email and user[3] == password:
                print("compte existe")
                break
        else:
            print("Le compte n'existe pas !")


def back_recording():
    frame_recording.grid_remove()
    frame_main.grid()
    
    
window = tkinter.Tk()
window.geometry("720x480")
window.title("Popo Page")
window.resizable(False, False)

# Frame principale
frame_main = tkinter.Frame(window)

bnt_recording = tkinter.Button(frame_main, text="Inscription", command=display_recording)
bnt_recording.grid(row=0, column=0, padx=3, pady=5)

# Frame d'inscription
frame_recording = tkinter.Frame(window)
frame_recording.grid(row=0, column=0, padx=180, pady=100)

label_last_name = tkinter.Label(frame_recording, text="Veuillez entrer vôtre addresse nom")
label_last_name.grid(row=0, column=0, sticky="w")
enter_last_name = tkinter.Entry(frame_recording, bg="white")
enter_last_name.grid(row=1, column=0, sticky="w")

label_firs_name = tkinter.Label(frame_recording, text="Veuillez entrer vôtre addresse prénom")
label_firs_name.grid(row=2, column=0, sticky="w")
enter_firs_name = tkinter.Entry(frame_recording)
enter_firs_name.grid(row=3, column=0, sticky="w")

label_email = tkinter.Label(frame_recording, text="Veuillez entrer vôtre addresse email")
label_email.grid(row=4, column=0, sticky="w")
enter_email = tkinter.Entry(frame_recording)
enter_email.grid(row=5, column=0, sticky="w")

label_password = tkinter.Label(frame_recording, text="Veuillez entrer vôtre mot de passe")
label_password.grid(row=7, column=0, sticky="w")
enter_password = tkinter.Entry(frame_recording)
enter_password.grid(row=8, column=0, sticky="w")

label_password_2 = tkinter.Label(frame_recording, text="Veuillez confirmer le mot de passe")
label_password_2.grid(row=9, column=0, sticky="w")
enter_password_2 = tkinter.Entry(frame_recording)
enter_password_2.grid(row=10, column=0, sticky="w")

label_error = tkinter.Label(frame_recording, text="Veuillez remplir tout les champ")
label_error.grid(row=11, column=0, sticky="w")

bnt_recording = tkinter.Button(frame_recording, text="S'inscrire", command=check_recording)
bnt_recording.grid(row=12, column=0, sticky="w", ipadx=3, ipady=2)

bnt_back = tkinter.Button(frame_recording, text="Retour", command=back_recording)
bnt_back.grid(row=13, column=0, sticky="w", ipadx=3, ipady=2)


window.mainloop()