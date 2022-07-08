from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random

WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300
WINDOW_PADDING = 50

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():

    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    new_data = {
        website:  {
            "email" : email,
            "password" : password,
        }
    }

    if len(website_entry.get()) == 0 or len(email_user_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Error", message="You have left one or more fields empty.")
    else:
        data = new_data
        try:
            f = open("password_manager.json", "r")
            data = json.load(f)
            data.update(new_data)
        finally:
            f = open("password_manager.json", "w")
            json.dump(data, f, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Recover Data ------------------------------- #

def find_password():
    try:
        f = open("password_manager.json", "r")
        data = json.load(f)
        website = website_entry.get()
        try:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Success", message=f"Email: {email}\nPassword: {password}")
        except KeyError:
            messagebox.showerror(title="Error", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
        pass


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(height=WINDOW_HEIGHT, width=WINDOW_WIDTH, padx=WINDOW_PADDING, pady=WINDOW_PADDING)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)

# BG
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_user_entry = Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
gen_password_button = Button(text="Generate Password", command=generate)
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(row=1, column=2)

canvas.grid(row=0, column=1)

window.mainloop()
