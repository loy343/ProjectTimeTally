import csv


# Open the CSV file for reading
with open('days_of_November_23.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)



    # Skip the header row if needed
    #next(csv_reader)

    csv_data = [data for data in csv_reader]


    #Start column
    for start_column in csv_data:
        for i, cell in enumerate(start_column):
            start_column[i] = cell.replace('initiate','start')
         

    # #END column
    for end_column in csv_data:
        for i, cell in enumerate(end_column):
            end_column[i] = cell.replace('finish','end')


    # #Hour column
    for hour_column in csv_data:
        for i, cell in enumerate(hour_column):
            hour_column[i] = cell.replace('time','hour')

    with open('days_of_October_23.csv', "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_data)


    print(csv_data)