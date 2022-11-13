from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import pickle
import os
import base64

EXCLUDE_PASSWORD_SYMBOLS = '/`'
TEMPORARY_FILE = "data.pckl"


class PasswordData:
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    def __init__(self):
        self.password_data = {}
        try:
            self.password_data = pickle.load(open(TEMPORARY_FILE, "rb"))
            os.remove(TEMPORARY_FILE)
        except Exception as e:
            print(e)

    def encoder(self, a_string):
        return base64.b64encode(a_string.encode('utf-8'))

    def decoder(self, some_bytes):
        return base64.decodebytes(some_bytes)

    def add_data(self, website, email, password):
        self.password_data[self.encoder(website)] = [self.encoder(email), self.encoder(password)]
        self.save_data()

    def save_data(self):
        self.password_data[self.encoder("password_letters_used")] = self.encoder(self.symbols)
        self.password_data[self.encoder("password_numbers_used")] = self.encoder(self.letters)
        self.password_data[self.encoder("password_symbols_used")] = self.encoder(self.numbers)
        pickle.dump(self.password_data, open(TEMPORARY_FILE, "wb"))


password_data = PasswordData()


# Password Generator Project


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    password_list = [char for char in password_list if char not in set(EXCLUDE_PASSWORD_SYMBOLS)]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            password_data.add_data(website, email, password)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="day_029_password_manager_logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


def handle_closing():
    print("saving data ....", end="")
    password_data.save_data()
    print(".. done")
    window.destroy()


window.protocol("WM_DELETE_WINDOW", handle_closing)

window.mainloop()
