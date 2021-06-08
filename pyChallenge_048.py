again = 'y'
count = 0
while again == 'y':
    name = input("What is the name of the person you would like to invite to the party? : ")
    print('"', name, 'has now been invited."')
    count = count + 1
    again = input("Is there anyone else you would like to invite? (y/n) : ")
print('"', count, 'people were invited to the party."')
