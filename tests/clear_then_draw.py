"""
On a canvas of size 500x500, draw some stuff. Then, clear to white.
Then, draw another ellipse. The screen should have only the last ellipse.
Also, the color of the last ellipse should be drawn using the previous
color setting, which is blue.
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
pd.set_pen_color(0, 255, 0)
pd.ellipse(0.25, 0.25, 0.25, 0.25)  # a circle in the bottom left
pd.set_pen_color(255, 0, 0)
pd.ellipse(0.5, 0.5, 0.15, 0.25)  # a vertical ellipse
pd.set_pen_color(0, 0, 255, 100)
pd.ellipse(0.75, 0.75, 0.25, 0.15)  # a horizontal ellipse

pd.clear()

pd.ellipse(0.75, 0.75, 0.25, 0.15)  # a horizontal ellipse
pd.run()
