"""
On a canvas of size 500x500, draw an empty polygon with 5 sides

xcoords = { 0.5, 1, 1  , 0.75, 0.5 };
ycoords = { 0  , 0, 0.7, 1   , 0.7 };
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
pd.polygon(0.5, 0, 1, 0, 1, 0.7, 0.75, 1, 0.5, 0.7)
pd.run()
