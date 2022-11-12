# imports
from turtle import Turtle, Screen
import random
import time

# Constants
SCREEN_SIZE = 800
HALF_SCREEN = int(SCREEN_SIZE / 2)
MOVE_DISTANCE = int(HALF_SCREEN / 15)
COLLISION_DISTANCE = int(HALF_SCREEN / 20)
STARTING_POSITIONS = [(0, 0), (-MOVE_DISTANCE, 0), (-MOVE_DISTANCE * 2, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Scoreboard settings
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# Food class

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-HALF_SCREEN + MOVE_DISTANCE, HALF_SCREEN - MOVE_DISTANCE) // 10 * 10
        random_y = random.randint(-HALF_SCREEN + MOVE_DISTANCE, HALF_SCREEN - MOVE_DISTANCE) // 10 * 10
        self.goto(random_x, random_y)


# Snake class

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(stretch_len=MOVE_DISTANCE / 20.0, stretch_wid=MOVE_DISTANCE / 20.0)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


# ScoreBoard


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, HALF_SCREEN - MOVE_DISTANCE * 2)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


# main.py

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def init_screen(a_snake, width=SCREEN_SIZE, height=SCREEN_SIZE, bgcolor="black", title="My Snake Game"):
    screen = Screen()
    screen.setup(width=width, height=height)
    screen.bgcolor(bgcolor)
    screen.title(title)
    screen.tracer(0)
    screen.listen()
    screen.onkey(a_snake.up, "Up")
    screen.onkey(a_snake.down, "Down")
    screen.onkey(a_snake.left, "Left")
    screen.onkey(a_snake.right, "Right")
    return screen


screen = init_screen(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < COLLISION_DISTANCE:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if abs(snake.head.xcor()) >= HALF_SCREEN or abs(snake.head.ycor()) >= HALF_SCREEN:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < COLLISION_DISTANCE:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
