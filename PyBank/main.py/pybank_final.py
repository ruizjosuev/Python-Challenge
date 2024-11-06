# -*- coding: UTF-8 -*-
"""PyBank Homework File."""

# Dependencies
import csv
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Path to the CSV file
file_path = '/Users/willianruiz/bootcamp/Github_HW/Python-Challenge/PyBank/Resources/budget_data.csv'
file_to_output = 'analysis/budget_analysis.txt'  # Output file path

# Define variables to track the financial data
total_months = 0
total_profit_losses = 0
previous_profit_losses = None
changes = []
dates = []

# Open the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip header row

    # Process each row
    for row in csv_reader:
        # Get the date and profit/losses for the current row
        date = row[0]
        profit_losses = int(row[1])

        # Add date to dates list
        dates.append(date)

        # Update total months and total profit/losses
        total_months += 1
        total_profit_losses += profit_losses

        # Calculate change in profit/losses if not the first row
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)
        previous_profit_losses = profit_losses

# Calculate average change, greatest increase, and greatest decrease
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find dates of greatest increase and decrease
greatest_increase_date = dates[changes.index(greatest_increase) + 1]  # Offset by 1 due to changes list being 1 shorter
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]

# Create the analysis output
analysis_output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the analysis to the console
print(analysis_output)

# Save the analysis output to a text file
with open(file_to_output, mode='w') as file:
    file.write(analysis_output)

print(f"Analysis has been saved to {file_to_output}")
