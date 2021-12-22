import re
import csv

counter = 0
with open("csv_file_directory.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name'].strip().upper()
        if re.search('search_string', name):
            counter += 1
print(f' "Search_String" appeared: {counter} times')
