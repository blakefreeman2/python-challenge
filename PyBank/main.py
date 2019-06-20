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
mydict = {}
months = []
profit = []
amtchange= []
change = 0
Total = 0
MS = 0
changeavgtot= 0
x = 0

with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader) 
  for row in csvreader:
    months.append(str(row[0]))
    profit.append(str(row[1]))
    Total = Total + int(row[1])
    MS = len(months)
    if x != 0:
      change = int(row[1]) - x
      amtchange.append(change)
      changeavgtot -= change 
    x = int(row[1])
  
mydict = dict(zip(months,profit))
amont = sum(amtchange)
#print(amont)
Average = amont / len(amtchange)
#print(changeavgtot)
#print(round(Average, 2))
print(mydict.min())

print("Finacial Analysis")
print("---------------------------")
print("Total Months: " + str(len(amtchange)))
print("Total: " + str(Total)) 
print("Average Change: $" + str(round(Average, 2)))


#print(change)
#print(min(str(array[0,1])))
#print(max(array[1]))
#print(round(Average, 2))
#print(MS)
#print(Total)
#print("------------------------------------------------------------------------")
#print("There is a total of " + str(len(months)) + " months.")


  #```text
  #Financial Analysis
  #---------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```