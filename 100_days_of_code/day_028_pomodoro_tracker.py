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


class Pomodorotracker:

    def __init__(self, tk_window):
        self.repetitions = 0
        self.timer = None
        self.countdown = 0
        self.total_marks = ""

        self.window = tk_window

        self.title_label = Label(text="Click Start", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
        self.title_label.grid(column=1, row=0)

        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_img = PhotoImage(file="day_028_pomodoro_tracker_background.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        self.start_button = Button(text="Start", highlightthickness=0, command=self.start_timer)
        self.start_button.grid(column=0, row=2)

        self.reset_button = Button(text="Reset", highlightthickness=0, command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)

        self.check_marks = Label(fg=GREEN, bg=YELLOW)
        self.check_marks.grid(column=1, row=3)

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Click Start")
        self.check_marks.config(text="")
        self.repetitions = 0
        self.countdown = 0
        self.total_marks = ""

    def start_timer(self):
        # fixed TO_DO: 1. multiple clicks create multiple timers !
        if self.countdown > 0:
            pass
        else:

            self.repetitions += 1

            work_seconds = WORK_MIN * 60
            short_break_seconds = SHORT_BREAK_MIN * 60
            long_break_seconds = LONG_BREAK_MIN * 60

            print(self.repetitions, self.countdown)
            if self.repetitions % 8 == 0:  # every 8th repetition should be a big break
                self.countdown = long_break_seconds
                self.run_countdown(long_break_seconds)
                self.title_label.config(text="Long Break!", fg=RED)
            elif self.repetitions % 2 == 0:
                self.countdown = short_break_seconds
                self.run_countdown(short_break_seconds)
                self.title_label.config(text="Short Break", fg=PINK)
            else:
                self.countdown = work_seconds
                self.run_countdown(work_seconds)
                self.title_label.config(text="Work Work!!", fg=GREEN)

    def run_countdown(self, run_seconds):
        count_minutes = math.floor(run_seconds / 60)
        count_seconds = run_seconds % 60
        if count_seconds < 10:
            count_seconds = f"0{count_seconds}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_minutes}:{count_seconds}")
        if self.countdown > 0:
            self.countdown -= 1
            self.timer = window.after(1000, self.run_countdown, run_seconds - 1)
        else:
            self.countdown = run_seconds
            self.start_timer()
            self.total_marks = ""
            work_sessions = math.floor(self.repetitions / 2)
            for _ in range(work_sessions):
                self.total_marks += "✔"
            self.check_marks.config(text=self.total_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro tracker")
window.config(padx=100, pady=50, bg=YELLOW)

pomodoro_object = Pomodorotracker(window)

window.mainloop()
