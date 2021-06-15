def ask_num():
    num = int(input("Enter the number : "))
    return num

def count(num):
    n = 1
    while n <= num:
        print(n)
        n = n + 1

def main():
    num = ask_num()
    count(num)

main()
