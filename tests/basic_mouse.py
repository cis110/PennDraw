"""Have a square follow the mouse on screen.
Change colors when the mouse is clicked.
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
x_center = 0.5
y_center = 0.5
half_side = 0.1
pd.set_pen_color(pd.HSS_BLUE)

while True:
    pd.clear()
    x_center, y_center = pd.mouse_x(), pd.mouse_y()
    if pd.mouse_pressed():
        pd.set_pen_color(pd.HSS_RED)
    else:
        pd.set_pen_color(pd.HSS_BLUE)
    pd.filled_square(x_center, y_center, half_side)
    pd.advance()
