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
