sample_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
choice_num1 = int(input('Select a row : '))
print(sample_list[choice_num1])
newValue = int(input('Please enter a new value. : '))
sample_list[choice_num1].append(newValue)
print(sample_list[choice_num1])
