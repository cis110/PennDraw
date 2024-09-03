import penndraw as pd
import math

for i in range(1, 628):
    x = 0.5 + 0.5 * math.cos(i/100)
    y = 0.5 + 0.5 * math.sin(i/100)
    pd.set_pen_radius(i / 60000)
    pd.point(x, y)

pd.run()
