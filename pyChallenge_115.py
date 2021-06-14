import csv
file = open("Books.csv", "r")
x = 0
for i in file:
    display = "row " + str(x) + " - " + i
    print(display)
    x = x + 1
