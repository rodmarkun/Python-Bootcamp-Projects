from tkinter import *
import pandas
import random



BACKGROUND_COLOR = "#B1DDC6"

try:
    french_to_eng_words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_to_eng_words_data = pandas.read_csv("data/french_words.csv")
to_learn = french_to_eng_words_data.to_dict(orient="records")

current_card = {}

# Button Functions
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    new_word()

def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(canvas_img, image=back_card_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

# Window
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

# Canvas with card
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_img)
canvas.config(bg=BACKGROUND_COLOR)

# Canvas Text
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
button_wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_image, highlightthickness=0, command=new_word)
button_wrong.grid(row=1, column=0)

button_right_image = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_image, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

new_word()

window.mainloop()