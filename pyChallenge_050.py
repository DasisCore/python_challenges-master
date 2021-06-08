num = int(input('Please enter a number between 10 and 20. : '))
while num < 10 or num > 20: # 왼쪽의 num이 True면 밑의 함수 반복, False면 끝남.
    if num < 10:
        print('Too low')
    elif num > 20:
        print('Too high')
    num = int(input("Try again enter a number : "))
print('Thank you.')
