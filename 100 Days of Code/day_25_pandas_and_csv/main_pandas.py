import pandas
# data = pandas.read_csv("weather_data.csv")
#
# # Convert to list mean
# temp_list = data["temp"].to_list()
# avg_list = sum(temp_list)/len(temp_list)
# # print(avg_list)
# #
# # # Panda Mean
# # print(data["temp"].mean())
# #
# # Panda Max
# # print(data["temp"].max())
# #
# # # Get data in column
# # print(data.condition)
#
# # # Get Data in Row
# # print("Data for Monday:")
# # print(data[data.day == "Monday"])
#
# # # Get day with maximum temperature:
# # max_temp = data.temp.max()
# # print("Day with maximum temprature:")
# # print(data[data.temp == max_temp])
#
# # # TODO: convert mondays temperature to Fahrenheit
# # print(data[data.day == "Monday"].temp*1.8+32)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
#


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
SQUIRREL_COLOURS = data["Primary Fur Color"].dropna().unique()
COUNT = []

for COLOR in SQUIRREL_COLOURS:
    COLOR_COUNT = len(data[data["Primary Fur Color"] == COLOR])
    COUNT.append(COLOR_COUNT)


data_dict = {
    "Fur Color": SQUIRREL_COLOURS,
    "Count": COUNT
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


