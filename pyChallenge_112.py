import csv
file = open("Books.csv" ,"a")
book = input("Enter the book name. : ")
writer = input("Enter the writer name. : ")
year = input("Please enter the year of release. : ")
newvalue = book + "," + writer + "," + year + "\n"
file.write(newvalue)
file.close()
