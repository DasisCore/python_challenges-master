input_age = int(input("What are your age? : "))
if input_age >= 18:
    print('"You can vote"')
elif input_age == 17:
    print('"You can learn to drive"')
elif input_age == 16:
    print('"You can buy a lottery ticket"')
else:
    print('"You can go trick-or-tricking"')
