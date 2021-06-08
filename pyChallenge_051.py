#"10 green bottles."
bottle = 10
while bottle > 0:
    print('There are',bottle , 'green bottles hanging on the wall')
    print(bottle, 'green bottles hanging on the wall.')
    print('and if 1 green bottle should accidentally fall')
    h_num = int(input('how many green vottles will be hanging on the wall? : '))
    bottle = bottle - 1
    if h_num == bottle:
        print('"There will be', bottle, 'green bottles hanging on the wall"\n')
    else:
        bottle = int(input('"No, try again." : '))
print("There are no more green bottles hanging on the wall")
