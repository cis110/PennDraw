"""
Draw the image with its default dimensions in the
center of the canvas. 
"""

import penndraw as pd

pd.set_canvas_size(500, 500)


pd.picture(0.25, 0.5, "pyglet_logo.jpg", 50, 50, 45)
pd.picture(0.5, 0.5, "selfie.jpeg", 200, 200, 180)
pd.picture(0.75, 0.5, "pyglet_logo.png", 100, 100, -45)
pd.run()
