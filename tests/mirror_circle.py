import penndraw as pd

pd.set_canvas_size(500, 500)

while True:
    pd.clear()
    pd.set_pen_color(pd.HSS_BLUE)
    pd.filled_circle(0.3, 0.4, 0.01)
    if pd.mouse_pressed():
        x_center = pd.mouse_x()
        y_center = 1 - pd.mouse_y()
        pd.set_pen_color(pd.HSS_RED)
        pd.filled_circle(x_center, y_center, 0.01)
    pd.advance()