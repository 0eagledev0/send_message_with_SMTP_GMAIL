import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox


def send(from_email, password, message, subject, to_email):
    """
    Sends an email using Gmail's SMTP server.

    Parameters:
    from_email (str): The sender's email address.
    password (str): The sender's email password.
    message (str): The content of the email.
    subject (str): The subject line of the email.
    to_email (str): The recipient's email address.
    """
    try:
        # Create an EmailMessage object and set its content and headers
        msg = EmailMessage()
        msg.set_content(message)
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Start TLS encryption for the connection
        server.starttls()
        # Log in to the SMTP server using the provided credentials
        server.login(from_email, password)
        # Send the email
        server.send_message(msg)
        # Terminate the SMTP session
        server.quit()
    except Exception as e:
        # Create a Tkinter root window and hide it
        root = tk.Tk()
        root.withdraw()
        # Show an error message box with the exception details
        messagebox.showerror("Error", f"An error has occurred: {e}")
