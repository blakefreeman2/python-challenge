total = 0
rownum= 0
changeavgtot= 0

months= []
profit= []
amtchange= []

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
   csvreader= csv.reader(csvfile, delimiter=',')
   print(csvreader)
   csv_header = next(csvreader)

   for row in csvreader:
       months.append(row[0])
       profit.append(row[1])
       total = total + int(row[1])
       change = int(profit[rownum]) - int(profit[rownum - 1])
       amtchange.append(change + 1)
       changeavgtot += change
       rownum += 1

avgchange = changeavgtot / len(amtchange)