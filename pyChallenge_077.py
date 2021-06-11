invite = []
invite.append(input('Who will you invite to the party? (1/3) : '))
invite.append(input('Who will you invite to the party? (2/3) : '))
invite.append(input('Who will you invite to the party? (3/3) : '))
answer = str(input('Do you have someone to invite? (y/n) : '))
def invited():
    global answer
    if answer == 'y' or answer == 'n':
        while answer == 'y':
            invite.append(input('Enter the name of the person you want to invite. : '))
            answer = input('Do you have someone to invite? (y/n) : ')
    else:
        print("Please enter it correctly. (y/n)")
        answer = str(input('Do you have someone to invite? (y/n) : '))
        invited()
invited()
print(invite)
choice = input('Enter one of the names in the list. : ')
print('The index of the name is',invite.index(choice))
decision = input('Are you sure you want to invite that person? (y/n) : ')

def de_cide():
    if decision == 'y':
        print(invite)
    elif decision == 'n':
        del invite[invite.index(choice)]
        print(invite)
    else:
        print('Invalid input.')
        decide()
de_cide()

# print('The number of people invited ',len(invite))
