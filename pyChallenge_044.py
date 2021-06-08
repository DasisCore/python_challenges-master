num = int(input('How many people would you like to invite to the party? : '))
if num < 10:
    for i in range(0, num):
        name = input('What your friends name? : ')
        print('"', name,'has been invited"')
else:
    print('Too many people')
