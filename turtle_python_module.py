import turtle
w = turtle.Screen()
w.bgcolor("lightblue")
t = turtle.Turtle()
t.pencolor("red")
t.pensize(4)
t.shape("turtle")
t.fillcolor("pink")

for i in range(4):
    t.right(90)
    t.forward(200)

    for i in range(3):
        t.pencolor("green")
        t.left(120)
        t.forward(200)

t.penup()
t.goto(200,200)
t.left(120)
t.pendown()
for k in range(360):
    t.pencolor("white")
    t.left(1)
    t.forward(4)


w.exitonclick
