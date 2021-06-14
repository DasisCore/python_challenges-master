list = {}
count = 1
for i in range(0, 4):
    name = input('Please enter the name (%d/4) : ' %(count))
    age = int(input('Please enter your age. : '))
    shoes = int(input('Please enter your shoes size :'))
    list[name] = {'Age':age,'Shoes':shoes }
    count = count + 1
del_name = input('Enter the name of the person you want to remove. :')
del list[del_name]
for i in list:
    print(i)
