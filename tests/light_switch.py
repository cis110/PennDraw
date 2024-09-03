import penndraw as pd
on = False
while True:
    if on:
        pd.clear(pd.BLACK)
    else:
        pd.clear(pd.YELLOW)

    if pd.has_next_key_typed():
        key = pd.next_key_typed()
        if key == 'x':
            on = not on
    pd.advance()
