data_sales = {'John':{'N':3056, 'S':8463, 'E':8441, 'W':2694},
            'Tom':{'N':4832, 'S':6786, 'E':4737, 'W':3612} ,
            'Anne':{'N':5239, 'S':4802, 'E':5820, 'W':1859},
            'Fiona':{'N':3904, 'S':3645, 'E':8821, 'W':2451}}
name = input('Enter the your name : ')
area = input('Enter the your area : ')
print(data_sales[name][area])

def dec():
    decision = input('Are you sure you want to change your data? (y/n) : ')
    if decision == 'y':
        change_name = input('What is the name of the data you want to change? : ')
        change_area = input('What is the area of the data you want to change? : ')
        change_num = int(input('How much sales do you want to change? : '))
        data_sales[change_name][change_area] = change_num
        print(data_sales[change_name])
    elif decision == 'n':
        print(data_sales[name][area])
    else:
        print('Invaild input')
        dec()
dec()
