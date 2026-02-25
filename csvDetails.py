import csv

"""
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']

]

with open('userInfo.csv', 'w') as file:
        csv_file = csv.writer(file)
        csv_file.writerows(data)
        print("CSV file created successfully.")

"""



#  Reading CSV file
with open('userInfo.csv', 'r') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        print(row)