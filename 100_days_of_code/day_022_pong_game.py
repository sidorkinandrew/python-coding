# imports
from turtle import Screen, Turtle
import time

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH / 4 * 3)
SCREEN_UPDATE_DELAY = 0.01

PADDLE_MOVE = int(SCREEN_WIDTH / 40)
BALL_MOVE = int(SCREEN_HEIGHT / 150)
BALL_SPEEDUP_PERCENT = 20

SCOREBOARD_FONT = ("Courier", 80, "normal")


# Paddle class

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_MOVE * 5 / 20, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + PADDLE_MOVE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - PADDLE_MOVE
        self.goto(self.xcor(), new_y)


# Ball class

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = BALL_MOVE
        self.y_move = BALL_MOVE
        self.move_speed = SCREEN_UPDATE_DELAY

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 1 - BALL_SPEEDUP_PERCENT / 100

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = SCREEN_UPDATE_DELAY
        self.bounce_x()


# ScoreBoard class

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(int(-SCREEN_WIDTH / 8), int(SCREEN_HEIGHT / 4))
        self.write(self.l_score, align="center", font=SCOREBOARD_FONT)
        self.goto(int(SCREEN_WIDTH / 8), int(SCREEN_HEIGHT / 4))
        self.write(self.r_score, align="center", font=SCOREBOARD_FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


# main

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((int(SCREEN_WIDTH / 2) - PADDLE_MOVE, 0))
l_paddle = Paddle((int(-SCREEN_WIDTH / 2) + PADDLE_MOVE, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if abs(ball.ycor()) > SCREEN_HEIGHT / 2 - PADDLE_MOVE:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < PADDLE_MOVE * 1.5 and ball.xcor() > SCREEN_WIDTH / 2 - PADDLE_MOVE * 2 \
            or ball.distance(l_paddle) < PADDLE_MOVE * 1.5 and ball.xcor() < -SCREEN_WIDTH / 2 + PADDLE_MOVE * 2:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > SCREEN_WIDTH / 2 - PADDLE_MOVE:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses:
    if ball.xcor() < -SCREEN_WIDTH / 2 + PADDLE_MOVE:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
