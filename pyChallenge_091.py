from array import *
nums = array('i', [1, 1, 3, 5, 7])
for i in nums:
    print(i)
choice_num = int(input('Enter one of the numbers in the array. : '))
print(nums.count(choice_num))
