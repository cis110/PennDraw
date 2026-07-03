"""p5.js-style demo: a square bounces around the canvas.
Click to change its color. Press a key to print it to the console.
"""

import penndraw as pd

pd.set_canvas_size(500, 500)

x_center = 0.5
y_center = 0.5
half_side = 0.1
dx = 0.01
dy = 0.007


@pd.setup
def setup():
    pd.set_pen_color(pd.HSS_BLUE)


@pd.draw
def draw():
    global x_center, y_center, dx, dy
    pd.clear()
    x_center += dx
    y_center += dy
    if not (half_side <= x_center <= 1 - half_side):
        dx *= -1
    if not (half_side <= y_center <= 1 - half_side):
        dy *= -1
    pd.filled_square(x_center, y_center, half_side)


@pd.on_mouse_pressed
def on_click(x, y):
    pd.set_pen_color(pd.HSS_RED)


@pd.on_key_pressed
def on_key(key):
    print(f"Key pressed: {key}")


pd.run()
