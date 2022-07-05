from data import question_data
from question_model import Question


####################
### Coded myself ###
# Without any help #
####################

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank[0].text)    # 이제 이렇게 접근가능!
print(question_bank[0].answer)  # 이제 이렇게 접근가능!


is_game_over = False
while not is_game_over:
    question_num = 1
    got_right = 0
    for question in question_bank:
        text = question.text
        answer = input(f"Q.{question_num}: {text} (True/False): ")
        if question.answer == answer:
            got_right += 1
            print("You got it right!")
            print(f"The correct answer was: {question.answer}.")
            print(f"Your current score is: {got_right}/{question_num}")
        else:
            print("That's wrong")
            print(f"The correct answer was: {question.answer}.")
            print(f"Your current score is: {got_right}/{question_num}")

        print("\n\n")

        if question_num == len(question_bank):
            print("You've completed the quiz")
            print(f"Your final score was: {got_right}/{question_num}")
            is_game_over = True

        question_num += 1
