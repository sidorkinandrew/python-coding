import colorgram
import requests

import turtle as turtle_module
import random

picture_fname = __file__.split("\\")[-1].split(".")[0] + ".jpg"
turtle_module.colormode(255)
number_of_dots = 100


def fetch_hirst_picture(fname):
    print("fetching a Hirst picture from cdn.sanity.io ..", end="")
    jpg_data = requests.get(
        "https://cdn.sanity.io/images/dqllnil6/production/537b6eca8c43b46982da4c2af786fb1124592d0a-1200x995.jpg?w=1080&q=60&auto=format")
    print(f".. done\nwriting to {fname} ..", end="")
    with open(fname, "wb") as f:
        f.write(jpg_data.content)
    print(".. done\n")


def get_colors_from_local_file(fname, num_colors=30):
    print(f"extracting {num_colors} colors from {fname} ..", end="")
    rgb_colors = []
    colors = colorgram.extract(fname, num_colors)
    for color in colors:
        rgb_colors.append(color.rgb)
    print(".. done\n")
    return rgb_colors


def init_turtle():
    a_turtle = turtle_module.Turtle()
    a_turtle.speed("fastest")
    a_turtle.penup()
    a_turtle.hideturtle()
    a_turtle.setheading(225)
    a_turtle.forward(300)
    a_turtle.setheading(0)
    return a_turtle


def draw_hirst_picture(a_turtle, number_of_dots=number_of_dots, dot_size=20, dot_distance=50):
    for dot_count in range(1, number_of_dots + 1):
        a_turtle.dot(dot_size, random.choice(rgb_colors))
        a_turtle.forward(dot_distance)
        if dot_count % 10 == 0:
            a_turtle.setheading(90)
            a_turtle.forward(dot_distance)
            a_turtle.setheading(180)
            a_turtle.forward(dot_distance*10)
            a_turtle.setheading(0)


fetch_hirst_picture(picture_fname)

rgb_colors = get_colors_from_local_file(picture_fname)

tim = init_turtle()
draw_hirst_picture(tim)

screen = turtle_module.Screen()
screen.exitonclick()
