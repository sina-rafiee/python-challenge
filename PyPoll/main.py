#import Modules
import os
import csv
candidatevotes = {}

#set path for file
csvpath = os.path.join('Resources', 'election_data.csv')
#open the csv file
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #read the header row first
    csvheader = next(csvreader)
    #print(csvheader)
    
    #read each row of data
    rowcount = []
    
    for row in csvreader:
        rowcount.append(row[0])
        voter = (str(len(rowcount)))
        if row[2] not in candidatevotes:
            candidatevotes[row[2]] = 1
        else:
            candidatevotes[row[2]] += 1

          





print("election results")
print("Total Votes: {}".format(voter))
for candidate, votes in candidatevotes.items():
    percentvotes = round((votes/int(voter)*100), 3)
    print("{}: {}%  ({})".format(candidate, percentvotes, votes))
winner = max(candidatevotes, key=candidatevotes.get)
print("winner:  {}".format(winner))

f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("Total Votes: {}".format(voter))
f.write('\n')
for candidate, votes in candidatevotes.items():
    percentvotes = round((votes/int(voter)*100), 3)
    f.write("{}: {}%  ({})".format(candidate, percentvotes, votes))
    f.write('\n')
f.write("winner:  {}".format(winner))
    
    

       










