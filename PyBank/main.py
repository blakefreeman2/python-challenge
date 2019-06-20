import os

import csv
### PyBank

#![Revenue](Images/revenue-per-lead.png)

#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `months` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#* Your task is to create a Python script that analyzes the records to calculate each of the following:

  #* The total number of months included in the dataset

  #* The net total amount of "Profit/Losses" over the entire period

  #* The average of the changes in "Profit/Losses" over the entire period

  #* The greatest increase in profits (months and amount) over the entire period

  #* The greatest decrease in losses (months and amount) over the entire period

#* As an example, your analysis should look similar to the one below:
csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
profit = []
amtchange= []
minmonths = []
maxmonths = []
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
Average = amont / len(amtchange)


import numpy as np
minmonths = np.argmin(amtchange) + 1
maxmonths = np.argmax(amtchange) + 1 

print("Finacial Analysis")
print("---------------------------")
print("Total Months: " + str(len(amtchange)))
print("Total: " + str(Total)) 
print("Average Change: $" + str(round(Average, 2)))
print("Greates Increase in Profits: " + (months[maxmonths]) +" (" + str(max(amtchange)) + ")")
print("Greates Increase in Profits: " + (months[minmonths]) +" (" + str(min(amtchange)) + ")")

text_file = open("PyBank.txt","w",newline='')

text_file.write(("Finacial Analysis\n"))
text_file.write("---------------------------\n")
text_file.write("Total Months: " + str(len(amtchange)) + "\n")
text_file.write("Total: " + str(Total)+ "\n") 
text_file.write("Average Change: $" + str(round(Average, 2)) + "\n")
text_file.write("Greates Increase in Profits: " + (months[maxmonths]) +" (" + str(max(amtchange)) + ")\n")
text_file.write("Greates Increase in Profits: " + (months[minmonths]) +" (" + str(min(amtchange)) + ")\n")
text_file.close()
  #```text
  #Financial Analysis
  #---------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```