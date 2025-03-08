import os
import csv

# Input and output file locations
file_to_load = r"C:\Users\the_a\Documents\Challenges\python_challenge\PyPoll\Resources\election_data.csv"
# Output destination for election analysis
file_to_output = r"C:\Users\the_a\Documents\Challenges\python_challenge\PyPoll\Analysis\election_analysis.txt"

# Ensure the output directory is available
analysis_directory = r"C:\Users\the_a\Documents\Challenges\python_challenge\PyPoll\Analysis"
os.makedirs(analysis_directory, exist_ok=True)  # Avoids error if the directory already exists

# Initialize tracking variables for election results
vote_count = 0
candidate_votes = {}  # Stores the total votes per candidate
leading_candidate = ""
highest_vote_count = 0

# Open and process the CSV file
with open(file_to_load) as election_data:
    csv_reader = csv.reader(election_data)

    # Read and skip the header row
    header = next(csv_reader)

    # Iterate through the dataset row by row
    for row in csv_reader:
        # Increment the total number of votes
        vote_count += 1

        # Extract the candidate's name from the row
        candidate_name = row[2]

        # If this candidate is not in the dictionary, add them with an initial count of 0
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Increase the candidate's vote tally
        candidate_votes[candidate_name] += 1

# Identify the candidate with the most votes
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    if votes > highest_vote_count:
        highest_vote_count = votes
        leading_candidate = candidate

# Construct the election results summary
output_text = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {vote_count:,}\n"
    f"-------------------------\n"
)

# Append each candidate's results to the summary
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percentage_of_votes = (votes / vote_count) * 100
    output_text += f"{candidate}: {percentage_of_votes:.3f}% ({votes:,})\n"

# Include the final winner details
output_text += (
    f"-------------------------\n"
    f"Winner: {leading_candidate}\n"
    f"-------------------------\n"
)

# Display the election summary in the terminal
print(output_text)

# Save the results to a text file
with open(file_to_output, "w") as text_file:    # Open in write mode
    text_file.write(output_text)   # Store the output summary in the file
