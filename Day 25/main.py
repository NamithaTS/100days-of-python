import csv

# import csv
# file=open("weather_data.csv","r")# data=csv.reader(file)
# for row in data:
#     print(row)
#     print(row[1])


# data1=list(file.readlines())
# data=[]
# for line in data1:
#     line=line.strip()
#     data.append(line)
# print(data)
import pandas as pd
from numpy.ma.extras import average
#
# data=pd.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# print(data.to_dict())
# print(sum(data["temp"].to_list())/len(data["temp"].to_list()))
# print(average(data["temp"].to_list()))
# print(round(data["temp"].mean(),2))
# print(max(data["temp"]))
# print(data["temp"].max())
# c=data["condition"].to_list()
# print(c)
# l=[]
# for item in c:
#     if item not in l:
#
#         l.append(item)
# print(l)
# print(data[data.day=="Monday"])

# print(data[data.temp==data["temp"].max()])
# print(data.temp.max())
# m=data[data.temp==data.temp.max()]
# print(m.day)
# m=data[data.day=="Monday"]
# # print(m.temp)
# print(m.temp[0]*(9/5)+32)

# d={"marks":[34,45,56,78],"grades":['a','b','c','f']}
# print(pd.DataFrame(d))
# n=pd.DataFrame(d)
# n.to_csv("new.csv")

data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(len(data[data["Primary Fur Color"]=="Gray"]))
d={"Fur Color":["Gray","Cinnamon","Black"],"count":[len(data[data["Primary Fur Color"]=="Gray"]),len(data[data["Primary Fur Color"]=="Cinnamon"]),len(data[data["Primary Fur Color"]=="Black"])]}
df=pd.DataFrame(d)
df.to_csv("sq_count.csv")

