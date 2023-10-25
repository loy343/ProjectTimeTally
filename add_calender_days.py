import calendar
import csv
from datetime import datetime

# Get the current year and month
current_date = datetime.now()
year = current_date.year
month = current_date.month

# Create a list of day numbers and their corresponding day names
days_in_month = [
    (day, calendar.day_name[calendar.weekday(year, month, day)])
    for day in range(1, calendar.monthrange(year, month)[1] + 1)
]

# Define the output CSV file
output_file = f'days_of_{current_date.strftime("%B")}_{current_date.strftime("%y")}.csv'

# Write the data to a CSV file
with open(output_file, 'w', newline='') as csvfile:
    
    def off_day(dow):
        if dow == 'Sunday' or dow == 'Monday':
            return 'False'
        else: return 'True'

    csvwriter = csv.writer(csvfile)
    
    # Write the CSV header
    csvwriter.writerow(['Day', 'Day_of_Week','Start', "End", 'Hours', 'Work_Day'])
    
    # Write the day and day of the week for each day in the month
    for day, day_of_week in days_in_month:
        csvwriter.writerow([day, day_of_week,"initiate","finish","time",off_day(day_of_week)])

print(f"CSV file '{output_file}' created with days and their corresponding day of the week for the current month.")
