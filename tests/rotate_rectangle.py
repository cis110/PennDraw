import penndraw as pd

pd.line(0, 0.5, 1, 0.5)
pd.line(0.5, 0, 0.5, 1)
pd.filled_rectangle(0.5, 0.5, 0.2, 0.1, 10)

pd.set_pen_color(pd.RED)
pd.filled_circle(0.5, 0.5, 0.01)
pd.square(0.5, 0.5, 0.2, 10)

pd.set_pen_color(pd.BLUE)
pd.filled_rectangle(0.9, 0.9, 0.05, 0.03, 30)
pd.filled_rectangle(0.9, 0.9, 0.05, 0.03, -30)

pd.set_pen_color(pd.GREEN)
pd.filled_circle(0.9, 0.9, 0.01)
pd.square(0.1, 0.1, 0.05, 10)
pd.square(0.1, 0.1, 0.05, -10)


pd.run()
