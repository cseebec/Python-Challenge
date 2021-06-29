#Import Dictionaries
import os
import csv

#Relative Path to budget_data
budget_csv=os.path.join('..', 'Resources', 'budget_data.csv')

#Initialize variables
net_total=0
profit_loss=[]
useless=0

#Open CSV file and begin working with data
with open(budget_csv, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip Header Row
    next(csvreader)
    #Loop Through rest of rows
    for row in csvreader:
        net_total +=int(row[1])

print(net_total)




