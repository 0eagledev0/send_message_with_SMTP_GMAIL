import tkinter as tk
from send import send

def set_placeholder(entry, placeholder):
    """
    Set a placeholder text in the given entry widget.

    Parameters:
    - entry: The Tkinter Entry widget where the placeholder will be set.
    - placeholder: The placeholder text to display.
    """
    # Insert the placeholder text and set its color to grey.
    entry.insert(0, placeholder)
    entry.config(fg='grey')

    def on_focus_in(event):
        """
        Clear the placeholder text when the entry widget gains focus.
        """
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def on_focus_out(event):
        """
        Reapply the placeholder text if the entry widget loses focus and is empty.
        """
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg='grey')

    # Bind focus in and out events to the corresponding functions.
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def on_submit():
    """
    Collect input values from the form, display them in the console,
    and send the email using the `send` function.
    """
    # Retrieve the values from the input fields.
    from___email = from_email.get()
    password = entry2.get()
    to____email = to_email.get()
    subjeet = subject.get()
    message_Body = text_box.get("1.0", tk.END)

    # Display the values in the console for debugging purposes.
    print("from email:", from___email)
    print("pass:", password)
    print("to email:", to____email)
    print("subjeet:", subjeet)
    print("message:", message_Body)
    # Call the send function with the collected data.
    send(from___email, password, message_Body, subjeet, to____email)

# Create the main application window.
root = tk.Tk()
root.title("SMTP email")
root.geometry("700x600")
root.config(bg="black")
root.iconbitmap("image/socialemailcircularbutton_80177.ico")
# Add a title label to the window.
title_label = tk.Label(root, text="Send a message using your Gmail SMTP.", font=("Arial", 20, "underline", "bold"),bg="black", fg="white")
title_label.pack(pady=10)
# Add a subtitle label for the Gmail connection section.
subtitle_label = tk.Label(root, text="Gmail connection:", font=("Arial", 16, "underline", "bold"),bg="black", fg="green")
subtitle_label.pack(pady=(10, 5))
# Define the font size for the input fields.
font_size = ("Arial", 12)
# Create and configure the email input field with a placeholder.
from_email = tk.Entry(root, width=50, font=font_size)
from_email.pack(pady=5)
set_placeholder(from_email, "Enter your email here...")
# Create and configure the password input field with a placeholder.
entry2 = tk.Entry(root , show="*", width=50 , font=font_size)
entry2.pack(pady=5)
set_placeholder(entry2, "Enter your password here...")
# Add a subtitle label for the message section.
subtitle_label = tk.Label(root, text="Message:", font=("Arial",  16, "underline", "bold"),bg="black", fg="green")
subtitle_label.pack(pady=(10, 5))
# Create and configure the recipient email input field with a placeholder.
to_email = tk.Entry(root, width=50, font=font_size)
to_email.pack(pady=5)
set_placeholder(to_email, "Enter the email address you want to send to.")
# Create and configure the subject input field with a placeholder.
subject = tk.Entry(root , width=50, font=font_size)
subject.pack(pady=5)
set_placeholder(subject, "Add a subject.")
# Create and configure the text box for the message body.
text_box = tk.Text(root, height=10, width=70, font=font_size)
text_box.pack(pady=5)
# Create and configure the submit button.
submit_button = tk.Button(root, text="Submit", command=on_submit, font=("Arial", 16, "underline", "bold"), bg="green", fg="white")
submit_button.pack(pady=10)
# Run the main event loop.
root.mainloop()
