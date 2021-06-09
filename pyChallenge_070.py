nation = ("Korea", "USA", "Japen", "Russia", "China")
print(nation)
n_nation = input('Please enter one of the above countries. : ')
print('The index number of the entered country is number', nation.index(n_nation))
# 밑으로 추가된 부분.
num = int(input('Enter the number(0~4) : '))
print(nation[num])
