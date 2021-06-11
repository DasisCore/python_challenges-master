tv_list = ['Infinite Challenge', 'Running man', 'Gag Concert', '1 Night 2 Days' ]
for i in tv_list:
    print(i)
anthor_tv = input('Please enter another program. : ')
want_num = int(input('Enter the desired location in the list.(0 ~ 3) : '))
tv_list.insert(want_num, anthor_tv)

for i in tv_list:
    print(i)
