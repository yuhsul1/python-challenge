import os, csv

bank_csv=os.path.join('..','..','Resrouces','budget_data.csv')

total_month = 0
total_profit = 0
previous_profit = 0

greatest_increase=["",0]
greatest_decrease=["",0]
profit_tracker = []



with open(bank_csv,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:

        total_month = total_month + 1
        total_profit = total_profit + int(row[1])
        profit_change = int(row[1])-previous_profit
        previous_profit = int(row[1])

        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_change
        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_change
        if (total_month > 1):
            profit_tracker.append(profit_change)

    average = sum(profit_tracker)/(len(profit_tracker))

    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: "+ str(total_month))
    print("Total: " + str(total_profit))
    print("Average Change: " + "{:12.2f}".format(average))
    print("Greatest Increase in Profits "+str(greatest_increase[0])+" $ "+"("+str(greatest_increase[1])+")")
    print("Greatest Decrease in Profits "+str(greatest_decrease[0])+" $ "+"("+str(greatest_decrease[1])+")")
        
output_path = os.path.join("bank_analysis.csv")

with open(output_path,"w",newline='')as analysis:
    analysis.write("Financial Analysis")
    analysis.write("\n")
    analysis.write("-------------------------")
    analysis.write("\n")
    analysis.write("Total Months: "+ str(total_month))
    analysis.write("\n")
    analysis.write("Total: " + str(total_profit))
    analysis.write("\n")
    analysis.write("Average Change: " + "{:12.2f}".format(average))
    analysis.write("\n")
    analysis.write("Greatest Increase in Profits "+str(greatest_increase[0])+" $ "+"("+str(greatest_increase[1])+")")
    analysis.write("\n")
    analysis.write("Greatest Decrease in Profits "+str(greatest_decrease[0])+" $ "+"("+str(greatest_decrease[1])+")")

