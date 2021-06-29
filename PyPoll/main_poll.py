#Import Dictionaries
import os
import csv

#Relative Path to election_data
election_csv=os.path.join('..', 'Resources', 'election_data.csv')

#Initialize variables
vote_count=0
all_votes=[]

with open(election_csv, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip Header Row
    next(csvreader)
    #Loop Through rest of rows
    for row in csvreader:
        vote_count+=1
        all_votes.append(row[2])

#Create a list of candidates by removing duplicates using set function
candidates_set=set(all_votes)
#Convert set to list 
candidates_list=list(candidates_set)

votes_per_candidate=[]
candidate_percentage=[]
#Count votes for each candidate
for num in range(len(candidates_list)):
    candidate_votes=0
    vote_percentage=0
    candidate_votes=all_votes.count(candidates_list[num])
    vote_percentage=round(candidate_votes/vote_count,2)
    votes_per_candidate.append(candidate_votes)
    candidate_percentage.append(vote_percentage*100)

#Print Statements 
#print("Election Results")
#print("------------------------")
#print(f"Total Votes: {vote_count}")
#print("------------------------")
print(list(candidates_list))
print(list(votes_per_candidate))
print(list(candidate_percentage))
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------