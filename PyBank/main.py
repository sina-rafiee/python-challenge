#import Modules
import os
import csv
import statistics
rowlist = []

#set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')
#open the csv file
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #read the header row first
    csvheader = next(csvreader)
    #print(csvheader)
    
    #read each row of data
    rowcount = []
    change = []
    month_change = []
    total = 0.0
    greatest_increase = 0
    greatest_decrease = 0
    increase_month = ''
    decrease_month = ''
    for row in csvreader:
        rowcount.append(row[0])
        months = (str(len(rowcount)))
        total = total + int(row[1])
        change.append(int(row[1]))
        if int(row[1]) > greatest_increase:
            increase_month = (row[0])
            greatest_increase = (int(row[1]))
        elif int(row[1]) < greatest_decrease:
            decrease_month = (row[0])
            greatest_decrease = int(row[1])    

for i in range(len(change)-1):
    monthlychange = (change[i+1] - change[i])
    month_change.append(monthlychange)
    average_change = statistics.mean(month_change)




print("Total months: {}".format(months))
print("Total: ${}".format(int(total)))
print("Average change: ${}".format(round(average_change, 2)))
print("Greatest Increase in Profits: {}  ${}".format(increase_month, greatest_increase))
print("Greatest Decrease in Profits: {}  ${}".format(decrease_month, greatest_decrease))
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("\n")
f.write("Total months: {}".format(months))
f.write("\n")

f.write("Total: ${}".format(int(total)))
f.write("\n")

f.write("Average change: ${}".format(round(average_change, 2)))
f.write("\n")

f.write("Greatest Increase in Profits: {}  ${}".format(increase_month, greatest_increase))
f.write("\n")

f.write("Greatest Decrease in Profits: {}  ${}".format(decrease_month, greatest_decrease))


 
 
    #rowcount = sum(1 for row in csvreader)
    #print("total months: {}".format(rowcount))     
    #total = 0.0
    #for row1 in csvreader:
        #total = total + int(row1[1])
        #print("total months: {}".format(rowcount))
        #print("Total: ${}".format(total))
    
    

       










