# lst = []
# with open("weather_data.csv") as weather_data:
#     lst = weather_data.readlines()
# print(lst)

# import csv
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data["Primary Fur Color"]
gray = colors[colors == "Gray"].size
cinnamon = colors[colors == "Cinnamon"].size
black = colors[colors == "Black"].size

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

out = pandas.DataFrame(data_dict)
out.to_csv("new_data.csv")



