#Import Dictionaries
import os
import csv

#Relative Path to election_data
election_csv=os.path.join('..', 'Resources', 'election_data.csv')

#Initialize variables
vote_count=0

with open(election_csv, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip Header Row
    next(csvreader)
    #Loop Through rest of rows
    for row in csvreader:
        vote_count+=1

print(vote_count)