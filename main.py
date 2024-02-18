from turtle import Turtle, Screen
import random


is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)
user_selection = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race ? Enter a color: ")
colors = ["blue", "red", "green", "yellow", "purple", "orange"]
turtles = []


if user_selection:
  is_race_on = True

ycor = -100
for i in range(0, 6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.color(colors[i])
  new_turtle.goto(x=-235, y=ycor)
  ycor += 40
  turtles.append(new_turtle)
  


while is_race_on is True:
  for j in turtles:
    if j.xcor() >= 235:
      turtle_color = j.pencolor()
      if turtle_color == user_selection:
        print(f"You won, the '{turtle_color}' turtle won the race!")
      else:
        print(f"You lost, the '{turtle_color}' turtle won the race!")
    is_race_on = False
    turtle_speed = random.randint(0, 10)
    j.forward(turtle_speed)
    




screen.exitonclick()