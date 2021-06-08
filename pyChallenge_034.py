import math
num = int(input('1) Square \n2) Triangle\nEnter the number: '))
if num == 1:
    one_side = int(input('Enter the length of one side : '))
    squ_area = one_side ** 2
    print(squ_area)
elif num == 2:
    t_base = int(input('Enter the length of Triangle base :'))
    t_height = int(input('Enter the height of Triangle : '))
    t_area = (t_base * t_height) / 2
    print(t_area)
else:
    print('incorrect option selected')
