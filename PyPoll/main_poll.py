#Import Dictionaries
import os
import csv

#Relative Path to election_data
election_csv=os.path.join('..', 'Resources', 'election_data.csv')

with open(election_csv, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')