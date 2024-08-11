"""
Draw the image with its default dimensions in the
center of the canvas. 
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
pd.picture(0.5, 0.5, "pyglet_logo.png")
pd.run()
