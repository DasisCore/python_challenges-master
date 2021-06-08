import turtle
turtle.shape('turtle')
turtle.pensize(3)
turtle.left(120)
turtle.speed(10)
for j in range(0, 10):
    turtle.right(36)
    for i in range(0, 8):
        turtle.forward(100)
        turtle.right(45)
turtle.exitonclick()
