# -*- coding: UTF-8 -*-

# Dependencies
import csv
import os


# Files to load and output(attempted to use class example to no avail)
#file_to_load = os.path.join("Resources", "budget_data.csv")  # File path for input data
#file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # File path for the output report
# Files to load and output
file_to_load = r"PyBank\Resources\budget_data.csv"  # File path for input data
file_to_output= r"PyBank\Analysis\budget_analysis.txt" # File path for the output report

# Define variables to track the financial data
total_months = 0  # Counter for total months in dataset
month_of_change = []  # List to track month-over-month changes
net_change_list = []  # List to store changes in "Profit/Losses" between months
greatest_increase = ["", 0]  # Store month and value of greatest profit increase
greatest_decrease = ["", 9999999999999999999]  # Store month and value of greatest loss decrease
total_net = 0  # Track the total net amount of "Profit/Losses"
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])  # Add the first month's profit/loss
    prev_net = int(first_row[1])  # Store the first month's profit/loss for comparison

    # Process each row of data
    for row in reader:
# Track the total
        total_months += 1  # Increment the total month count
        total_net += int(row[1])  # Add the current month's profit/loss to the total

        # Track the net change
        net_change = int(row[1]) - prev_net  # Calculate month-over-month change
        prev_net = int(row[1])  # Update previous month's profit/loss for the next iteration
        net_change_list += [net_change]  # Add this month's change to the list
        month_of_change += [row[0]]  # Add the month to the change list

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
# Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the average net change across the months
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output (to terminal)
print(output)

# Export the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)