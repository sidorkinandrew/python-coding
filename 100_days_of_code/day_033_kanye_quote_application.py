from tkinter import *
from urllib.request import urlopen

import requests

BACKGROUND_URL = "https://github.com/sidorkinandrew/sidorkinandrew.github.io/raw/mainaster/100-days-of-python/day_033/background.png"
KANYE_URL = "https://github.com/sidorkinandrew/sidorkinandrew.github.io/raw/mainaster/100-days-of-python/day_033/kanye.png"


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    print(quote)
    if len(quote) > 60:
        canvas.itemconfigure(quote_text, font=("Arial", 20, "bold"))
    else:
        canvas.itemconfigure(quote_text, font=("Arial", 28, "bold"))
    canvas.itemconfig(quote_text, text=quote)


def get_picture_from_url(url):
    u = urlopen(url)
    raw_data = u.read()
    u.close()
    return raw_data


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(data=get_picture_from_url(BACKGROUND_URL))  # (file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click Kanye icon to start", width=250, font=("Arial", 28, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(data=get_picture_from_url(KANYE_URL))  # (file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
