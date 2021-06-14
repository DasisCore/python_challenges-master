import csv
start_year = int(input("Enter the start year. : "))
end_year = int(input("Enter the end year. : "))

file = list(csv.reader(open('Books.csv')))
tmp = []
for row in file:
    tmp.append(row)

for row in tmp:
    if int(row[2]) >= start_year and int(row[2]) <= end_year:
        print(row)
