"""
Draw the text with default parameters in the center of the canvas.
The text should be horizontally and vertically centered on the
small circle drawn.
The message should be "Howdy, partner."
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
pd.circle(0.5, 0.5, 0.01)
pd.text(0.5, 0.5, "Howdy, partner.")
pd.run()
