"""
On a canvas of size 500x500, draw a filled polygon with 5 sides

double[] xcoords = { 0.5, 1, 1  , 0.75, 0.5 };
double[] ycoords = { 0  , 0, 0.7, 1   , 0.7 };
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
pd.filled_polygon(0.5, 0, 1, 0, 1, 0.7, 0.75, 1, 0.5, 0.7)
pd.run()
