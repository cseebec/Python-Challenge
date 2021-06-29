#Import Dictionaries
import os
import csv

#Relative Path to budget_data
budget_csv=os.path.join('..', 'Resources', 'budget_data.csv')

#Initialize variables
net_total=0
profit_loss=[]
pl_change=[]

#Open CSV file and begin working with data
with open(budget_csv, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip Header Row
    next(csvreader)
    #Loop Through rest of rows
    for row in csvreader:
        #Calculate Total Change 
        net_total +=int(row[1])
        profit_loss.append(int(row[1]))

#Calculate the changes over the entire period
for m in range(1,len(profit_loss)):
    #print(f"Index {m}  Value {profit_loss[m]}")
    pl_change.append(profit_loss[m]-profit_loss[m-1])

print(f"Total: ${net_total}")


