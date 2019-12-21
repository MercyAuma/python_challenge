import os
import csv
import pandas as pd

#define variables

total_votes=0
uniquecandidates=0
summaryreportlist=[]

#output file

result_list = []
election_results_file = os.path.join('../Resources/Election_Results_Report.txt')

#set path to excel file
election_df = pd.read_csv("../Resources/large_election_data.csv",low_memory=False)
#print(election_df.head())

#The total number of votes cast
total_votes=election_df.Candidate.count()

#A complete list of candidates who received votes
uniquecandidates=election_df.Candidate.unique()

#Rename dataframe column 
election_df_votes=election_df[["Candidate","Voter ID"]].rename(columns={"Voter ID":"Vote"})

# group renamed columns by candidate to get vote count per candidate
election_df_votes_group=election_df_votes.groupby(['Candidate']).count().sort_values(by="Vote",ascending=False)

# Get add % of votes per candidate to data frame
election_df_votes_group['Perc_Votes'] = (election_df_votes_group["Vote"] / total_votes) * 100

# create summary report
summaryreportlist.append("Election Results")
summaryreportlist.append("-------------------------")
summaryreportlist.append("Total Votes: {total_votes}".format(total_votes=total_votes))
summaryreportlist.append("-------------------------")

for key, value in election_df_votes_group.iterrows():
    summaryreportlist.append("{candidate}: {percentage:.3f}% ({candidate_vote})"
                          .format(candidate=key, percentage=value["Perc_Votes"],
                          candidate_vote=int(value["Vote"])))

summaryreportlist.append("-------------------------")

winner_df = election_df_votes_group.loc[election_df_votes_group["Vote"] == election_df_votes_group["Vote"].max()]

for key,value in winner_df.iterrows():
    summaryreportlist.append("Winner: {winning_candidate}".format(winning_candidate=key))

summaryreportlist.append("-------------------------")

# Print output of election results
with open(file=election_results_file, mode='w') as write_results:
    for election_results in summaryreportlist:
        # Print to terminal
        print(election_results)
        # Write to file
        write_results.write("{item}\n".format(item=election_results))





       
        




