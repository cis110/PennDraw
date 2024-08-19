"""Draw four arcs. All arcs have their centers
in the middle of the canvas. The first arc is
a quarter of a circle, the second arc is a half
of a circle, the third arc is three quarters of
a circle, and the fourth arc is a full circle.
The circles have increasingly large radii
"""

import penndraw as pd

pd.set_canvas_size(500, 500)

pd.set_pen_color(pd.HSS_BLUE)

pd.closed_arc(0.5, 0.5, 0.15, 0, 90)
pd.closed_arc(0.5, 0.5, 0.2, 90, 270)
pd.arc(0.5, 0.5, 0.3, 270, 180)
pd.arc(0.5, 0.5, 0.4, 0, 360)

pd.run()