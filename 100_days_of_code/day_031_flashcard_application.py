from tkinter import *
from urllib.request import urlopen

import pandas
import random
import os

DATA_FILE = 'https://raw.githubusercontent.com/sidorkinandrew/sidorkinandrew.github.io/mainaster/100-days-of-python/day_031/data/french_words.csv'
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(DATA_FILE)
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
    print(to_learn)
else:
    to_learn = data.to_dict(orient="records")
    print(to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    print(current_card)
    to_learn.remove(current_card)
    print(len(to_learn))
    _data = pandas.DataFrame(to_learn)
    if not os.path.exists("data"):
        os.mkdir("data")
    _data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def get_picture_from_url(url):
    u = urlopen(url)
    raw_data = u.read()
    u.close()
    return raw_data

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(data=get_picture_from_url("https://github.com/sidorkinandrew/sidorkinandrew.github.io/raw/mainaster/100-days-of-python/day_031/images/card_front.png"))  # "images/card_front.png"
card_back_img = PhotoImage(data=get_picture_from_url("https://github.com/sidorkinandrew/sidorkinandrew.github.io/raw/mainaster/100-days-of-python/day_031/images/card_back.png"))  # "images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(data=get_picture_from_url("https://github.com/sidorkinandrew/sidorkinandrew.github.io/raw/mainaster/100-days-of-python/day_031/images/wrong.png"))  # file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(data=get_picture_from_url("https://github.com/sidorkinandrew/sidorkinandrew.github.io/raw/mainaster/100-days-of-python/day_031/images/right.png"))  # file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
