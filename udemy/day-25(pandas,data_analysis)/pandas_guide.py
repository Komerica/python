# 🟥 Not a good data (Painful to work with this data!!)
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

import csv

print("🧡 방법1) data를 List로 뽑아서 List에 저장하는 방법")
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)     # csv.reader object로 데이터 뽑힘!
    temperatures = []
    for row in data:
        print(row)  # List로 뽑힘!
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    # Result: [12, 14, 15, 14, 21, 22, 24]

print("🧡 방법2) data를 Dictionary로 뽑아서 List로 저장하는 방법")
with open("weather_data.csv") as data_file:
    data = csv.DictReader(data_file)
    print(data)     # csv.DictReader object로 데이터 뽑힘!
    temperatures = []
    for row in data:
        print(row)  # Dictionary로 뽑힘!
        temperatures.append(int(row["temp"]))
    print(temperatures)
    # Result: [12, 14, 15, 14, 21, 22, 24]


print("""
██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║██╔██╗██║██║░░██║███████║╚█████╗░
██╔═══╝░██╔══██║██║╚████║██║░░██║██╔══██║░╚═══██╗
██║░░░░░██║░░██║██║░╚███║██████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═════╝░""")
import pandas

print("🟧 pandas 사용법!")
data = pandas.read_csv("weather_data.csv")
print(data)
print(data.temp)    # object처럼 접근 가능!
print(data["temp"]) # dictionary처럼 접근 가능!

print("🧡 pandas Data types")
print(type(data))           # DataFrame
print(type(data.temp))      # Series
print(type(data["temp"]))   # Series


print("🟧 pandas Data Conversion")
print("🧡 DataFrame to Dictionary")
data_dict = data.to_dict()
print(data_dict)

print("🧡 Series to List")
data_list = data.temp.to_list()
print(data_list)

print("🟧 Average of Series")
print("🧡 방법1) for loop로 sum구해서 average 내기")
temp_sum = 0
for temp in data.temp:
    temp_sum += temp
average = temp_sum / len(data.temp)
print(average)

print("🧡 방법2) temp Series(column)을 list로 만들어서 sum구해서 average 내기!")
data_list = data.temp.to_list()
average = sum(data_list) / len(data_list)
print(average)

print("🧡 방법3) pandas mean 사용!")     # The Easiest Way!
print(data.mean())          # Method1: DataFrame에서 자동으로 숫자가 있는 Series를 찾아서 평균을 내준다!
print(data["temp"].mean())  # Method2
print(data.temp.mean())     # Method3


print("🟧 Max of Series")
print(data.max())           # Method1
print(data["temp"].max())   # Method2
print(data.temp.max())      # Method3


print("🟧 Get data in Columns")
print("🧡 방법1")
print(data["condition"])
print("🧡 방법2")
print(data.condition)
# Pandas, behind the scenes, has taken each of the columns and each of the heading and converted those headings into attributes!


print("🟧 Get Data in Rows")     # 조건에 맞는 row 찾기!
print("🧡 방법1")
print(data[data.day == "Monday"])
print("🧡 방법2")
print(data[data["day"] == "Monday"])


print("🟧 Highest temperature in Rows")      # 조건에 맞는 Row 찾기!
print("🧡 방법1")
print(data[data.temp == data.temp.max()])
print("🧡 방법2")
print(data[data["temp"] == data.temp.max()])
print("🧡 방법3")
print(data[data["temp"] == data["temp"].max()])


print("🟧 Get Monday's temp & condition")
monday = data[data.day == "Monday"]
print(monday)           # Monday's Row
print(monday.temp)      # Monday's temp
print(monday.condition) # Monday's condition


print("🟧 Celsius to Fahrenheit Conversion")
monday_temp = data[data.day == "Monday"].temp
print(monday_temp)      # 아래와 결과가 다른 걸 주목!
monday_temp = int(data[data.day == "Monday"].temp)
print(monday_temp)      # 12
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


print("🟧 Create a DataFrame from scratch")
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)


print("🟧 Save the created DataFrame above as a CSV file")
data.to_csv("new_data2.csv")