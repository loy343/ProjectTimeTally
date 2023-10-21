import time_punch
import csv


#time_punch.hours()


#add data to column

# Define the data to be added
new_age_data = [28, 33, 26]  # Add ages for new records

# Read the existing CSV data
existing_data = []
with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        existing_data.append(row)

# Modify the data by adding the new ages to the 'Age' column
for i, data_row in enumerate(existing_data):
    data_row['Age'] = new_age_data[i]

# Write the updated data back to the CSV file
with open('data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Name', 'Age']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    csv_writer.writeheader()

    # Write the modified data
    csv_writer.writerows(existing_data)

print("Data added to CSV file.")