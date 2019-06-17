## PyPoll
import os 
import csv
#![Vote-Counting](Images/Vote_counting.png)
#* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
poll_csv = os.path.join('resources','election_data.csv')
#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

Vote_count = []

County =[]

Names = []
 
Named = []

tally = [0, 0, 0, 0,]

Candidate_index = int(Names)
   
tally[Candidate_index] += 1


with open(poll_csv, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)

  for row in csvreader:
    Vote_count.append(row[0])

    County.append(row[1])

    Names.append(row[2])

  #print(len(Vote_count))
  print(tally)

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