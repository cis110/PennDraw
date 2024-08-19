import penndraw as pd

pd.set_canvas_size(500, 500)

pd.filled_pie(0.5, 0.5, 0.2, 0, 90)
pd.filled_pie(0.5, 0.5, 0.3, 90, 270)
pd.pie(0.5, 0.5, 0.4, 280, 340)

pd.run()