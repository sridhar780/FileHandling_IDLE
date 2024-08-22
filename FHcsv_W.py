import csv

# Data to be written to the CSV file
data1 = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago']
]

# Open the CSV file for writing
with open('output.csv', mode='w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)
    
    # Write the data to the CSV file
    csv_writer.writerows(data1)
