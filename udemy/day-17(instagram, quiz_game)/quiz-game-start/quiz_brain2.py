class QuizBrain:
    def __init__(self):
        self.score = 0
        self.question_num = 0

    def next_question(self, q_list):
        text = q_list[self.question_num].text
        correct_answer = q_list[self.question_num].answer
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {text} (True/False): ")
        self.check_answer(user_answer, correct_answer)
        print()

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_num}")

    def is_more_question(self, q_list):
        return len(q_list) > self.question_num
