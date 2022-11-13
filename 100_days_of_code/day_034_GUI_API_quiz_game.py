from tkinter import *
from urllib.request import urlopen

import requests
import html

THEME_COLOR = "#375362"
TRUE_TICK_URL = "https://github.com/sidorkinandrew/sidorkinandrew.github.io/raw/mainaster/100-days-of-python/day_034/true.png"
FALSE_TICK_URL = "https://github.com/sidorkinandrew/sidorkinandrew.github.io/raw/mainaster/100-days-of-python/day_034/false.png"
QUESTION_FONT = ("Arial", 18, "italic")

def get_picture_from_url(url):
    u = urlopen(url)
    raw_data = u.read()
    u.close()
    return raw_data


class Question:

    def __init__(self, q_text, q_answer, q_category=None):
        self.text = q_text
        self.answer = q_answer
        self.category = q_category


class QuestionBank:

    def __init__(self):
        self.question_bank = []

    def import_data_from_list(self, list_of_data, reset=False):
        self.question_bank = [] if reset else self.question_bank
        for question in list_of_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            self.question_bank.append(Question(question_text, question_answer))

    def import_data_from_opentdb(self, q_difficulty="", q_category="", q_type="boolean", q_limit=50, reset=False):
        # https://opentdb.com/api_category.php
        # https://opentdb.com/api.php?amount=50&type=boolean
        # https://opentdb.com/api.php?amount=50&category=28&difficulty=easy&type=boolean
        self.question_bank = [] if reset else self.question_bank
        parameters = {"amount": q_limit, "type": q_type}
        json_data = requests.get(f"https://opentdb.com/api.php", params=parameters).json()
        if "response_code" not in json_data or json_data["response_code"] != 0:
            message = f"[QuestionBank] Error importing from OpenDB! Respones code is {json_data['response_code']}"
            print(message)
            return message
        for question in json_data["results"]:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            question_category = question["category"]
            self.question_bank.append(Question(question_text, question_answer, question_category))


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.logo = """

  ______      __    __   __   ________       _______      ___      .___  ___.  _______ 
 /  __  \    |  |  |  | |  | |       /      /  _____|    /   \     |   \/   | |   ____|
|  |  |  |   |  |  |  | |  | `---/  /      |  |  __     /  ^  \    |  \  /  | |  |__   
|  |  |  |   |  |  |  | |  |    /  /       |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  `--'  '--.|  `--'  | |  |   /  /----.   |  |__| |  /  _____  \  |  |  |  | |  |____ 
 \_____\_____\\______/  |__|  /________|    \______| /__/     \__\ |__|  |__| |_______|

                                                                                       """
        print(self.logo)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        current_category = self.question_list[self.question_number].category
        if ":" in current_category:
            current_category = current_category.split(": ")[1]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        user_question = f"Q.{self.question_number} " \
                        f"[{current_category}]: " \
                        f"{q_text}"
        return user_question

    def check_answer(self, user_answer):
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False


class QuizInterfaceUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=QUESTION_FONT)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=300, bg="white")
        self.question_text = self.canvas.create_text(
            200,
            150,
            width=390,
            text="Question Text goes here",
            fill=THEME_COLOR,
            font=QUESTION_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(data=get_picture_from_url(TRUE_TICK_URL))  # (file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(data=get_picture_from_url(FALSE_TICK_URL))  # (file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


question_bank = QuestionBank()
question_bank.import_data_from_opentdb()
quiz = QuizBrain(question_bank.question_bank)
quiz_ui = QuizInterfaceUI(quiz)

