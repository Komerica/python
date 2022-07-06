from data2 import question_data
from question_model2 import Question
from quiz_brain2 import QuizBrain

####################
### Coded myself ###
# Without any help #
####################

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    question_bank.append(Question(text, answer))

print(question_bank[0].text)
print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.is_more_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_num}")