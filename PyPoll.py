import os
import csv

# The data we need to retrieve

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of vtes each candiate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#file_to_load = "./resources/election_results.csv"

print("get cwd ", os.getcwd())

# Initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []

#Declare an empty dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#file_to_load = "Election_Analysis/resources/election_results.csv"
file_to_load = os.path.join("Election_Analysis","resources","election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("Election_Analysis","analysis","election_analysis.txt")
#open the election file and read the file
with open(file_to_load) as election_data:

    # To do: perform analysis
    print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        #print(row[0])
        # Add to total vote count
        total_votes += 1

        # print the candiate from each row
        candidate_name = row[2]

        #If the candidate doesn't match an existing candidate..
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# save the results to our text file
with open(file_to_save,'w') as txt_file:

    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes : {total_votes:,}\n"
        f"---------------------\n"
    )

    print(election_results,end="")
    #Save the final vote count to the text file

    txt_file.write(election_results)


    #Determine the percentage of votes for each candidate by looping through the counts
    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        #calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes) *100

        #print the candidate name and percentage of votes
        candidate_results = (
            f"{candidate_name} : {vote_percentage:.1f}% ({votes:,}) \n"
            )

        print(candidate_results)
        txt_file.write(candidate_results)

        if(votes > winning_count) and (vote_percentage > winning_percentage) :
            #If true set winning count = votes and winning percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #Print the winning candidate's results in the terminal.       
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner : {winning_candidate}\n"
        f"Winning vote count : {winning_count:,}\n"
        f"Winninf Percentage : {winning_percentage:.1f}%\n"
        f"--------------------------\n"
    )

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)




