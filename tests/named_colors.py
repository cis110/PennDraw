"""
On a canvas of size 500x500, draw some stuff. There should be a yellow background
with a blue shape, orange shape, and red shape. This is a test to make sure that
setting the color works with tuples as inputs and that the named colors are indeed
in the namespace. (Probably don't really need to test that second part.)
Also the pen thickness should be 0.01, which is 5 times thicker than default.
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
pd.clear(pd.HSS_YELLOW)
pd.set_pen_radius(0.01)

pd.set_pen_color(pd.HSS_BLUE)
pd.ellipse(0.25, 0.25, 0.25, 0.25)  # a circle in the bottom left
pd.set_pen_color(pd.HSS_ORANGE)
pd.ellipse(0.5, 0.5, 0.15, 0.25)  # a vertical ellipse
pd.set_pen_color(pd.HSS_RED)
pd.ellipse(0.75, 0.75, 0.25, 0.15)  # a horizontal ellipse

pd.run()
