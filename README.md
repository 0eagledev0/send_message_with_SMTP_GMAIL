#  Send via SMTP GMAIL

![](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)  ![](https://camo.githubusercontent.com/050fc4e602f25dd4fc337b873fbc62b7d393673a9f4b1e7529a9a61ea35485a5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d4646443433423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d626c7565)   ![](https://img.shields.io/badge/Python-3.11-<>.svg)  ![]( https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white) <img src="image/obsidian-icon.svg" alt="Description of the image" width="50"/>

---

[Lire en français](README_FR.md)

---
## Description

This project is a Python application using the Tkinter library to create a graphical interface for sending emails via a Gmail SMTP server. Users can enter their email address, password, recipient's email address, subject, and body of the message. The application then handles sending the email using the provided information.
 
## Features

- **Graphical Interface**: Created with Tkinter, the interface allows users to easily enter the necessary information to send an email.
- **Email Sending via SMTP**: The project uses the `smtplib` module to connect to an SMTP server and send emails.
- **Error Handling**: If an error occurs while sending the email, a dialog box will appear to inform the user.

## Prerequisites

Before running the project, make sure you have the following installed:
- Python 3.6, 3.7, 3.8, 3.9, 3.10, or 3.11
- The following Python libraries:
  - `tkinter` (included by default with Python)
  - `smtplib` (included by default with Python)

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/0eagledev0/send_message_with_SMTP_GMAIL.git
    cd send_message_with_SMTP_GMAIL
    ```

2. Ensure that the necessary dependencies are installed.

## Usage

1. Run the main script to launch the application:
    ```bash
    python main.py
    ```

2. Fill in the following fields in the interface:
    - **Email**: Your Gmail email address.
    - **Password**: The password for your Gmail account.
    - **To**: The recipient's email address.
    - **Subject**: The subject of your email.
    - **Message**: The body of your email.

3. Click the "Submit" button to send the email.

## Project Structure

- `main.py`: The main script that creates the graphical interface with Tkinter and handles events.
- `send.py`: A separate module that handles sending emails via SMTP.

## Contributions

Contributions are welcome. If you have improvement ideas or bugs to report, feel free to open an issue or a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for more details.

## Warnings

- **Security**: The application requests the user's Gmail email and password. Make sure not to share these sensitive details and consider using application-specific passwords (instead of your main password) for security reasons.
- **Limitations**: This project is primarily an educational example and should not be used for mass email sending or critical applications without appropriate modifications.
