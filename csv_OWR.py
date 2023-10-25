import csv

input_csv_path = 'days_of_October_23.csv'
output_csv_path = 'output.csv'

def process_csv(input_file_path, output_file_path, processing_function):
    """
    Opens an input CSV file, applies a process function to each row, and writes the result to an output CSV file.

    :param input_file_path: The path to the input CSV file.
    :param output_file_path: The path to the output CSV file.
    :param process_function: A function that processes a row and returns a modified row.
    """
    with open(input_file_path, 'r', newline='') as input_file, open(output_file_path, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            processed_row = processing_function(row)
            print(processed_row)

# # Example process function that adds "Processed" to the end of each row
# def add_processed_to_row(row):
#     return row + ["Processed"]

# Usage of the process_csv function
input_file_path = 'input.csv'
output_file_path = 'output.csv'
def processing_function(row):
    processed_row = row
    return processed_row

process_csv(input_csv_path,output_csv_path, processing_function)

