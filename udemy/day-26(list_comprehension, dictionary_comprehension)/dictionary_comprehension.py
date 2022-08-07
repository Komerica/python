import random

##############
# Udemy code #
##############
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)


################
# Coded myself #
################
names2 = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores2 = {student: random.randint(1, 100) for student in names}
print(students_scores2)

passed_students2 = {student: score for (student, score) in students_scores2.items() if score >= 60}
print(passed_students2)