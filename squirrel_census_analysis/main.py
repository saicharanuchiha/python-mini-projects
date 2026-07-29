import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Data.csv")
gray_squirrel = sum(data["Primary Fur Color"] == "Gray")
red_squirrel = sum(data["Primary Fur Color"] == "Cinnamon")
black_squirrel = sum(data["Primary Fur Color"] == "Black")
print(gray_squirrel)
print(red_squirrel)
print(black_squirrel)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")