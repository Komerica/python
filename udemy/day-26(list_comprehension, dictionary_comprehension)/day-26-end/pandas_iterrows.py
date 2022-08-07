student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries Using "For Loop"
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# We can consider DataFrame pretty much as if we are working with Dictionaries.
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a DataFrame (can't do much with these)
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Iterrows: it allows us to loop through each of the rows of the DataFrame rather than each of the columns.
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
