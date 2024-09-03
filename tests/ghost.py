import penndraw as pd

pd.set_canvas_size(500, 500)

for i in range(10):
    pd.set_pen_color(*pd.HSS_BLUE, 255 // 10 * i)
    pd.filled_circle(0.2 + 0.05 * i, 0.5, 0.2)

pd.run()
