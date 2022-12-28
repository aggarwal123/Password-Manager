from cryptography.fernet import Fernet
import os


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split(" | ")
            print("User:", fer.decrypt(user.encode()).decode(), "| Password:",
                  fer.decrypt(password.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(fer.encrypt(name.encode()).decode() + " | " +
                fer.encrypt(pwd.encode()).decode() + "\n")


filesize = os.path.getsize("passwords.txt")
if filesize == 0:
    write_key()
key = load_key()
fer = Fernet(key)


while True:
    mode = input(
        "\nWould you like to add a new password or view existing ones or quit (view, add, quit)? ").lower()
    if mode == "quit":
        break
    if mode == "view":
        print("\n")
        view()
    elif mode == "add":
        add()
    else:
        print("INVALID MODE!")
        continue
