from array import *
nums = array('i', [])
for i in range(0, 5):
    newValue = int(input('Enter the number : '))
    nums.append(newValue)
nums = sorted(nums)
nums.reverse()
print(nums)
