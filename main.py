from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("Ninja Turtle Race!")
screen.setup(width=500, height=400)
screen.bgcolor("black")
user_bet = screen.textinput(title="Make Your Bet",
                            prompt="Which turtle will win the race? Choose: Blue, Orange, Red, or Purple").lower()

is_race_on = False
colors = ["blue", "DarkOrange2", "red", "purple"]
y_pos = [-150, -50, 50, 150]
ninja_turtles = []

for i in range(0, 4):
	ninj_turtle = Turtle(shape="turtle")
	ninj_turtle.color(colors[i])
	ninj_turtle.penup()
	ninj_turtle.goto(x=-230, y=y_pos[i])
	ninja_turtles.append(ninj_turtle)

if user_bet:
	is_race_on = True

while is_race_on:

	for turtle in ninja_turtles:
		turtle.speed("slow")
		if turtle.xcor() > 220:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				screen.title(f"You've won! The {winning_color} turtle won the race!")
				print(f"You've won! The {winning_color} turtle won the race!")
			else:
				screen.title(f"You've lost. The {winning_color} turtle won the race.")
				print(f"You've lost. The {winning_color} turtle won the race.")

		rand_dist = random.randint(1, 10)
		turtle.forward(rand_dist)

screen.exitonclick()
