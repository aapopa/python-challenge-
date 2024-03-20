import os
import csv

def read_election_data(file_path):
    #code obtained with assistance from chatgpt and from peer help. 
    data = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Skip the header row

        for row in csvreader:
            data.append(row[2])  
    return data

def calculate_election_results(data):
    candidates = {}
    total_votes = len(data)

    for candidate in data:
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

    winner = max(candidates, key=candidates.get)
    results = {candidate: (votes / total_votes * 100, votes) for candidate, votes in candidates.items()}
    return total_votes, results, winner

def format_output(total_votes, results, winner):
    output = f"Election Results\n{'-' * 25}\n"
    output += f"Total Votes: {total_votes}\n"
    output += f"Winner: {winner}\n"
    output += "-" * 25 + "\n"

    for candidate, (percentage, votes) in results.items():
        output += f"{candidate}: {percentage:.3f}% ({votes})\n"

    return output

def export_results_to_file(output, file_path):
    with open(file_path, 'w') as textfile:
        textfile.write(output)

# Path to the CSV file
election_data_csv = os.path.join("election_data.csv")

# Read election data from CSV
election_data = read_election_data(election_data_csv)

# Calculate election results
total_votes, results, winner = calculate_election_results(election_data)

# Format of the results
output = format_output(total_votes, results, winner)


output_file_path = "election_results.txt"
export_results_to_file(output, output_file_path)

print("Results exported to:", output_file_path)
