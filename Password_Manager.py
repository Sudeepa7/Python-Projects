from cryptography.fernet import Fernet
import os

def load_key():
    if not os.path.exists("key.key"):
        # Generate a new key if none exists
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    
    # Load the existing key
    with open("key.key", "rb") as key_file:
        return key_file.read()

def view(fer):
    if not os.path.exists("passwords.txt"):
        print("No passwords stored yet!")
        return
    
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" not in data:
                continue
            user, passw = data.split("|")
            try:
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
            except:
                print("User:", user, "| [could not decrypt password]")

def add(fer):
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        encrypted = fer.encrypt(pwd.encode()).decode()
        f.write(f"{name}|{encrypted}\n")

def main():
    # Load or generate the key (no master password mixing)
    key = load_key()
    fer = Fernet(key)  # Use the key directly

    while True:
        mode = input("Would you like to add a new password or view existing ones (view/add), or enter q to quit: ").lower()
        if mode == "q":
            break

        if mode == "view":
            view(fer)
        elif mode == "add":
            add(fer)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()