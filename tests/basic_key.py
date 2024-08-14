"""Have a bit of text follow the mouse on screen.
Change colors when the mouse is clicked.
"""

import penndraw as pd

pd.set_canvas_size(500, 500)
x_center = 0.5
y_center = 0.5
text = "NOTHING"
pd.set_pen_color(pd.HSS_BLUE)
pd.set_font_size(24)
while True:
    pd.clear()
    if pd.has_next_key_typed():
        if pd.is_key_typed('e'):
            pd.set_pen_color(pd.HSS_RED)
        else:
            pd.set_pen_color(pd.HSS_ORANGE)
        text = pd.next_key_typed()
    else:
        pd.set_pen_color(pd.HSS_BLUE)
    pd.text(x_center, y_center, text)
    pd.advance()
