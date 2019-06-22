## PyPoll
import os 
import csv
import numpy as np

poll_csv = os.path.join('resources','election_data.csv')

Candidates = []

with open(poll_csv, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)

  for row in csvreader:
    Candidates.append(row[2])

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

winner = max(set(Candidates),key=Candidates.count)


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total))
print("-------------------------")
print(f"{Can1}  {round(PCan1V , 2)}%  ({Can1V})")
print(f"{Can2}  {round(PCan2V , 2)}%  ({Can2V})")
print(f"{Can3}  {round(PCan3V , 2)}%  ({Can3V})")
print(f"{Can4}  {round(PCan4V , 2)}%  ({Can4V})")
print("-------------------------")
print("Winner: " +  winner)
print("-------------------------")


text_file = open("PyPoll.txt","w",newline='')

text_file.write("Election Results\n")
text_file.write("-------------------------\n")
text_file.write("Total Votes: " + str(Total)  +"\n")
text_file.write("-------------------------\n")
text_file.write(f"{Can1}  {round(PCan1V , 2)}%  ({Can1V})\n")
text_file.write(f"{Can2}  {round(PCan2V , 2)}%  ({Can2V})\n")
text_file.write(f"{Can3}  {round(PCan3V , 2)}%  ({Can3V})\n")
text_file.write(f"{Can4}  {round(PCan4V , 2)}%  ({Can4V})\n")
text_file.write("-------------------------\n")
text_file.write("Winner: " +  winner + "\n")
text_file.write("-------------------------\n")
text_file.close()
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