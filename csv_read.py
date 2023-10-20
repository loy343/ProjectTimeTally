import csv

# Open the CSV file for reading
with open('days_of_October_23.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row if needed
    next(csv_reader)

    # Read and process each row
    for row in csv_reader:
        Day, Day_of_Week, Hours = row
        print(f"Day: {Day}, DayOfWeek: {Day_of_Week}, Hours: {Hours}")

    print(row)