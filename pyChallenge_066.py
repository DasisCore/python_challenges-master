import random, turtle
turtle.shape("turtle")
turtle.pensize(5)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
i = 0
while i < 8:
    r_color = random.choice(["red", "black", 'pink', 'blue', 'orange', 'yellow', 'yellowgreen', 'purple'])
    turtle.color(r_color)
    turtle.forward(100)
    turtle.right(45)
    i = i + 1
turtle.hideturtle()
turtle.exitonclick()
