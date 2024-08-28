import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox


def send(from_email, password, message, subject, to_email):
    try:
        msg = EmailMessage()
        msg.set_content(message)
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Connexion au serveur SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()

    except Exception as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")
