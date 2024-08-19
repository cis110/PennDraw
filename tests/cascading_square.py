import penndraw as pd
from random import randint

x_center = 0.5
y_center = 0.5
half_side_length = 0.01
red = randint(0, 256)
blue = randint(0, 256)
green = randint(0, 256)
pd.set_pen_color(red, green, blue)

while True:
    pd.filled_square(x_center, y_center, half_side_length)
    half_side_length += 0.01
    if half_side_length >= 0.5:
        half_side_length = 0.01
        red = randint(0, 256)
        blue = randint(0, 256)
        green = randint(0, 256)
        pd.set_pen_color(red, green, blue)
    pd.advance()