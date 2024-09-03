import penndraw as pd
num_clicks = 0
while True:
    pd.clear()
    pd.text(0.5, 0.5, f"Number of Clicks: {num_clicks}")
    if pd.mouse_pressed():
        num_clicks = num_clicks + 1
    pd.advance()
