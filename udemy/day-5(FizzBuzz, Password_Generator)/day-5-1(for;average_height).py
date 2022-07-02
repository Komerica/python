# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

# Method1) len쓰고 하는 version
sum = 0
for height in student_heights:
    sum += height
    average = (f"{sum / len(student_heights):.0f}")
print(average)


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# Method2) len, sum 둘다 안쓰고 하는 version
sum = 0
for height in student_heights:
    sum += height

num_of_students = 0
for student in student_heights:
    num_of_students += 1

print(f"{sum / num_of_students:.0f}")
