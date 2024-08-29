#  Send via SMTP GMAIL
---

![](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)  ![](https://camo.githubusercontent.com/050fc4e602f25dd4fc337b873fbc62b7d393673a9f4b1e7529a9a61ea35485a5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d4646443433423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d626c7565)   ![](https://img.shields.io/badge/Python-3.11-<>.svg)  ![   ]( https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white) ![[obsidian-icon.svg|40x40]]

---
## Description

Ce projet est une application Python utilisant la bibliothèque Tkinter pour créer une interface graphique permettant d'envoyer des emails via un serveur SMTP Gmail. L'utilisateur peut saisir son email, son mot de passe, l'email du destinataire, le sujet et le corps du message. L'application se charge ensuite d'envoyer l'email en utilisant les informations fournies.
 
## Fonctionnalités

- **Interface Graphique** : Créée avec Tkinter, l'interface permet de saisir facilement les informations nécessaires pour envoyer un email.
- **Envoi d'Email via SMTP** : Le projet utilise le module `smtplib` pour se connecter à un serveur SMTP et envoyer des emails.
- **Gestion des erreurs** : Si une erreur survient lors de l'envoi de l'email, une boîte de dialogue s'affiche pour informer l'utilisateur.

## Prérequis
 
 Avant de lancer le projet, assurez-vous d'avoir les éléments suivants installés :
- Python 3.x
- Les bibliothèques Python suivantes : 
  - `tkinter` (inclus par défaut avec Python)
  - `smtplib` (inclus par défaut avec Python)

## Installation

1. Clonez le dépôt sur votre machine locale :
    ```bash
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo
    ```

2. Assurez-vous que les dépendances nécessaires sont installées.

## Utilisation

1. Exécutez le script principal pour lancer l'application :
    ```bash
    python main.py
    ```

2. Remplissez les champs suivants dans l'interface :
    - **Courriel** : Votre adresse email Gmail.
    - **Mot de passe** : Le mot de passe de votre compte Gmail.
    - **À** : L'adresse email du destinataire.
    - **Objet** : Le sujet de votre email.
    - **Message** : Le corps de votre email.

3. Cliquez sur le bouton "Soumettre" pour envoyer l'email.

## Structure du Projet

- `main.py` : Le script principal qui crée l'interface graphique avec Tkinter et gère les événements.
- `send.py` : Un module séparé qui gère l'envoi des emails via SMTP.

## Contributions

Les contributions sont les bienvenues. Si vous avez des idées d'améliorations ou des bugs à signaler, n'hésitez pas à ouvrir une issue ou une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE.txt) pour plus de détails.
## Avertissements

- **Sécurité** : L'application demande l'email et le mot de passe Gmail de l'utilisateur. Assurez-vous de ne pas partager ces informations sensibles et envisagez d'utiliser des mots de passe d'application (au lieu de votre mot de passe principal) pour des raisons de sécurité.
- **Limites** : Ce projet est principalement un exemple pédagogique et ne devrait pas être utilisé pour des envois massifs d'emails ou des applications critiques sans modifications appropriées.