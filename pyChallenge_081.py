fa_subject = []
fa_subject.append(input('What is your favorite subject? : '))
def append_sub():
    fa_subject.append(input('Please enter the subject to be added. : '))

def ans_add():
    answer = input('Have you entered enough? (y/n) : ')
    if answer == 'y':
        for letter in fa_subject:
            print(letter, end = "-")
    elif answer == 'n':
        append_sub()
        ans_add()
    else:
        print('Invalid input.')
        ans_add()
ans_add()


# 원래 문제가 원하던 답.
# subject = input('좋아하는 과목을 추가하세요. : ')
# for letter in subject:
#     print(letter, end = "-")
