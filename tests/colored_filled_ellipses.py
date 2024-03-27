"""
On a canvas of size 500x500, draw three filled ellipses of different colors.
1. A green circle in the bottom left corner.
2. A red vertical ellipse in the middle.
3. A low-opacity blue horizontal ellipse in the top right corner.
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
pd.set_pen_color(0, 255, 0)
pd.filled_ellipse(0.25, 0.25, 0.25, 0.25)  # a circle in the bottom left
pd.set_pen_color(255, 0, 0)
pd.filled_ellipse(0.5, 0.5, 0.15, 0.25)  # a vertical ellipse
pd.set_pen_color(0, 0, 255, 100)
pd.filled_ellipse(0.75, 0.75, 0.25, 0.15)  # a horizontal ellipse

pd.run()
