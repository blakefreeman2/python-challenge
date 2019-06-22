## PyPoll
import os 
import csv
import numpy as np
#![Vote-Counting](Images/Vote_counting.png)
#* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
poll_csv = os.path.join('resources','election_data.csv')
#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

Candidates = []




with open(poll_csv, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)

  for row in csvreader:


    Candidates.append(row[2])

Names = np.unique(Candidates)
Votes = np.array(np.unique(Candidates, return_counts=True))

Total =  len(Candidates)

Can1 = Votes[0,0]
Can2 = Votes[0,1]
Can3 = Votes[0,2]
Can4 = Votes[0,3]
Can1V = Votes[1,0]
Can2V = Votes[1,1]
Can3V = Votes[1,2]
Can4V = Votes[1,3]

PCan1V = float(Can1V) / float(Total) * 100
PCan2V = float(Can2V) / float(Total) * 100
PCan3V = float(Can3V) / float(Total) * 100
PCan4V = float(Can4V) / float(Total) * 100


print(f"{Can1}  {round(PCan1V , 2)}%  ({Can1V})")
print(f"{Can2}  {round(PCan2V , 2)}%  ({Can2V})")
print(f"{Can3}  {round(PCan3V , 2)}%  ({Can3V})")
print(f"{Can4}  {round(PCan4V , 2)}%  ({Can4V})")
  #* The total number of votes cast

  #* A complete list of candidates who received votes

  #* The percentage of votes each candidate won

  #* The total number of votes each candidate won

  #* The winner of the election based on popular vote.

#* As an example, your analysis should look similar to the one below:

  #```text
  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
  #```

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.