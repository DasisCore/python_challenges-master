import csv
file = open("Books.csv" ,"a")
nums = int(input("How many books do you want to add? : "))
for i in range(0, nums):
    book = input("Enter the book name. : ")
    writer = input("Enter the writer name. : ")
    year = input("Please enter the year of release. : ")
    newvalue = book + "," + writer + "," + year + "\n"
    file.write(newvalue)
file.close()

file = open("Books.csv" ,"r")
search = input("Enter the name of the writer to search for. : ")
for row in file:
    if search in str(row):
        print(row)
file.close()
