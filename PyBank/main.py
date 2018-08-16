import os, csv

#Define csv file path
bank_csv=os.path.join('..','..','Resrouces','budget_data.csv')

#Set starting value as 0
total_month = 0
total_profit = 0
previous_profit = 0

#Set empty list value as well as beginning comparison
greatest_increase=["",0]
greatest_decrease=["",0]
profit_tracker = []


#Open CSV file
with open(bank_csv,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:

        #Total month tracker
        total_month = total_month + 1

        #Total profit tracker
        total_profit = total_profit + int(row[1])

        #define profit change
        profit_change = int(row[1])-previous_profit

        #define previous profit (keep in mind, this command execute the profit change so it doesn't override the actual previous profit value)
        previous_profit = int(row[1])

        #use profit change to compare greatest increase list, if bigger then store Date and profit change row
        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_change
        #same as above, just reverse the comparison
        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_change
        #Since the total changes should be 1 less than the toal this would remove the change form 0 to 1 month (Advice from Edward)
        if (total_month > 1):
            profit_tracker.append(profit_change)

    #define average change
    average = sum(profit_tracker)/(len(profit_tracker))

    #print all record
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: "+ str(total_month))
    print("Total: " + str(total_profit))

    #look up how to print only the 2 decimal on internet
    print("Average Change: " + "{:12.2f}".format(average))
    print("Greatest Increase in Profits "+str(greatest_increase[0])+" $ "+"("+str(greatest_increase[1])+")")
    print("Greatest Decrease in Profits "+str(greatest_decrease[0])+" $ "+"("+str(greatest_decrease[1])+")")
        
output_path = os.path.join("bank_analysis.csv")


#I used .writerow and it separate every charater into a cell, so i uses simple write
with open(output_path,"w",newline='')as analysis:
    analysis.write("Financial Analysis")
    #simple switch lane
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

