"""
On a black canvas of size 500x500, draw a white circle in the top left corner,
and a white filled circle in the bottom right corner.
The top and left points of the upper circle should touch the top and left edges of the canvas.
The bottom and right points of the lower circle should touch the bottom and right edges of the canvas.
"""
import penndraw as pd

pd.set_canvas_size(500, 500)
pd.circle(0.1, 0.9, 0.1)
pd.filled_circle(0.9, 0.1, 0.1)
pd.run()
