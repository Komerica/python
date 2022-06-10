# Adding evens between 1 and 100

# Method1) My answer
sum_of_evens = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_of_evens += i
print(sum_of_evens)


# Method2) Udemy answer
sum_of_evens = 0
for i in range(2, 101, 2):
    sum_of_evens += i
print(sum_of_evens)
