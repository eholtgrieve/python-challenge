#read budget_data.csv file
import os 
import csv

budget_csv = os.path.join('Resources','budget_data.csv')

#variables variables variables

total_months = 0
total_revenue = 0 
previous_revenue = 0 
greatest_increase = 0
greatest_decrease = 0 

changes_list = []
increase_month = []
decrease_month = []



   
#read thru csv
with open(budget_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csvheader = next(csvreader)
    
    for row in csvreader:
        #calculate total months in dataset
        total_months = total_months + 1
        
        #calculate net total of profit/losses over period
        revenue = int(row[1])
        total_revenue = total_revenue + revenue
        
        #calculate changes in profit/losses over period
        revenue_changes = int(row[1]) - int(previous_revenue)
        previous_revenue = int(row[1])
        changes_list = changes_list + [revenue_changes]
        
        #calculate average profit/losses change
        avg_change = round(sum(changes_list) / len(changes_list), 2)
        
        #calculate greatest increase in profits (date and amount)
        if (revenue_changes > int(greatest_increase)):
            greatest_increase = row[1]
            increase_month = row[0]
        #calculate greatest decrease in profits (date and amount)
        if (revenue_changes < int(greatest_decrease)):
            greatest_decrease = row[1]
            decrease_month = row[0]

    
#print results to terminal

analysis = (
        f"\n--Financial Analysis--\n"
        f"\n-------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total Revenue: ${total_revenue}\n"
        f"Average Change: ${avg_change}\n"
        f"Greatest Increase in Profits: {increase_month} ${greatest_increase}\n"
        f"Greatest Decrease in Profits: {decrease_month} ${greatest_decrease}\n")
print(analysis)

#export text file with results        
budget_text = os.path.join('Analysis', 'budget_text.txt')

with open(budget_text, 'w') as budget_text_file:
    
    budget_text_file.write(analysis)
