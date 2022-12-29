import turtle
from turtle import Screen
import turtle as t
import random


is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Yarışma", prompt="sence hangi kamplumbaga kazanacak? ")
colors = ["blue", "red", "orange", "black", "green", "purple"]
kordinatlar = [-50, -25, 0, 25, 50, 75]
all_turtles = []

if user_bet:
    is_race_on = True

for i in range(6):
    flork = t.Turtle(shape="turtle")
    flork.penup()
    flork.color(colors[i])
    flork.goto(x=-200, y=kordinatlar[i])
    all_turtles.append(flork)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 130:
            is_race_on = False
            kazanan = turtle.pencolor()
            if kazanan == user_bet:
                print(f"bravo {kazanan} kazandı")
            else:
                print(f"kaybettiniz, {kazanan} renk kazandı")

        rand_sayı = random.randint(1, 10)
        turtle.forward(rand_sayı)

screen.exitonclick()
