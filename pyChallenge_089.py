from array import *
import random
nums = array('i', [])
for i in range(0, 5):
    r_num = random.randint(0, 100)
    nums.append(r_num)
for i in nums:
    print(i)
