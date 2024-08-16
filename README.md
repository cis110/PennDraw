---
layout: default
title: CIS 1100 penndraw.py Documentation
active_tab: penndraw
---

### [PennDraw.java](../assets/example_programs/PennDraw.java) 😠😠😠 FIX ME 😠😠😠

---

#### PennDraw Reference Page

The `penndraw` Python package is a reimplementation of `PennDraw.java`, which is itself an expanded version of `StdDraw` from Sedgewick and Wayne's *Introduction to Programming in Java: An Interdisciplinary Approach*. `PennDraw` supports everything that `StdDraw` supports, plus additional drawing and animation commands. This Python version is implemented using [`pyglet`](https://docs.pyglet.org/en/latest/index.html).

---

#### Downloading and Using PennDraw

If you are using Codio, the `penndraw` package has already been installed for you. You should not need to install or configure anything to run `PennDraw` programs.

If you want to use `penndraw` outside of Codio, you can install it on all platforms using the following command:

```console
pip install penndraw
```

*Please note that animations do not work outside of Codio on Windows machines right now.*
---

#### Getting Started: A Simple Program

Here's a simple program that draws a line and a point:
```python
import penndraw as pd
pd.line(0, 0, 1, 1)
pd.point(0, 1)
pd.run()
```
- `PennDraw` is implemented as a Python package called `penndraw`. You must import this at the start of each program that uses `PennDraw`. The line `import penndraw as pd` takes care of this and allows you to use the abbreviation `pd` as well. **All of the documentation assumes that you are using the `pd` abbreviation.**
- `PennDraw` takes care of creating a window for you as soon as you start drawing.
- `pd.line(0, 0, 1, 1)` draws a line from near the lower-left corner to the near the upper-right corner.
- `pd.point(0, 1)` draws a point near the upper left corner
- `pd.run()` causes your drawing to appear. Forgetting to do this will mean that your line & point won't show up.

<!-- **Why aren't (0, 0) and (1, 1) at the actual corners of the window?** Most CIS 1100 assignments that involve drawing will require you to keep your drawing within the "unit square" defined by the corners (0, 0) and (1, 1). The margin that PennDraw adds makes it easy to visually verify that you stay inside this square: just draw the unit square (`PennDraw.square(0.5, 0.5, 0.5)` — see below) and make sure your drawing is completely inside it. -->

---

#### Window Size and Scale

By default, the `PennDraw` window is 512×512 pixels. To change this, use

```python
pd.set_canvas_size(width, height)
```

