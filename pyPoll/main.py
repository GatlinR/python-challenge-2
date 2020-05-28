import csv
import os 

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    total = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    khan_perc = 0
    correy_perc = 0
    li_perc = 0
    otooley_perc = 0

    for row in csvreader:
        total += 1
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1

    khan_perc = khan / total * 100
    correy_perc = correy / total * 100
    li_perc = li / total * 100
    otooley_perc = otooley / total *100

    winner = max([khan, correy, li, otooley])
    if winner == khan:
        winner = "Khan"
    elif winner == correy:
        winner = "Correy"
    elif winner == li:
        winner = "Li"
    else:
        winner = "O'Tooley"

text_analysis = open("text_analysis.txt", "w+")
text_analysis.write(
        f"Election Results\n"
        f"--------------------------------\n"
        f"Total votes: {str(total)}\n"
        f"--------------------------------\n"
        f"Khan: {int(khan_perc)} % ({str(khan)})\n"
        f"Correy: {int(correy_perc)} % ({str(correy)})\n"
        f"Li: {int(li_perc)} % ({str(li)})\n"
        f"O'Tooley: {int(otooley_perc)} % ({str(otooley)})\n"
        f"--------------------------------\n"
        f"Winner: {str(winner)}\n"
        f"--------------------------------\n"
)
text_analysis.close()

text = "text_analysis.txt"
with open(text, "r") as text:
    lines = text.read()
    print(lines)

