import penndraw as pd
x_center = 0.5  # SETUP
loop_num = 1
while True:
    pd.clear()                            # 1. clear the screen
    pd.filled_square(x_center, 0.5, 0.1)  # 2. draw this frame
    print(f"In Loop #{loop_num}, square is at x={x_center}")
    x_center += 0.01                      # 3. update shapes for next frame
    loop_num += 1
    pd.advance()
