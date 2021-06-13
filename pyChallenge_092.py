from array import *
import random

nums1 = array('i', []) # 사용자가 적은 숫자 3개 담기
nums2 = array('i', []) # 임의의 숫자 5개 넣기

for i in range(0, 3):
    add_num = int(input('Enter the number : '))
    nums1.append(add_num)

for o in range(0, 5):
    r_num = random.randint(0, 100)
    nums2.append(r_num)

f_nums = array('i', [])
f_nums.extend(nums1)
f_nums.extend(nums2)
f_nums = sorted(f_nums)

for i in f_nums:
    print(i)
