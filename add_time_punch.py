import csv
#from csv_OWR import process_csv
from time_punch import hours
#finds missing data in csv and replace



# Specify the input and output CSV file paths
input_csv_path = 'days_of_October_23.csv'
output_csv_path = 'output.csv'

# Specify the name of the column to check and update
#['Day', 'Day_of_Week', 'Start', 'End', 'Hours']
day_column = 'Day'
dow_column = 'Day_of_Week'
start_column = 'Start'
end_column = 'End'
hour_column = 'Hours'
work_day = 'Work_Day'

#dummy Data
# time_punch = {
# "month": '10',
# "day": '13',
# "Day_of_week": 'Friday',
# "start": '12:12',
# "end": '13:12',
# "hours": '1'
# }

# Open the input CSV file for reading and the output CSV file for writing
with open(input_csv_path, 'r') as input_file, open(output_csv_path, 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    # Read the header row
    header = next(reader)
    
    # Write the header to the output file
    writer.writerow(header)
    

    #V1 Find missing values in the target column and data
    # for row in reader:
    #     if row[header.index('Work_Day')] == 'False':
    #         pass #skips off days
    #     elif row[header.index(day_column)] == time_punch['day'] and row[header.index(dow_column)] == time_punch['Day_of_week']:
    #         print(row)
    #         row[header.index(start_column)] = time_punch['start']
    #         row[header.index(end_column)] = time_punch['end']
    #         row[header.index(hour_column)] = time_punch['hours']
    #     else: print('Wrong day')
    #     writer.writerow(row)

    #V2
    for row in reader:
        time_punch = {}
        day = row[header.index(day_column)]
        dow = row[header.index(dow_column)]
        if row[header.index('Work_Day')] == 'False':
            pass #skips off days
        elif row[header.index(start_column)] == 'initiate':
            print(row)
            time_punch = hours(day, dow)
            row[header.index(start_column)] = time_punch['start']
            row[header.index(end_column)] = time_punch['end']
            row[header.index(hour_column)] = time_punch['hours']
            writer.writerow(row)
        else: print('Wrong day')
        #writer.writerow(row)

            


print("CSV processing complete.")
