from array import *
import random
nums = array('f', [])
for i in range(0, 5):
    r_nums = random.uniform(10, 100)
    nums.append(r_nums)

choice_num = int(input('Enter an integer between 2 and 5. : '))
tryagain = True
while tryagain:
    if choice_num >= 2 and choice_num <= 5:
        for i in range(0, 5):
            ans = nums[i] / choice_num
            print(round(ans, 2))
            tryagain = False
    else:
        print('Invalid input.')
        choice_num = int(input('Enter an integer between 2 and 5. : '))
