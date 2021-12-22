import csv

with open("csv_file_directory.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # To skip the titles for columns
    for row in reader:
        print(row)
