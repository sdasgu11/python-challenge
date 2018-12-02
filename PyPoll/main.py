#	The total number of votes cast
#	A complete list of candidates who received votes
#	The percentage of votes each candidate won
#	The total number of votes each candidate won
#	The winner of the election based on popular vote.

# importing libraries

import csv
verbose = False
WritetoFile = True
inputfile = "resources/election_data.csv"
outputfile = "out_election_data.txt"

# creating list to store data parsed from the file.also create a list to store the analysed data for further processing.
data_list = []
unique_candidates = []
analysis_list = []
candidates = []
counter = 0
with open(inputfile) as csv_file:
    csvreader =csv.reader(csv_file,delimiter =',')
    Removeheader = True
    for row in csvreader:
        if Removeheader:
            Removeheader = False
            continue
        data_list.append([row[0],row[1],row[2]])
        counter = counter + 1

        if verbose: print('>>> Completed CSV File Reading')
    print ('Election Results')
    print(data_list)
    print ('-------------------------')
    print ('Total Votes  : ' + str(counter))
#list of names transferred to unique_candidates
unique_candidates = [row[2] for row in data_list]
#
for x in unique_candidates:
    if x not in candidates:
        candidates.append(x)
 #   print('[%s]' % ', '.join(map(str, list_candidates)))
print("List of Candidate are " + str(candidates))

poll_results = [0] * len(candidates)

for row in data_list :

    candidate_name = row [2]

    candidate_number = candidates.index(candidate_name)

    vote_cnt = poll_results [candidate_number] + 1

    poll_results [candidate_number] = vote_cnt


vote_cnt = -99999

for i in range (len(candidates)):

    if (int(poll_results[i]) > vote_cnt ):

        winner = candidates[i]

        vote_cnt = poll_results[i]

for i in range (len(candidates)):

    percent_won = (poll_results[i] / counter) * 100

    vote_count = poll_results[i]

    analysis_list.append (candidates[i] + ': '

                     + str(percent_won) + '% ('

                     + str(vote_count) + ')')

analysis_list.append ('-------------------------')

analysis_list.append ('Winner: ' + str(winner))

analysis_list.append ('-------------------------')

#print analysis

for line in analysis_list:

    print (line)



