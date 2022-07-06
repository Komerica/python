from data2 import question_data
from question_model2 import Question
from quiz_brain2 import QuizBrain

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_bank.append(Question(text, answer))

print(question_bank[0].text)
print(question_bank[0].answer)

quiz = QuizBrain()

while quiz.is_more_question(question_bank):
    quiz.next_question(question_bank)

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_num}")