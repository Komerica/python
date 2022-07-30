# ❌ It would be painful to work with the data below. Comma Separated Value & \n
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
# Result: ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

import csv

# With Pandas, it will be easier! It won't be faff like this.
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    # How to skip the first loop
    # iterdata = iter(data)
    # next(iterdata)
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)
# Result: [12, 14, 15, 14, 21, 22, 24]

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
print(type(data))           # DataFrame: Equivalent to the whole table
print(type(data["temp"]))   # Series: Equivalent to a list(Single column in your table)

###################
# Data Conversion #
###################
print("🟧 DataFrame to Dictionary")
data_dict = data.to_dict()
print(data_dict)

print("🟧 Series to List")
temp_list = data["temp"].to_list()
print(temp_list)

#####################################################
print("🟧 Average of Series(A column of DataFrame)")
print("🧡 방법1")
average = sum(temp_list) / len(temp_list)
print(average)
print("🧡 방법2 Easier way!")
print(data["temp"].mean())

print("🟧 Maximum value from 'temp' column (Data Series Method)")
print(data["temp"].max())

print("🟧 Get data in Columns")
print("🧡 방법1")
print(data["condition"])
print("🧡 방법2")
print(data.condition)   # Pandas, behind the scenes, has taken each of the columns and each of the heading and converted those headings into attributes!

print("🟧 Get Data in Row")
print(data[data.day == "Monday"])
print(data[data["day"] == "Monday"])

print("🟧 Highest temperature in Row")
print(data[data.temp == data.temp.max()])

print("🟧 Get Monday's temp")
monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp)

print("🟧 Celsius to Fahrenheit Conversion")
monday_temp = int(monday.temp)  # int로 무조건 convert해줘야함!
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
data.to_csv("new_data.csv")

