#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import seaborn as sb
 

#Storing the file in the variable: UberDataSet 
UberDataSet=pd.read_csv("Uber_HourlyAggregate.csv")


#Returns first five data to see its structure
print(UberDataSet.head())
print()
print(UberDataSet.isnull().sum()) #prints if there are any null valus. It will sum up the number null values/fields. 
print()
print(UberDataSet.info())#prints number of columns and rows
print()
print((UberDataSet.describe())) #prints mean, medium,standard deviation, minimum and maximum values of each column.


#Line Graph depicting Hourly mean travel time
mp.figure(figsize=(10,6))
sb.lineplot(x='Hour_of_the_Day', y='Mean_Travel_Time', data=UberDataSet, marker='o', color='r')
mp.title('Hourly Mean Travel Time (Line Plot)')
mp.xlabel('Hour of the day')
mp.ylabel('Mean Travel Time (in seconds)')
mp.grid(True)
mp.show()

#Box plot depicting Hourly mean travel time  
mp.figure(figsize=(10,6))
sb.boxplot(x='Hour_of_the_Day', y='Mean_Travel_Time', data=UberDataSet, palette='coolwarm')
mp.title('Hourly Mean Travel Time (Box Plot)')
mp.xlabel('Hour of the day')
mp.ylabel('Mean Travel Time (in seconds)')
mp.show()

#Heat map depicting areas of high or low travel time between source-destination pairs.
pivot_table = UberDataSet.pivot_table(index="Destination_ID", columns="Source_ID", values="Mean_Travel_Time",aggfunc='mean')
mp.figure(figsize=(10,6))
sb.heatmap(pivot_table, cmap="viridis", annot=False)
mp.title("Source-Destination Travel Time Heat Map")
mp.xlabel("Source ID")
mp.ylabel("Destination ID")
mp.show()
