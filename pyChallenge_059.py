import random
color = random.choice(["black", "white" ,"purple", "orange", "green"])
print(color) #알고리즘 확인을 위해 삽입.
a_color = input('Choose one of the following colors.\n"Black", "White" ,"Purple", "Orange", "Green" : ')
a_color = a_color.lower()
answer = True
while answer == True:
    if color == a_color:
        print('"Well done!"')
        answer = False
    elif a_color == "Black":
        a_color = input('"Is your heart Black?"\nEnter the color again : ')
        answer = True
    elif a_color == "White":
        a_color = input('"You are as pure as white."\nEnter the color again : ')
        answer = True
    elif a_color == "Purple":
        a_color = input('"Purple is the color of nobility."\nEnter the color again : ')
        answer = True
    elif a_color == "Orange":
        a_color = input('"Have you been eating oranges for a long time?"\nEnter the color again : ')
        answer = True
    elif a_color == "Green":
        a_color = input('"I bet you are Green with envy"\nEnter the color again : ')
        answer = True
    else:
        a_color = input('"Enter the color again" : ')
