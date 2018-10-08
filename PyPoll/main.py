import os
import csv

file_to_read = os.path.join("data", "election_data.csv")
file_to_write_to = os.path.join('analysis', 'election_analysis.txt')

total_votes = 0
candidate_info = {}
winner_votes = 0
winner = ''

with open(file_to_read, newline='') as file_obj:

    # read csv file
    file_data = csv.reader(file_obj)

    # read / skip the header
    file_header = next(file_data)

    for row in file_data:

        # store data from file
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        # get number of votes cast
        total_votes = total_votes + 1

        # add unique candidate to dictionary
        if candidate not in candidate_info:
            candidate_info[candidate] = {'votes': 1}

        # add vote to respective candidate obj
        else:
            candidate_info[candidate]['votes'] = candidate_info[candidate]['votes'] + 1

with open(file_to_write_to, 'w') as text_file:

    total_votes_summary = (
        '\nElection Results\n'
        '--------------------\n'
        f'Total Votes: {total_votes}\n'
        '--------------------\n'
    )

    # print and export total votes
    print(total_votes_summary.rstrip())
    text_file.write(total_votes_summary)

    # get the total number and percentage of votes each candidate received
    for candidate in candidate_info:
        candidate_votes = candidate_info[candidate]["votes"]
        candidate_percentage = (candidate_info[candidate]["votes"] / total_votes) * 100
        candidate_summary = f'{candidate}:  {candidate_percentage:.3f}% ({candidate_votes})\n'

        # print and export candidate vote summary
        print(candidate_summary.strip())
        text_file.write(candidate_summary)

        # get the winning candidate based on popular vote
        if (candidate_votes > winner_votes):
            winner_votes = candidate_votes
            winner = candidate

    winner_summary = (
        '--------------------\n'
        f'Winner: {winner}\n'
        '--------------------\n'
    )

    # print and export the winner of the election
    print(winner_summary)
    text_file.write(winner_summary)



