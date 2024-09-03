import penndraw as pd

pd.line(0, 0.5, 1, 0.5)
pd.line(0.5, 0, 0.5, 1)
pd.filled_ellipse(0.5, 0.5, 0.2, 0.1, 10)

pd.set_pen_color(pd.RED)
pd.filled_circle(0.5, 0.5, 0.01)
pd.square(0.5, 0.5, 0.2, 10)

pd.set_pen_color(pd.BLUE)
pd.ellipse(0.9, 0.9, 0.05, 0.03, 30)
pd.ellipse(0.9, 0.9, 0.05, 0.03, -30)
pd.ellipse(0.9, 0.9, 0.05, 0.03, -60)
pd.ellipse(0.9, 0.9, 0.05, 0.03, 60)


pd.set_pen_color(pd.GREEN)
pd.filled_circle(0.9, 0.9, 0.01)
pd.ellipse(0.1, 0.1, 0.05, 0.03)
pd.ellipse(0.1, 0.1, 0.05, 0.03, 45)
pd.line(0.1, 0, 0.1, 1)
pd.line(0, 0.1, 1, 0.1)


# pd.ellipse(0.1, 0.1, 0.05, 0.03, 10)
# pd.ellipse(0.1, 0.1, 0.05, 0.03, -10)
# pd.ellipse(0.1, 0.1, 0.05, 0.03, -20)
# pd.ellipse(0.1, 0.1, 0.05, 0.03, 20)
# pd.ellipse(0.1, 0.1, 0.05, 0.03, -90)
pd.ellipse(0.1, 0.1, 0.05, 0.03, 90)


pd.set_pen_color(pd.HSS_RED)
pd.filled_circle(0.1, 0.1, 0.01)

pd.run()
