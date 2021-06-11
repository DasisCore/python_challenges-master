nums = []
nums.append(int(input('Please enter a number.(1/3) : ')))
nums.append(int(input('Please enter a number.(2/3) : ')))
nums.append(int(input('Please enter a number.(3/3) : ')))
def desi():
    decision = input('Do you want to save the last number? (y/n) : ')
    if decision == 'n':
        del nums[2]
        print(nums)
    elif decision == 'y':
        print(nums)
    else:
        print('Invalid input.')
        decision = input('Do you want to save the last number? (y/n) : ')
        desi()
desi()
