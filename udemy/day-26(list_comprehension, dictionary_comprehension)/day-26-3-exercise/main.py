####################
### Coded myself ###
# Without any help #
####################

with open("file1.txt") as file1:
    file_1_data = file1.read().splitlines()
    print(file_1_data)

with open("file2.txt") as file2:
    file_2_data = file2.read().splitlines()
    print(file_2_data)

common_contents = [num1 for num1 in file_1_data for num2 in file_2_data if num1 == num2]
print(common_contents)

# Convert into Set (Remove duplicates)
set_common_contents = set(common_contents)
print(set_common_contents)

# Convert into list
list_common_contents = list(set_common_contents)

# Convert String into Int
result = [int(i) for i in list_common_contents]

# Write your code above 👆
print(result)


##############
# Udemy Code #
##############
with open("file1.txt") as file1:
    file_1_data = file1.readlines()
    print(file_1_data)

with open("file2.txt") as file2:
    file_2_data = file2.readlines()
    print(file_2_data)

# 여기서 int(num) 과정이 strip역할을 해줘서 \n가 날아간다! So, 아래 commented out 한 파트 생략가능!
result = [int(num) for num in file_1_data if num in file_2_data]
print(result)

# result_final = []
# for num in result:
#     stripped_num = int(num.strip("\n"))
#     result_final.append(stripped_num)
# print(result_final)

