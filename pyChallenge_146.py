# selection = int(input("Enter your selection : "))
shiftcode = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
print(shiftcode[0])
def get_data():
    message = input("Please enter your message : ")
    message = message.lower()
    num = int(input("How much do you want to shift? (1 ~ 26): "))
    while num > 26 or num == 0:
        num = int(input("How much do you want to shift? (1 ~ 26): "))
    data = (message, num)
    return(data)

def make_code(message, num):
    new_cord = ""
    for x in message:
        y = shiftcode.index(x)
        y = y + num
        if y > 26:
            y = y - 27
        char = shiftcode[y]
        new_cord = new_cord + char
    print(new_cord)
    print()

def decode(message, num):
    new_cord = ""
    for x in message:
        y = shiftcode.index(x)
        y = y - num
        if y < 0:
            y = y + 27
        char = shiftcode[y]
        new_cord = new_cord + char
    print(new_cord)
    print()

def main():
    tryagain = True
    while tryagain:
        print("1) Make a code")
        print("2) Decode a message")
        print("3) Quit")
        print()
        select = input("Enter the number : ")
        if select == "1":
            (message, num) = get_data()
            make_code(message, num)
        elif select == "2":
            (message, num) = get_data()
            decode(message, num)
        elif select == "3":
            tryagain = False
        else:
            print("Invaild input")
main()
