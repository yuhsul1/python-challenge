import os
import csv

poll_path = os.path.join("..","..","Resrouces","election_data.csv")

vote_count = 0
candidate_list = []
candidate_vote_count = {}

winner_vote = ["",0]

with open(poll_path,"r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    for row in csv_reader:
        vote_count +=1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_vote_count[row[2]]=1
        else:
            candidate_vote_count[row[2]]+=1
    
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(vote_count))
    print("-------------------------")
    for candidate in candidate_vote_count:
        print(candidate +":"+str(round(candidate_vote_count[candidate]/vote_count*100))+"%" +" ("+str(candidate_vote_count[candidate])+")")
        if (candidate_vote_count[candidate]>winner_vote[1]):
            winner_vote[0] = candidate
            winner_vote[1] = candidate_vote_count[candidate]
       
    print("-------------------------")
    print("Winner: "+winner_vote[0])
    print("-------------------------")


poll_output = "poll_result.txt"
with open(poll_output, 'w') as textfile:
    print("Election Results",file = textfile)
    print("-------------------------",file = textfile)
    print("Total Votes " + str(vote_count),file = textfile)
    print("-------------------------",file = textfile)
    for candidate in candidate_vote_count:
        print(candidate +":"+str(round(candidate_vote_count[candidate]/vote_count*100))+"%" +" ("+str(candidate_vote_count[candidate])+")",file = textfile)
    print("-------------------------",file = textfile)
    print("Winner: "+winner_vote[0],file = textfile)
    print("-------------------------",file = textfile)
