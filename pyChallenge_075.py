ran_num = [369, 789, 542, 999]
for i in ran_num:
    print(i)
choice_num = int(input('Please enter a three-digit number. : '))
if choice_num in ran_num:
    print(ran_num.index(choice_num))
else:
    print('"That is not in the list"')
