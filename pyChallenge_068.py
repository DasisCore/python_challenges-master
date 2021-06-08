import random, turtle
turtle.shape('turtle')
turtle.speed(100)
line_num = random.randint(10, 100)
for i in range(0, line_num):
    length_num = random.randint(10, 100)
    angle_num = random.randint(0, 360)
    turtle.forward(length_num)
    turtle.right(angle_num)
turtle.exitonclick()
