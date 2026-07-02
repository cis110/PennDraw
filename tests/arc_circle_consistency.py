"""Visual demo of the arc/circle consistency bug.

arc() computes its radius using only _factor_x, so it always draws a
pixel-space circle regardless of the canvas aspect ratio.

circle() uses both _factor_x and _factor_y, so it draws a user-space
circle (which is an ellipse in pixel space when the canvas is non-square).

On a square canvas the two are identical — this script shows that case.

Red  = circle(x, y, r)      — user-space circle
Blue = arc(x, y, r, 0, 360) — pixel-space circle (bug: ignores y scale)
"""
import penndraw as pd

pd.set_canvas_size(512, 512)
pd.set_pen_color(pd.WHITE)
pd.filled_square(0.5, 0.5, 0.5)

pd.set_pen_radius(0.004)
pd.set_pen_color(pd.RED)
pd.circle(0.5, 0.5, 0.3)
pd.set_pen_color(pd.BLUE)
pd.arc(0.5, 0.5, 0.3, 0, 360)

pd.set_pen_color(pd.BLACK)
pd.set_font_size(14)
pd.text(0.5, 0.15, "Red = circle()   Blue = arc(0,360)")
pd.text(0.5, 0.08, "On a square canvas these should overlap exactly")

pd.run()
