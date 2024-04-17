"""
Draw the text in different configurations.
The text "Harry Smith" should be horizontally and vertically centered on the
white circle drawn.
"Travis Q. McGaha" should have its left edge aligned with the blue point. It should be in 16 point font (largest)
"Python is cool!" should have its right edge aligned with the yellow point. It should be in 10 point font (smallest)
The message should be "Howdy, partner."
"""

import penndraw as pd

pd.set_canvas_size(500, 500)

pd.filled_circle(0.5, 0.5, 0.01)
pd.text(0.5, 0.5, "Harry Smith")

pd.set_pen_color(pd.HSS_BLUE)
pd.set_font_size(16)
pd.filled_circle(0.5, 0.75, 0.01)
pd.set_pen_color(pd.WHITE)
pd.text_left(0.5, 0.75, "Travis Q. McGaha")

pd.set_pen_color(pd.HSS_YELLOW)
pd.set_font_size(10)
pd.filled_circle(0.5, 0.25, 0.01)
pd.set_pen_color(pd.WHITE)
pd.text_right(0.5, 0.25, "Python is cool!")


pd.run()
