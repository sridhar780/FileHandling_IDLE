import csv

# Open the CSV file for reading
with open('data.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        print(row)