- `width` and `height` are the width and height of the drawing area in pixels (including the drawing area's "margin", but not including the window title or window borders).
- Calling `pd.set_canvas_size()` will erase everything in your window, and reset your line width, color, and font. It's best to use it only once at the very beginning of your programming.

You can also change the window's coordinate system, which can make it much easier to compute the coordinates for your shapes:

```python
pd.set_x_scale(left, right)
pd.set_y_scale(bottom, top)
pd.set_scale(left/bottom, right/top)
pd.set_scale()
```

- `left` is the x-coordinate of the left edge, `right` is the x-coordinate of the right edge, `bottom` is the y-coordinate of the bottom edge, and `top` is the y-coordinate of the top edge. `pd.set_scale(left/bottom, right/top)` is similar to calling both `pd.set_x_scale(left, right)` and `pd.set_y_scale(bottom, top)` with the same inputs (both x- and y-scales will be the same.)
- `pd.set_scale()` resets the scale to the default. It is equivalent to `pd.set_scale(0, 1)`
- *left, right, top, and bottom* can all be fractional or negative numbers, such as 1.2, 3.14159, or -2.71828.

**Trying out the scale functions:**

- Cut and paste the program below into a blank file and save it into that folder under the name `penn_draw_scale_test.py`. Make sure the capitalization matches exactly.
- Run `penn_draw_scale_test.py`. When you run it, you should see a line between the bottom left and the center of the canvas. Note that the line now ends in the top middle of the image: the call to `pd.set_x_scale(0, 2)` redefined the right margin to have x-coordinate 2, so the x-coordinate 1 now refers to the middle of the window.

```python
import penndraw as pd
pd.set_x_scale(0, 2)
pd.line(0, 0, 1, 1)
pd.run()
```

- Play with different values in the call to pd.set_x_scale(). Each time you make a change, save your file, close the running program, and then run the program again.
- Replace the class to `pd.set_x_scale()` with a call to `pd.set_y_scale()`. Play with different values to see the effect on the image.
- Specifically, try `pd.set_y_scale(1, 0)`. This should flip your image vertically—it defines the *top* margin to have y-coordinate `0` and the *bottom* margin to have y-coordinate `1`.
- Try calling `pd.set_scale(left/top, right/bottom)` and see what it does with different values.
- Try calling `pd.set_x_scale()` and `pd.set_y_scale()` in the same program.

---

#### Point/Line Thickness and Color

These calls adjust the line thickness:

```java
pd.set_pen_radius()
pd.set_pen_radius(radius)
```

- `pd.set_pen_radius` resets the line thickness to the default, which is fairly arbitrarily defined as 0.002.
- `pd.set_pen_radius(radius)` sets the line width to the value radius. To get a line that is twice as thick as the default, use `pd.set_pen_radius(0.004)`.

You can also change the line color:

```java
pd.set_pen_color()
pd.set_pen_color(color)
pd.set_pen_color(red, green, blue)
pd.set_pen_color(red, green, blue, alpha)
```

- `pd.set_pen_color()` resets the pen color to the default (black).
- `pd.set_pen_color(color)` sets the color to the specified, named color. You can choose from this table:

| PennDraw Name   | Color Sample                                                                                                                   | PennDraw Name  | Color Sample                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `pd.BLACK`      | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(0, 0, 0)" /></svg>       | `pd.WHITE`     | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(255, 255, 255)" /></svg> |
| `pd.RED`        | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(255, 0, 0)" /></svg>     | `pd.GREEN`     | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(0, 255, 0)" /></svg>     |
| `pd.BLUE`       | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(0, 0, 255)" /></svg>     | `pd.YELLOW`    | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(255, 255, 0)" /></svg>   |
| `pd.CYAN`       | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(0, 255, 255)" /></svg>   | `pd.MAGENTA`   | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(255, 0, 255)" /></svg>   |
| `pd.DARK_GRAY`  | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(64, 64, 64)" /></svg>    | `pd.GRAY`      | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(128, 128, 128)" /></svg> |
| `pd.LIGHT_GRAY` | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(192, 192, 192)" /></svg> | `pd.ORANGE`    | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(255, 200, 0)" /></svg>   |
| `pd.PINK`       | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(255, 175, 175)" /></svg> | `pd.HSS_BLUE`  | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(31, 119, 180)" /></svg>  |
| `pd.HSS_ORANGE` | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(255, 126, 14)" /></svg>  | `pd.HSS_RED`   | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(219, 49, 34)" /></svg>   |
| `pd.HSS_YELLOW` | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(255, 219, 128)" /></svg> | `pd.TQM_NAVY`  | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(0, 51, 102)" /></svg>    |
| `pd.TQM_BLUE`   | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(24, 123, 205)" /></svg>  | `pd.TQM_WHITE` | <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg"><rect width="50" height="50" fill="rgb(245, 240, 236)" /></svg> |

- `pd.set_pen_color(red, green, blue)` sets the pen color to the specified *(red, green, blue)* value. *red*, *green*, and *blue* should be integers (whole numbers) between 0 and 255. For black, set all three to 0 for white set all three to 255. You can easily figure out the correct values using any of the myriad color pickers available on the web. [Here's one color picker](http://johndyer.name/lab/colorpicker/) that works great.
- `pd.set_pen_color(red, green, blue, alpha)` set the pen color to the specified (red, green, blue) value and the specified transparency *alpha*. All four numbers should be integers between 0 and 255. Set *alpha* to 0 to make the color fully transparent (invisible), or 255 to make it fully opaque (solid). Anything in between will be translucent.

**Trying out line thickness and color functions:**

- Cut and paste the sample program below into a blank file, and save it into your folder as `penndraw_pen_test`. Run it. You should see a figure similar to the one below (the blue line should be thicker than the black line).

```python
import penndraw as pd
pd.line(0, 0, 1, 1)
pd.set_pen_color(pd.BLUE)
pd.set_pen_radius(0.005)
pd.line(1, 0, 0, 1)
pd.run()
```

- Try out different values for `pd.set_pen_color()`, including different named colors, red/green/blue values, and red/green/blue/alpha values. See how each one affects the second line's color.
- Try specifying the color `pd.set_pen_color(pd.blue)`. Your program will not run successfully, and you will get an error along the lines of the following:

```console
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'penndraw' has no attribute 'blue'
```

This is a **runtime error** that leads to a crash in your program. The moral of the story is that CAPITALIZATION MATTERS!

- Try specifying a fractional value for red/green/blue/alpha, like 0.5. You should get a different compiler error along the lines of

```console
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/harrysmith/Documents/PennDraw/penndraw/penndraw.py", line 160, in set_pen_color
    color = _validate_color(args)
  File "/Users/harrysmith/Documents/PennDraw/penndraw/penndraw.py", line 216, in _validate_color
    raise ValueError(
ValueError: Invalid colors: must have 3 or 4 integer components between 0-255.
```

This is Python's way of saying that you have specified a color value that looks ok at first sight (everything is whole numbers), but is in fact bogus. It's analagous to an English sentence that is grammatically correct and made up of real words, but is total gibberish. ("Green blackbirds cha-cha solemnly from dawn to Australia.")

- Try different values for `pd.set_pen_radius()` and see how they affect the second line's thickness.

---

#### Clearing the Window

To clear the window, use: `pd.clear()`

```python
pd.clear(color)
pd.clear(red, green, blue)
pd.clear(red, green, blue, alpha)
```

`pd.clear()` erases everything on the screen and makes the entire window background white. If you want to set the window background to a different color, you can specify the color by name, or as red, green, and blue values, just like line colors. You can even specify transparency on your background color, in which case whatever was already drawn on the window will show through.

---

#### Points and Lines

Draw points and lines using:

```python
pd.point(x, y)
pd.line(xstart, ystart, xend, yend)
```

`x`, `y`, `xstart`, `ystart`, `xend`, and `yend` are the coordinates of the point and the start and end of the line. The sample programs in the previous section illustrate their use.


---

#### Squares and Circles

Draw squares and circles using:

```python
pd.square(xcenter, ycenter, half_width)
pd.square(xcenter, ycenter, half_width, angle)
pd.filled_square(xcenter, ycenter, half_width)
pd.filled_square(xcenter, ycenter, half_width, angle)

pd.circle(xcenter, ycenter, radius)
pd.filledCircle(xcenter, ycenter, radius)
```

`xcenter` and `ycenter` are the coordinates of the `center` of the square, **not** one of its corners! `angle` gives the amount of **counter-clockwise** rotation in degrees. `pd.square()` draws an **outline** in the current line color. `pd.filled_square()` draws a square **filled in** with the current line color.

**Sample square program:**

```python
# penndraw_square_test.py
import penndraw as pd
# solid black square centered at (.5, .5)
# with sides of length .6 (half-width of .3)
pd.filled_square(0.5, 0.5, 0.3)

# blue square outline centered at (.7, .3)
# with sides of length .4
# rotated 30 degrees counter-clockwise
pd.set_pen_color(pd.BLUE)
pd.square(.7, .3, .2, 30)

pd.run()
```

---

#### Rectangles and Ellipses

Draw rectangles using:

```python
pd.rectangle(xcenter, ycenter, half_width, half_height)
pd.rectangle(xcenter, ycenter, half_width, half_height, angle)
pd.filled_rectangle(xcenter, ycenter, half_width, half_height)
pd.filled_rectangle(xcenter, ycenter, half_width, half_height, angle)

pd.ellipse(xcenter, ycenter, half_width, half_height)
pd.ellipse(xcenter, ycenter, half_width, half_height, angle)
pd.filled_ellipse(xcenter, ycenter, half_width, half_height)
pd.filled_ellipse(xcenter, ycenter, half_width, half_height, angle)
```

`xcenter` and `ycenter` are the coordinates of the `center` of the rectangle, **not** one of its corners! `angle` gives the amount of **counter-clockwise** rotation in degrees. `pd.rectangle()` and `pd.ellipse()` draw the outlines of the shapes only. `pd.filled_rectangle()` and `pd.filled_ellipse()` draw filled shapes.

**Sample rectangle program:**

```python
# penndraw_rectangle_test.py
import penndraw as pd
# solid black square centered at (.5, .5)
# with sides of length .6 (half-width of .3)
pd.filled_rectangle(0.5, 0.5, 0.3, .15)

# blue square outline centered at (.7, .3)
# with sides of length .4
# rotated 30 degrees counter-clockwise
pd.set_pen_color(pd.BLUE)
pd.rectangle(.7, .3, .2, .1, 30)

pd.run()
```

---

#### Arcs, Closed Arcs, and Pies

`PennDraw` supports *circular* arcs, or arcs that are part of a circle. Specify them by providing the center and radius of a circle, and the start and end angles of the arc you want to draw. You can also close the arc with a straight line or chord (a "closed arc"), or by connected the ends of the arc back to the center of the circle (a "pie"):

```python
pd.arc(x, y, r, start_angle, end_angle)

pd.closed_arc(x, y, r, start_angle, end_angle)
pd.filled_arc(x, y, r, start_angle, end_angle)

pd.pie(x, y, r, start_angle, end_angle)
pd.filled_pie(x, y, r, start_angle, end_angle)
```

**Sample arc program:**

```python
# Filename: penndraw_arc_test.py
import penndraw as pd
# black arc
pd.arc(0.15, 0.6, 0.3, 10, 100)

# blue closed arc and filled arc
pd.set_pen_color(pd.BLUE)
pd.closed_arc(0.15, 0.3, 0.3, 10, 100)
pd.filled_arc(0.15, 0.0, 0.3, 10, 100)

# red pie and filled pie
pd.set_pen_color(pd.RED)
pd.pie(0.65, 0.6, 0.3, 10, 100)
pd.filled_pie(0.65, 0.1, 0.3, 10, 100)

pd.run()
```

---

#### Polylines and Polygons

Polygons and polylines are closely related: for both you specify a list of coordinates that are connected in order by straight line segments. The difference is that a polygon connects the last point back to the first one to create a closed shape. For each of the functions below, the arguments are the alternating x and y coordinates of the points. You can specify as many points as you like.

```python
pd.polyline(x1, y1, x2, y2, x3, y3, ...)
pd.polygon(x1, y1, x2, y2, x3, y3, ...)
pd.filled_polygon(x1, y1, x2, y2, x3, y3, ...)
```

**Sample polyline/polygon program:**

```python
# Filename: penndraw_polygon_test.py

import penndraw as pd
# three-segment (four-point) black polyline
pd.polyline(0, 0, 0.25, 0, .25, 1, 0, 1)

# blue, five-sided polygon
pd.set_pen_color(pd.BLUE)
pd.polygon(0.5, 0, 1, 0, 1, 0.7, 0.75, 1, 0.5, 0.7)

pd.run()
```

---

#### Images

Drawing images is quite easy:

```python
pd.picture(xcenter, ycenter, filename)
pd.picture(xcenter, ycenter, filename, angle)
pd.picture(xcenter, ycenter, filename, width, height)
pd.picture(xcenter, ycenter, filename, width, height, angle)
```

- `xcenter` and `ycenter` are the coordinate where the image should be centered.
- `filename` is the name of the picture file, this file should be written in quotations with file extensions, for example `"dog.jpg"` would be a valid filename.
- If this point is outside the window, the image will not be drawn at all.
- *angle* is the amount to rotate the image counter-clockwise, in degrees
- The image will be drawn full size unless you specify `width` and `height`. The `width` and `height` values are in **pixels**, not coordinates. If both values are specified, the image will be squashed or stretched to fit. If one of the values is zero, the image will be scaled to fit the other one.
- Use negative `width` and/or `height` values to flip the image.

---

#### Text

**Drawing Text:**

```python
pd.text(x, y, text)
pd.text(x, y, text, angle)

pd.text_left(x, y, text)
pd.text_left(x, y, text, angle)

pd.text_right(x, y, text)
pd.text_right(x, y, text, angle)
```

- `text` must be a single line of text. To draw multiple lines of text, you need to call the `text()` functions once per line, using different y coordinates.
- Text will be drawn in the current line color.
- Remember that text is a string and therefore should be in quotes.

For example:

```python
pd.text(0.4, 0.2, "abc", 30)
```

**Changing the font and size:**

```python
pd.set_font(font_name)
pd.set_font(font_name, point_size)
pd.set_font_size(point_size)
```

- Font sizes are specified in points (i.e. 12 is small-but-legible), not coordinates or pixels.
- In CIS 1100 we recommend that you do not change font **names** because the grading computers have different fonts installed than your PC. If you switch fonts, your drawing is likely to look different to your TA than it does to you. It *is* safe to change the size using `set_font_size()` and to turn bold and italic on and off.

**Listing & Modifying Fonts:**

⚠️⚠️⚠️ These font-related tools are not yet implemented. Using them will crash your program. ⚠️⚠️⚠️

The available fonts vary system by system, and it can be a little difficult to figure out what the names to give `set_font()`. We provide the following function to help you:

`pd.list_fonts()`

- `pd.list_fonts()` prints out a list of all the font names you can use to the Terminal or Command Prompt. Every PC has different fonts installed, so changing fonts is a little dangerous if you want other people to run your program and see the same drawing. (If you ask for a font that isn't installed, Java will substitute another font that may well look completely different.)

You can modify the style of the font using the following functions:

```
pd.set_font_plain()
pd.set_font_bold()
pd.set_font_italic()
pd.set_font_bold_italic()
```

Or, well, you could. But they're not implemented yet. So don't.

---

#### Animation

`PennDraw` provides a function that can be used for creating animations:

```
pd.advance()
```

```python
# Filename: basic_animation.py
import penndraw as pd

# Stuff here will run just once.
pd.set_canvas_size(500, 500)
x_center = 0.5
y_center = 0.5
half_side = 0.1
pd.set_pen_color(pd.HSS_BLUE)

# Stuff indented under "while True:" will
# execute once per "frame" of the animation.
while True:
    pd.clear()
    pd.filled_square(x_center, y_center, half_side)
    x_center += 0.01
    if x_center > 1 + half_side:
        x_center = -half_side
    pd.advance() # necessary to make anim. appear
```

- If you are creating an animation instead of a static drawing, you **should not use `pd.run()`** at the end of the program. 
- Drawing commands will not immediately show up on the screen in animation mode. Instead the drawing will be created in memory, and will only be shown when you call `pd.advance()`. Moreover, `PennDraw` will ensure that new frames are not shown faster than the frame rate you specified.
- If your drawing takes to long to prepare in memory (usually because you have lots of complicated drawing commands), it will not be possible to maintain the frame rate you specified. In this case your animation will be slow and jerky. Your options are to simplify the drawing so it completes faster, or slow down the frame rate to give yourself more time.


---

#### Keyboard and Mouse

`PennDraw` has very basic support for keyboard and mouse input. It is much less powerful than most user interface libraries provide, but also much simpler.

- `pd.mouse_pressed()` returns `True` or `False` to indicate whether a mouse button is currently pressed. Use this inside an animation loop to determine if the user is currently clicking.
- `pd.mouse_x()` returns the x-coordinate of the mouse cursor's current position. It uses the same coordinate system as the drawing commands.
- `pd.mouse_y()` returns the y-coordinate of the mouse cursor's current position.
- `pd.has_next_key_typed()` returns `True` or `False` to indicate whether the user is currently holding down a key in this frame.
- `pd.next_key_typed()` returns the character that the user is currently typing. If the user hasn't typed anything, it will generate a runtime error and your program will crash. If the user is pressing multiple keys at once, one will be selected arbitrarily. This function responds with the correct character if shift is being held.
- `pd.is_key_typed()` allows you to check whether or not specific key is being typed right now. This can be more convenient to use than the `has_next_key_typed`/`next_key_typed` pattern when you're looking to match against a small number of key presses.

To read in a message that a user types in one character at a time, you need to call `pd.next_key_typed()` once for each character the user has typed. The following example builds a String of everything the user has typed so far, then prints it out:

```python
while True:
    s = ""
    if pd.has_next_key_typed(): # make sure there is keyboard input to process
        s += pd.next_key_typed() # read in one character of keyboard input and add it to the end of s
        print(s) # print out the input history
```

