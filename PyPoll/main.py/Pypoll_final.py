# -*- coding: UTF-8 -*-
"""PyPoll Homework File."""

import csv
import os

# Set the current working directory to the script's location
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Define the path to your election data file and output file
file_path = '/Users/willianruiz/bootcamp/Github_HW/Python-Challenge/PyPoll/Resources/election_data.csv'
file_to_output = 'analysis/election_results.txt'

# Initialize a dictionary to hold candidate vote counts
candidate_votes = {}

# Initialize the total vote counter
total_votes = 0

# Open and read the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    
    # Count votes for each candidate
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Construct the election results as a string
analysis_output = "Election Results\n"
analysis_output += "-------------------------\n"
analysis_output += f"Total Votes: {total_votes}\n"
analysis_output += "-------------------------\n"

# Determine the winner and calculate percentages
winner = ""
winning_votes = 0

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    analysis_output += f"{candidate}: {percentage:.3f}% ({votes})\n"
    
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes

analysis_output += "-------------------------\n"
analysis_output += f"Winner: {winner}\n"
analysis_output += "-------------------------\n"

# Print the analysis to the console
print(analysis_output)

# Save the analysis output to a text file
with open(file_to_output, mode='w') as file:
    file.write(analysis_output)

print(f"Analysis has been saved to {file_to_output}")
