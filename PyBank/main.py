import os
import csv

file_to_read = os.path.join('data', 'budget_data.csv')
file_to_write_to = os.path.join('analysis', 'budget_analysis.txt')

total_net_change = 0
greatest_net_increase_month = ''
greatest_net_increase = 0
greatest_net_decrease_month = ''
greatest_net_decrease = 99999999999999

# open csv file
with open(file_to_read, newline='') as file_obj:

    # read csv file
    file_data = csv.reader(file_obj)

    # read / skip the header
    file_header = next(file_data)

    #read first row
    first_row = next(file_data)
    prev_net = int(first_row[1])
    total_months = 1
    total_net = int(first_row[1])

    for row in file_data:

        # get data from file
        month = row[0]
        month_net = int(row[1])

        # get totals
        total_months = total_months + 1
        total_net = total_net + month_net

        # get net change
        net_change = month_net - prev_net
        prev_net = month_net
        total_net_change = total_net_change + net_change

        # get the greatest increase
        if (net_change > greatest_net_increase):
            greatest_net_increase_month = month
            greatest_net_increase = net_change

        # get the greatest decrease
        if (net_change < greatest_net_decrease):
            greatest_net_decrease_month = month
            greatest_net_decrease = net_change

    # get average net change
    average_net_change = total_net_change / (total_months - 1)

with open(file_to_write_to, "w") as txt_file:

    summary = (
        '\nFinancial Analysis\n'
        '-------------------\n'
        f'Total: ${total_net}\n'
        f'Total Months: {total_months}\n'
        f'Average Change: ${average_net_change:.2f}\n'
        f'Greatest Increase in Profits: {greatest_net_increase_month} (${greatest_net_increase})\n'
        f'Greatest Decrease in Profits: {greatest_net_decrease_month} (${greatest_net_decrease})\n')

    #print results to terminal
    print(summary)

    #export results to file
    txt_file.write(summary)


