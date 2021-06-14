sample_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row_num = int(input('Enter the line to be printed. (0~3) : '))
print(sample_list[row_num])
col_num = int(input('Enter the column to be printed. (0~2): '))
print(sample_list[row_num][col_num])
def reset():
    select = input('Are you sure you want to change the value? (y/n) : ')
    if select == 'y':
        change_num = int(input('Enter the number you want to change. : '))
        sample_list[row_num][col_num] = change_num
        print(sample_list[row_num])
    elif select == 'n':
        print(sample_list[row_num])
    else:
        print('Invalid input')
        reset()
reset()
