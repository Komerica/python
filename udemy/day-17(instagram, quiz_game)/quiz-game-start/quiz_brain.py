class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # TODO-1: asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        # self.check_answer(user_answer, current_question.answer)
        return user_answer

    # TODO-2: Checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")

    # TODO-3: Checking if we're the end of the quiz
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"Your final score is {self.score}")
            return False


