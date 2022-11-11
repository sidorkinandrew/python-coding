import requests


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
        json_data = requests.get(f"https://opentdb.com/api.php?amount={q_limit}&type={q_type}").json()
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
        current_question = self.question_list[self.question_number]
        current_category = self.question_list[self.question_number].category
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number} [Category: {current_category if current_category is not None else 'Not specified'}]:"
            f" {current_question.text} (True(y)/False(n)): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        user_answer = user_answer.lower()
        if user_answer == "q":
            self.still_has_questions = lambda: False
        if user_answer == "y":
            user_answer = "true"
        if user_answer == "n":
            user_answer = "false"
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


question_bank = QuestionBank()
question_bank.import_data_from_opentdb()

quiz = QuizBrain(question_bank.question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
