import csv
input_csv_path = 'days_of_October_23.csv'
output_csv_path = 'output.csv'
# Open the input CSV file for reading and the output CSV file for writing
with open(input_csv_path, 'r') as input_file, open(output_csv_path, 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    # Read the header row
    header = next(reader)
    
    # Write the header to the output file
    writer.writerow(header)
    
    for row in reader:
        if row[header.index('Work_Day')] == 'False':
            pass
        else: print('yo')

