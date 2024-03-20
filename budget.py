import os 
import csv 

def calculate_changes(analysis):
    changes = [int(analysis[i+1][1]) - int(analysis[i][1]) for i in range(len(analysis)-1)]
    max_increase = max(changes)
    max_increase_month = analysis[changes.index(max_increase) + 1][0]
    max_decrease = min(changes)
    max_decrease_month = analysis[changes.index(max_decrease) + 1][0]
    return max_increase, max_increase_month, max_decrease, max_decrease_month 

def format_output(max_increase, max_increase_month, max_decrease, max_decrease_month):
    output = f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n"
    output += f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n"
    return output

budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None) 

    Date_sum = 0
    Date_index = []
    analysis = []
    profits = []
    total_profit = 0
    
    for row in csvreader:
        analysis.append(row) 
        Date_value = row[0]  
        Date_sum += 1 
        profit_value = float(row[1])
        Date_index.append(Date_value)
        profits.append(profit_value)
        total_profit += profit_value

max_difference = max(profits) - min(profits)
max_increase, max_increase_month, max_decrease, max_decrease_month = calculate_changes(analysis)

output = format_output(max_increase, max_increase_month, max_decrease, max_decrease_month)

# Export results to a text file
output_file_path = "financial_analysis.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-" * 25 + "\n")
    output_file.write(f"Number of Months: {Date_sum}\n")
    output_file.write(f"Total Profit: ${total_profit}\n")
    output_file.write(f"Greatest Difference Between Rows: ${max_difference}\n")
    output_file.write(output)

print("Results exported to:", output_file_path)



