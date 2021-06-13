from array import *

nums = array('i', [])
for i in range(0, 5):
    add_num = int(input('Enter the number : '))
    if add_num >= 10 and add_num <= 20:
        nums.append(add_num)
    else:
        print('Outside the range')
print('Thank you!')
for i in nums:
    print(i)
