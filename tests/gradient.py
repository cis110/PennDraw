import penndraw as pd
pd.set_canvas_size(256, 256)
x = 0
while x < 256:
    pd.set_pen_color(x, x, x)
    pd.filled_rectangle(x / 255, 0.5, 1 / 255, 0.25)
    x += 1
pd.run()
