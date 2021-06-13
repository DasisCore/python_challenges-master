from array import *
nums = array('i', [])
for i in range(0, 5):
    add_num = int(input('Enter the number : '))
    nums.append(add_num)
nums = sorted(nums)

for i in nums:
    print(i)

array_num = int(input('Enter one of the numbers in the array. : '))
if array_num in nums:
    nums.remove(array_num)
else:
    print('Invalid input.')

for i in nums:
    print(i)
