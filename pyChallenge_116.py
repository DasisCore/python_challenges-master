import csv
file = list(csv.reader(open("Books.csv")))
booklist = []
for i in file:
    booklist.append(i)
x = 0
for i in booklist:
    display = x, booklist[x]            # booklist를 화면에 정리하여 표시.
    print(display)
    x = x + 1
num = int(input("Which row do you want to delete? : "))     # 삭제할 데이터.
del booklist[x]

x = 0
for i in booklist:
    display = x, booklist[x]        #삭제 후 데이터 표시.
    print(display)
    x = x + 1

alter = int(input("Which row do you want to change? : "))           # 바꿀부분 확인.
x = 0
for i in booklist[alter]:
    display = x, booklist[alter][x]             #바꿀 열 부분 표
    print(display)
    x = x + 1
part = int(input("Enter the part you want to change. : "))
newdata = input("Enter the new data : ")
booklist[alter][part] = newdata             #데이터 수정.
print(booklist[alter])

file = open("Books.cvs", "w")
for i in booklist:
    newrecord = i[0] + "," + row[1] + "," + row[2] + "\n"           #바꾼 데이터 입력.
    file.write(newrecord)
file.close()
