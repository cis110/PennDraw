import pyglet as pg
from multipledispatch import dispatch
from unfilled_shapes import *

DEFAULT_SIZE: int = 512
DEFAULT_MIN_COORD: float = 0.0
DEFAULT_MAX_COORD: float = 1.0
BATCH: pg.graphics.Batch = pg.graphics.Batch()
VERTICES: list = []
BORDER: float = 0.0
height: int = DEFAULT_SIZE
width: int = DEFAULT_SIZE
x_min: float = DEFAULT_MIN_COORD
x_max: float = DEFAULT_MAX_COORD
y_min: float = DEFAULT_MIN_COORD
y_max: float = DEFAULT_MAX_COORD
x_scale: float = width / (x_max - x_min)
y_scale: float = height / (y_max - y_min)
window: pg.window.Window = pg.window.Window(width, height)
color: tuple[int, int, int, int] = (255, 255, 255, 255)


def run():
    pg.app.run()


def set_canvas_size(w: int, h: int):
    global width, height
    if (w < 1 or h < 1):
        raise ValueError(
            "Invalid canvas size: width and height must be positive.")
    width = w
    height = h
    window.set_size(w, h)
    set_scale(x_min, x_max)


# @dispatch(tuple)
# def set_pen_color(c: tuple[int]):
#     global color
#     if not (3 <= len(c) <= 4) or not all(isinstance(x, int) and 0 <= x <= 255 for x in color):
#         raise ValueError(
#             "Invalid color tuple: must have 3 integer components between 0-255.")
#     color = color


# @dispatch(int, int, int)
# def set_pen_color(r: int, g: int, b: int):
#     if not all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)):
#         raise ValueError(
#             "Invalid colors: must have 3 integer components between 0-255.")
#     color = (r, g, b)


def set_pen_color(*args):
    """set_pen_color(r: int, g: int, b: int) -> None
    set_pen_color(r: int, g: int, b: int, a: int) -> None
    set_pen_color(color: tuple[int, int, int]) -> None
    set_pen_color(color: tuple[int, int, int, int]) -> None

    Set the color of the pen to the specified RGB or RGBA color.
    Raises a ValueError if the color is invalid.
    """
    global color
    if len(args) == 1:
        if not isinstance(args[0], tuple) or len(args[0]) not in (3, 4) or not all(isinstance(x, int) and 0 <= x <= 255 for x in args[0]):
            raise ValueError(
                "Invalid color: input tuple must consist of 3 or 4 integers between 0-255.")
        if len(args[0]) == 3:
            color = args[0] + (255,)
        else:
            color = args[0]
    elif len(args) in (3, 4):
        if not all(isinstance(x, int) and 0 <= x <= 255 for x in args):
            raise ValueError(
                "Invalid colors: must have 3 or 4 integer components between 0-255.")
        color = args
    else:
        raise ValueError(
            "Invalid number of arguments. Must provide a color in RGB or RGBA format.")


def set_scale(min_c: float, max_c: float):
    global x_min, x_max, y_min, y_max
    size = max_c - min_c
    x_min = min_c - BORDER * size
    x_max = max_c + BORDER * size
    y_min = min_c - BORDER * size
    y_max = max_c + BORDER * size
    set_transform()


def set_transform():
    global x_scale, y_scale
    x_scale = width / (x_max - x_min)
    y_scale = height / (y_max - y_min)


def scale_x(x: float) -> float:
    return (x - x_min) * x_scale


def scale_y(y: float) -> float:
    return (y - y_min) * y_scale


def factor_x(w: float) -> float:
    return w * width / abs(x_max - x_min)


def factor_y(h: float) -> float:
    return h * height / abs(y_max - y_min)


def keep(f):
    def wrapper(*args, **kwargs):
        VERTICES.append(f(*args, **kwargs))
    return wrapper


@keep
def __ellipse(x: float, y: float, a: float, b: float, filled: bool):
    x_scaled = scale_x(x)
    y_scaled = scale_y(y)
    a_scaled = factor_x(a)
    b_scaled = factor_y(b)

    if (a_scaled < 1 or b_scaled < 1):
        raise ValueError(
            "Invalid ellipse size: width and height must be positive.")

    if not filled:
        return UnfilledEllipse(x_scaled, y_scaled, a_scaled, b_scaled, color, BATCH)
    else:
        return pg.shapes.Ellipse(x_scaled, y_scaled, a_scaled, b_scaled, color, BATCH)


def ellipse(x: float, y: float, a: float, b: float):
    __ellipse(x, y, a, b, False)


def filled_ellipse(x: float, y: float, a: float, b: float):
    __ellipse(x, y, a, b, True)


@keep
def circle(x: float, y: float, radius: float):
    return __ellipse(x, y, radius, radius, False)


@window.event
def on_draw():
    window.clear()
    BATCH.draw()
