compnum = 50
count = 1
num = int(input('Enter a number : '))
while num != compnum :
    count = count + 1
    if num < compnum:
        print('The input value is less than the correct answer.')
    else:
        print('The input value is greater than the correct answer.')
    num = int(input('Enter the number again : '))
print("Well done, you took ", count, 'attempts"')
