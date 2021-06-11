password = input('Please enter a new password. : ')
re_password = input('Please enter it again. : ')
if password == re_password:
    print('"Thank you"')
elif password.lower() == re_password.lower():
    print('"They must be in the same case"')
else:
    print('"Incorrect"')
