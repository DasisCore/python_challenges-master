name = input('"Enter the your name" : ')
len_name = len(name)
if len_name < 5:
    surname = input('"Enter the your surname" : ')
    real_name = surname+name
    print(real_name.upper())
else:
    print(name.lower())
