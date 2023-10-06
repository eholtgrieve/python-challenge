#read election_data.csv

import os 
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

#variable variables variables
total_votes = 0
winner_count = 0
total_candidate_votes = 0

percentage_votes = []
candidates_list = []
popular_vote = []


#read thru csv
with open(election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:
        #calculate total votes
        
        total_votes = total_votes + 1 
    
        #find complete list of candidates who recieved votes
        
        candidate_name = row[2]
        
        if candidate_name not in candidates_list == True:
                
                candidates_list.append(candidate_name)
            
                total_candidate_votes[candidate_name] = 0   
        
        
    for candidate_name in candidates_list:
         
        #calculate total votes for each candidate
        
        total_candidate_votes[candidate_name] = total_candidate_votes[candidate_name] + 1

        #calculate percentage of votes for each candidate
        
        percentage_votes = round(((total_candidate_votes[candidate_name]/ total_votes) * 100), 3)

        #find winner of popular vote
        if total_candidate_votes > winner_count:
            winner_count = total_candidate_votes
            popular_vote = candidate_name   

candidate_info = f"{candidate_name} : {total_candidate_votes} {percentage_votes}"


# print results to terminal 
results = (
f"\n--Election Results--\n"
f"\n-------------------------\n"
f"Total Votes: {total_votes}\n"
f"\n-------------------------\n"
f"{candidate_info}\n"
f"{candidate_info}\n"
f"{candidate_info}\n"
f"Winner: {popular_vote}\n"
f"\n-------------------------\n"
    )
print(results)

#export text file with results
results_text = os.path.join('Analysis/results_text_file.txt')

with open(results_text, 'w') as budget_text_file:
    budget_text_file.write(results)