import csv
import os 

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    months = 0
    total = 0
    greatProfit = 0
    newGreatProfit = 0
    dateGreatProfit = 0
    greatLoss = 0
    newGreatLoss = 0
    dateGreatLoss = 0

    for row in csvreader:
        months += 1
        total += int(row[1])
        average = int(total / months)
        greatProfit = int(row[1])
        greatLoss = int(row[1])
        if greatProfit > newGreatProfit:
            newGreatProfit = greatProfit
            dateGreatProfit = row[0]
        if greatLoss < newGreatLoss:
            newGreatLoss = greatLoss
            dateGreatLoss = row[0]    

text_analysis = open("text_analysis.txt", "w+")
text_analysis.write(
        f"Financial Analysis\n"
        f"-------------------------------\n"
        f"Total months: {str(months)}\n"
        f"Total: $ {str(total)}\n"
        f"Average Change: $ {str(average)}\n"
        f"Greatest Increase In Profits: {str(dateGreatProfit)} gained $ {str(newGreatProfit)}\n"
        f"Greatest Decrease In Profits: {str(dateGreatLoss)} lost $ {str(newGreatLoss)}\n" 
    )
text_analysis.close()

text = "text_analysis.txt"
with open(text, "r") as text:
    lines = text.read()
    print(lines)



