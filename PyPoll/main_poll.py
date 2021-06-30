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
    #Read in header row
    csv_header=next(csvreader)
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
#Count votes for each candidate and calculate percentage of votes
for num in range(len(candidates_list)):
    candidate_votes=0
    vote_percentage=0
    candidate_votes=all_votes.count(candidates_list[num])
    vote_percentage=round((candidate_votes/vote_count)*100,4)
    votes_per_candidate.append(candidate_votes)
    candidate_percentage.append(vote_percentage)

#Create new columns and organize them so they are sorted from the candidate with the most votes 
#to the candidate with the fewest votes. Making sure that the information across lists still matches
candidate_in_order=[]
num_votes_in_order=[]
percentage_in_order=[]
for ranking in range(len(candidates_list)):
    most_votes=0
    most_votes=max(votes_per_candidate)
    indexwinner=votes_per_candidate.index(most_votes)
    num_votes_in_order.append(votes_per_candidate.pop(indexwinner))
    candidate_in_order.append(candidates_list.pop(indexwinner))
    percentage_in_order.append(candidate_percentage.pop(indexwinner))

#Print Statements in terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {vote_count}")
print("------------------------")
#A for loop is needed here because if we hard code the number of candidates we may be wrong 
#so be looping through the list we know we have the number of candidates correct
for position in range(len(candidate_in_order)):
    print(f"{candidate_in_order[position]} {percentage_in_order[position]}% ({num_votes_in_order[position]})")
print("------------------------")
#The candidate that comes first in this list is always going to be the winner because the list is sorted
#from most votes to least votes
print(f"Winner: {candidate_in_order[0]}")

#Print same statements to a .txt file
#YOU HAVE TO CHANGE THIS PATH BECAUSE IT IS AN ABSOLUTE PATH AND WILL ONLY WORK ON MY COMPUTER
f = open("C:/Users/Collin/Desktop/B.Upenn_Data_Analytics/D.Git_Push_Submitted_Homework_Repos/HW3/PyPoll/Analysis/Results.txt", "w")
#Write Results in file
f.write("Election Results\n")
f.write("------------------------\n")
f.write(f"Total Votes: {vote_count}\n")
f.write("------------------------\n")
for position in range(len(candidate_in_order)):
    f.write(f"{candidate_in_order[position]} {percentage_in_order[position]}% ({num_votes_in_order[position]})\n")
f.write("------------------------\n")
f.write(f"Winner: {candidate_in_order[0]}\n")
