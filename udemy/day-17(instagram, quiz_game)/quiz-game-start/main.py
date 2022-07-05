from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#############
# My code 1 #
#############
# question_bank = []
# for i in range(len(question_data)):
#     text = question_data[i]["text"]
#     answer = question_data[i]["answer"]
#     question_bank.append(Question(text, answer))
#
# print(question_bank)


##############
# Udemy code #
##############
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank[0].text)    # 이제 이렇게 접근가능!
print(question_bank[0].answer)  # 이제 이렇게 접근가능!


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
