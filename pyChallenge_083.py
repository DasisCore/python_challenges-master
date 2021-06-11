msg = input('Please enter your message in capital letters. : ')
tryagain = True
while tryagain == True:
    if msg.isupper():
        print(msg)
        print('Great!')
        tryagain = False
    else:
        msg = input('Please re-enter. : ')
