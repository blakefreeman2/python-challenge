import os

import csv
### PyBank

#![Revenue](Images/revenue-per-lead.png)

#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#* Your task is to create a Python script that analyzes the records to calculate each of the following:

  #* The total number of months included in the dataset

  #* The net total amount of "Profit/Losses" over the entire period

  #* The average of the changes in "Profit/Losses" over the entire period

  #* The greatest increase in profits (date and amount) over the entire period

  #* The greatest decrease in losses (date and amount) over the entire period

#* As an example, your analysis should look similar to the one below:
csvpath = os.path.join('Resources', 'budget_data.csv')
months = []
profit = []
change = []
Total = 0
MS = 0
Value = 0

with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)

  for row in csvreader:
    months.append(row[0])
    #print(months)
    #print(row[0])
    profit.append(row[1])
    #print(profit)
    #print(row[1])
    Total = Total + int(row[1])
    MS = len(months)
#Change = int(profit[profit]) - int(profit[profit - 1])
Average = Total / MS
array = [months,profit]

print(change)
print(min(str(array[0,1])))
print(max(array[1]))
print(round(Average, 2))
print(MS)
print(Total)
print("------------------------------------------------------------------------")
print("There is a total of " + str(len(months)) + " months.")
