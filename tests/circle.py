"""
On a black canvas of size 500x500, draw a white circle in the top left corner.
The top and left points of the circle should touch the top and left edges of the canvas.
"""
import penndraw as pd

pd.set_canvas_size(500, 500)
pd.circle(0.1, 0.9, 0.1)
pd.run()
