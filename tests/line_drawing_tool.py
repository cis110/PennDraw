import penndraw as pd

old_x, old_y = 0.5, 0.5
pd.set_pen_radius(0.012)

while True:
    if pd.mouse_pressed():
        x, y = pd.mouse_x(), pd.mouse_y()
        if y > 0.5:
            pd.set_pen_color(pd.RED)
        else:
            pd.set_pen_color(pd.BLACK)
        pd.line(old_x, old_y, x, y)
        old_x, old_y = x, y
    pd.advance()
