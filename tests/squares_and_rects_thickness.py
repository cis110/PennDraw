"""
On a black canvas of size 300x300, draw a blue filled square to cover
the entire screen. Then draw a green filled rectangle that covers the bottom half,
and a red rectangle (outline) that covers the top half. Finally, draw a thick yellow square
in the center of the canvas.
"""
import penndraw as pd

pd.set_canvas_size(500, 500)
pd.set_pen_color(0, 0, 255)
pd.filled_square(0.5, 0.5, 0.5)
pd.set_pen_color(0, 255, 0)
pd.filled_rectangle(0.5, 0.25, 0.5, 0.25)
pd.set_pen_color(255, 0, 0)
pd.rectangle(0.5, 0.75, 0.5, 0.25)
pd.set_pen_radius(0.01)
pd.set_pen_color(255, 255, 0)
pd.square(0.5, 0.5, 0.1)

pd.run()
