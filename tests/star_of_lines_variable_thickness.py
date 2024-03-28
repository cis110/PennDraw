"""
On a black canvas of size 400x400, draw a red vertical line,
a thicker blue horizontal line, and an even thicker
green diagonal line heading from the bottom left to the top right.
"""

import penndraw as pd

pd.set_canvas_size(400, 400)
pd.set_pen_color(255, 0, 0)
pd.line(0.5, 0.1, 0.5, 0.9)
pd.set_pen_radius(0.008)
pd.set_pen_color(0, 0, 255)
pd.line(0.1, 0.5, 0.9, 0.5)
pd.set_pen_radius(0.016)
pd.set_pen_color(0, 255, 0)
pd.line(0.1, 0.1, 0.9, 0.9)
pd.run()
