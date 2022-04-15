# Get count of all squirrels of each fur color and represent it as it follows:
#,Fur Color,Count
#0,grey,2473
#1,red,392
#2,black,103

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_fur_list = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
red_fur_list = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_fur_list = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

squirrel_dict = {
    "Fur Color" : ["grey", "red", "black"],
    "Count" : [len(grey_fur_list), len(red_fur_list), len(black_fur_list)]
}

final_fur_data = pandas.DataFrame(squirrel_dict)
print(final_fur_data)