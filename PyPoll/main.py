# Module 3 Challenge: Coding for "Python-Challenge: PyPoll"

# Import Dependencies
import os
import csv

# Specify path to csv data file
election_data = os.path.join("Resources", "election_data.csv")
analysis_file = os.path.join("analysis", "PyPoll_results.txt")

# Define variables for calculating and holding values
total_votes = 0  # Start count for total number of votes
candidate_votes = {}  # Dictionary for candidate votes each candidate received
candidates = []  # List of candidates
winning_candidate = ""
winning_count = 0  # Winning count tracker

# Open and read in csv data excluding header
with open(election_data) as data:
    reader = csv.reader(data, delimiter=",")
    header = next(reader)

    # Loop to calculate votes and candidates
    for row in reader:
        total_votes = total_votes + 1  # Adds to the total vote count
        candidate_name = row[2]  # Retrieve candidate names

        # If the candidate's name is not in the list of existing candidates
        if candidate_name not in candidates:
            candidates.append(candidate_name)  # Add the name to the candidates list
            candidate_votes[candidate_name] = 0  # Track the candidate votes
        # Add vote to each candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(analysis_file, "w") as results_file:
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")

    # Print the total vote counts
    print(election_results, end="")
    results_file.write(election_results)

    # Loop to retrieve vote counts and percentages
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percent_votes = float(votes) / float(total_votes) * 100

    # Retrieve winning vote count and winning candidates   # Loop to retrieve vote counts and percentages
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
        vote_results = f"{candidate}: {percent_votes:.3f}% ({votes})\n"

    # Print Candidate Results
        print(vote_results, end="")
        results_file.write(vote_results)

    # Print the winning candidate
        winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------------------\n")

    # Print Winner
    print(winning_candidate_summary)
    results_file.write(winning_candidate_summary)

#Export analysis results to a text file
with open("PyPoll.txt", "w") as text_file:
    text_file.write(str(results_file))
