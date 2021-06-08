import turtle
turtle.speed(5)
turtle.penup()
turtle.goto(-140, +70)
turtle.pendown()
turtle.pensize(5)
turtle.color('skyblue', 'yellowgreen')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("pink", 'yellow')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("purple", 'orange')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(70)

turtle.exitonclick()
