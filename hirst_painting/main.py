import turtle
import random

color_list = [(212, 210, 208), (226, 221, 224), (224, 229, 226), (226, 229, 232), (158, 79, 50), (184, 178, 181),
              (215, 193, 150), (153, 179, 155), (32, 109, 137), (186, 152, 37), (43, 131, 90), (146, 28, 20),
              (142, 174, 185), (8, 103, 78), (213, 88, 59), (140, 69, 80), (218, 179, 173), (163, 21, 28),
              (210, 179, 183), (70, 50, 41), (65, 150, 171), (95, 149, 97), (203, 67, 75), (5, 89, 109),
              (63, 49, 55), (23, 66, 93), (74, 67, 44), (176, 201, 185), (173, 194, 212)]

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed(0)
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
