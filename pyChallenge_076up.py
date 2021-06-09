<<<<<<< HEAD
invite = []
invite.append(input('Who will you invite to the party? (1/3) : '))
invite.append(input('Who will you invite to the party? (2/3) : '))
invite.append(input('Who will you invite to the party? (3/3) : '))
answer = input('Do you have someone to invite? (y/n) : ')
=======
# invite = []
# answer = input('Do you have someone to invite? (y/n) : ')
# def invited():
#     if answer == 'y' or answer == 'n':
#         while answer == 'y':
#             invite.append(input('Enter the name of the person you want to invite. : '))
#             answer = input('Do you have someone to invite? (y/n) : ')
#     else:
#         print("Please enter it correctly. (y/n)")
#         invited()
# print('The number of people invited ',len(invite))
invite = []
answer = str(input('Do you have someone to invite? (y/n) : '))
>>>>>>> 052e4929750bab0df3010a9672b1e6d6c4b28790
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
<<<<<<< HEAD
invited()

print(invite)
print('The number of people invited ',len(invite))
=======

invited()
>>>>>>> 052e4929750bab0df3010a9672b1e6d6c4b28790
