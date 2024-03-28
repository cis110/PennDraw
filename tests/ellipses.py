"""
On a canvas of size 500x500, draw three white ellipses.
1. A circle in the bottom left corner.
2. A vertical ellipse in the middle.
3. A horizontal ellipse in the top right corner.
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
pd.set_pen_radius(0.008)
pd.ellipse(0.25, 0.25, 0.125, 0.125)  # a circle in the middle
pd.ellipse(0.5, 0.5, 0.075, 0.125)  # a horizontal ellipse
pd.ellipse(0.75, 0.75, 0.125, 0.075)  # a vertical ellipse

pd.run()
