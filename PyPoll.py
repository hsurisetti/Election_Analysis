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


#file_to_load = "Election_Analysis/resources/election_results.csv"
file_to_load = os.path.join("Election_Analysis","resources","election_results.csv")

#open the election file and read the file

with open(file_to_load,'r') as election_data:

    # To do: perform analysis
    print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
    #   print(row[0])


file_to_save = os.path.join("Election_Analysis","analysis","election_analysis.txt")

with open(file_to_save,'w') as txt_file:

    #write some data to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("-"*40)
    txt_file.write("\n Araphoe\n Denver\n Jefferson")





