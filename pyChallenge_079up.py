nums = []
count = 0
while count < 3:
    en_num = int(input('Please enter a number.(%d/3) : ' %(count+1)))
    nums.append(en_num)
    count = count + 1
    if count == 3:
        answer = input('Do you want to save the last number? (y/n) : ')
        def decision():
            global answer
            if answer == 'y':
                print(nums)
            elif answer == 'n':
                del nums[2]
                print(nums)
            else:
                print('Invalid input.')
                answer = input('Do you want to save the last number? (y/n) : ')
                decision()
decision()
