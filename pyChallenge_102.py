list = {}
count = 1
for i in range(0, 4):
    name = input('Please enter the name (%d/4) : ' %(count))
    age = int(input('Please enter your age. : '))
    shoes = int(input('Please enter your shoes size :'))
    list[name] = {'Age':age,'Shoes':shoes }
    count = count + 1
print(list)
