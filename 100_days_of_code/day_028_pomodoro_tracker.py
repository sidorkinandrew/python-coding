from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

repetitions = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global repetitions
    repetitions = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global repetitions
    repetitions += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:  # every 8th repetition should be a big break
        count_down(long_break_seconds)
        title_label.config(text="Long 20 min Break", fg=RED)
    elif repetitions % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_seconds)
        title_label.config(text="Work Work Work!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(countdown):
    count_minutes = math.floor(countdown / 60)
    count_seconds = countdown % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if countdown > 0:
        global timer
        timer = window.after(1000, count_down, countdown - 1)
    else:
        start_timer()
        total_marks = ""
        work_sessions = math.floor(repetitions / 2)
        for _ in range(work_sessions):
            total_marks += "✔"
        check_marks.config(text=total_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day_028_pomodoro_tracker_background.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
