invite = []
invite.append(input('Who will you invite to the party? (1/3) : '))
invite.append(input('Who will you invite to the party? (2/3) : '))
invite.append(input('Who will you invite to the party? (3/3) : '))
answer = input('Do you have someone to invite? (y/n) : ')
while answer == 'y':
    invite.append(input('Enter the name of the person you want to invite. : '))
    answer = input('Do you have someone to invite? (y/n) : ')
print(invite)
print('The number of people invited ',len(invite))
