#Import Dictionaries
import os
import csv

#Relative Path to budget_data
budget_csv=os.path.join('..', 'Resources', 'budget_data.csv')

#Initialize variables
net_total=0
profit_loss=[]
pl_change=[]
date_list=[]

#Open CSV file and begin working with data
with open(budget_csv, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip Header Row
    next(csvreader)
    #Loop Through rest of rows
    for row in csvreader:
        #Calculate the Net Total 
        net_total +=int(row[1])
        profit_loss.append(int(row[1]))
        date_list.append(row[0])

#By definition, Sets only contain unique elements, so when the list with all dates 
# is converted to a set any duplicate date is removed.
total_months=len(set(date_list))

total_change=0
#Calculate the changes over the entire period
#Start at 1 so the first entry is the second value minus the first value
for m in range(1,len(profit_loss)):
    pl_change.append(profit_loss[m]-profit_loss[m-1])
    total_change+=profit_loss[m]-profit_loss[m-1]

#Calculate average change, max change and min change
avg_change=round(total_change/len(pl_change),2)
max_increase=max(pl_change)
min_increase=min(pl_change)

#Find the indexes of max and min increase
#Have to add 1 to the index because pl_change starts at the second index of profit_loss
mx=pl_change.index(max_increase)+1
mn=pl_change.index(min_increase)+1

#Print Statements to Terminal
print("Financial Analysis")
print("-----------------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {date_list[mx]} (${max_increase})")
print(f"Greatest Decrease in Profits: {date_list[mn]} (${min_increase})")


#YOU HAVE TO CHANGE THIS PATH BECAUSE IT IS AN ABSOLUTE PATH AND WILL ONLY WORK ON MY COMPUTER
f = open("C:/Users/Collin/Desktop/B.Upenn_Data_Analytics/D.Git_Push_Submitted_Homework_Repos/HW3/PyBank/Analysis/Results.txt", "w")
#Write Results in file
f.write("Financial Analyis\n")
f.write("----------------------------------------\n")
f.write(f"Total Months: {total_months} \n")
f.write(f"Total: ${net_total} \n")
f.write(f"Average Change: ${avg_change} \n")
f.write(f"Greatest Increase in Profits: {date_list[mx]} (${max_increase}) \n")
f.write(f"Greatest Decrease in Profits: {date_list[mn]} (${min_increase}) \n")
f.close()

