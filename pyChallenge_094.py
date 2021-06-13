from array import *
import random
nums = array('i', [])
for i in range(0,5):
    r_num = random.randint(0, 100)
    nums.append(r_num)

for i in nums:
    print(i)
choice_num = int(input('Enter one of the numbers in the array. : '))
tryagain = True
while tryagain:
    if choice_num in nums:
        print(nums.index(choice_num))
        tryagain = False
    else:
        print('Invalid input.')
        choice_num = int(input('Enter one of the numbers in the array. : '))
