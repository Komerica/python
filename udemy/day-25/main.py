#❌ It would be painful to work with the data below. Comma Separated Value & \n
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
print(data["temp"])
