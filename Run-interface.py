import tkinter as tk

from send import send


def set_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg='grey')

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg='grey')

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
def on_submit():
    # Récupère les valeurs des champs et du select list
    from___email = from_email.get()
    password = entry2.get()
    to____email = to_email.get()
    subjeet = subject.get()
    message_Body = text_box.get("1.0", tk.END)

    # Affiche les valeurs dans la console
    print("from email:", from___email)
    print("pass:", password)
    print("to email:", to____email)
    print("subjeet:", subjeet)
    print("message:", message_Body)
    send(from___email, password, message_Body, subjeet, to____email)

# Créer la fenêtre principale
root = tk.Tk()
root.title("SMTP email")
root.geometry("700x600")
root.config(bg="black")
root.iconbitmap("image/socialemailcircularbutton_80177.ico")
# Ajouter un titre
title_label = tk.Label(root, text="Envoyer un message a partir de ton smtp Gmail", font=("Arial", 20, "underline", "bold"),bg="black", fg="white")
title_label.pack(pady=10)

subtitle_label = tk.Label(root, text="Connexion courriel:", font=("Arial", 16, "underline", "bold"),bg="black", fg="green")
subtitle_label.pack(pady=(10, 5))

font_size = ("Arial", 12)
from_email = tk.Entry(root, width=50, font=font_size)
from_email.pack(pady=5)
set_placeholder(from_email, "Entrez votre courriel ici...")
entry2 = tk.Entry(root , show="*", width=50 , font=font_size)
entry2.pack(pady=5)
set_placeholder(entry2, "Entrez votre mots de passe ici...")

subtitle_label = tk.Label(root, text="Message:", font=("Arial",  16, "underline", "bold"),bg="black", fg="green")
subtitle_label.pack(pady=(10, 5))
#TO
to_email = tk.Entry(root, width=50, font=font_size)
to_email.pack(pady=5)
set_placeholder(to_email, "Entrez le courriel a qui vous souhaitez envoyer")
# Subject
subject = tk.Entry(root , width=50, font=font_size)
subject.pack(pady=5)
set_placeholder(subject, "Ajouter un objet")
text_box = tk.Text(root, height=10, width=70, font=font_size)
text_box.pack(pady=5)

# bouton pour soumettre
submit_button = tk.Button(root, text="Soumettre", command=on_submit, font=("Arial", 16, "underline", "bold"), bg="green", fg="white")
submit_button.pack(pady=10)

root.mainloop()
