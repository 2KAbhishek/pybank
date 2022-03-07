import pandas as pd
from pathlib import Path

# Read in the data from the csv file
budget_csv = Path("data/budget_data.csv")
df = pd.read_csv(budget_csv)

# Count the number of rows in the dataframe
num_rows = df.shape[0]

# Sum the total profit/losses
total_profit = df["Profit/Losses"].sum()

# Average of the changes in profit/losses over the entire period
change_over_period = df["Profit/Losses"].diff()
avg_change = round(change_over_period.mean(), 2)

# Greatest increase in profits (date and amount) over the entire period
greatest_increase = df["Profit/Losses"].max()
condition = df["Profit/Losses"] == greatest_increase
index = df[condition].index.tolist()
greatest_increase_date = df.loc[index[0], "Date"]
previous_month_profit = df.loc[index[0] - 1, "Profit/Losses"]
greatest_increase += abs(previous_month_profit)

# Greatest decrease in profits (date and amount) over the entire period
greatest_decrease = df["Profit/Losses"].min()
condition = df["Profit/Losses"] == greatest_decrease
index = df[condition].index.tolist()
greatest_decrease_date = df.loc[index[0], "Date"]
previous_month_profit = df.loc[index[0] - 1, "Profit/Losses"]
greatest_decrease -= abs(previous_month_profit)

# Export a text file with the results
report_path = Path("gen/report.txt")
with open(report_path, "w") as report_file:
    report_file.write("Financial Analysis\n")
    report_file.write("----------------------------\n")
    report_file.write(f'Total Months: {num_rows}\n')
    report_file.write(f'Total: ${total_profit}\n')
    report_file.write(f'Average Change: ${avg_change}\n')
    report_file.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
    report_file.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')
