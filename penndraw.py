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
pen_radius: float = 0.002


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


def set_pen_radius(r: float):
    global pen_radius
    if not isinstance(r, (int, float)):
        raise TypeError(
            "Invalid pen radius: must be a number between 0 and 1")
    if r <= 0:
        raise ValueError("Invalid pen radius: must be positive.")
    pen_radius = r


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


def scaled_pen_radius() -> float:
    return pen_radius * width


def keep(f):
    def wrapper(*args, **kwargs):
        VERTICES.append(f(*args, **kwargs))
    return wrapper


def scale_inputs(f):
    def wrapper(*args, **kwargs):
        print(*_scale_points(*args))
        return f(*_scale_points(*args), **kwargs)
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
        _e = UnfilledEllipse(x_scaled, y_scaled, a_scaled,
                             b_scaled, color=color, batch=BATCH)
        paired = [[a + x_scaled, b + y_scaled] for a, b in zip(
            _e._get_vertices()[::2], _e._get_vertices()[1::2])]
        return pg.shapes.MultiLine(*paired, thickness=scaled_pen_radius(), closed=True, color=color, batch=BATCH)
    else:
        return pg.shapes.Ellipse(x_scaled, y_scaled, a_scaled, b_scaled, color=color, batch=BATCH)


def ellipse(x: float, y: float, a: float, b: float):
    __ellipse(x, y, a, b, False)


def filled_ellipse(x: float, y: float, a: float, b: float):
    __ellipse(x, y, a, b, True)


def circle(x: float, y: float, radius: float):
    __ellipse(x, y, radius, radius, False)


def filled_circle(x: float, y: float, radius: float):
    __ellipse(x, y, radius, radius, True)


@keep
def __rectangle(x: float, y: float, half_width: float, half_height: float, filled: bool):

    w_scaled = factor_x(half_width)
    h_scaled = factor_y(half_height)
    x_scaled = scale_x(x) - w_scaled
    y_scaled = scale_y(y) - h_scaled
    print(w_scaled, h_scaled, x_scaled, y_scaled)

    if (w_scaled < 1 or h_scaled < 1):
        raise ValueError(
            "Invalid rectangle size: half_width and half_height must be positive.")

    if not filled:
        _r = UnfilledRectangle(x_scaled, y_scaled, 2 *
                               w_scaled, 2 * h_scaled, color=color, batch=BATCH)
        paired = [[a + x_scaled, b + y_scaled] for a, b in zip(
            _r._get_vertices()[::2], _r._get_vertices()[1::2])]
        # add a repeat of the second vertex to avoid the weird line cap issue
        paired.append(paired[1])
        return pg.shapes.MultiLine(*paired, thickness=scaled_pen_radius(), closed=True, color=color, batch=BATCH)
    else:
        return pg.shapes.Rectangle(x_scaled, y_scaled, 2 * w_scaled, 2 * h_scaled, color=color, batch=BATCH)


def rectangle(x: float, y: float, half_width: float, half_height: float):
    __rectangle(x, y, half_width, half_height, False)


def filled_rectangle(x: float, y: float, half_width: float, half_height: float):
    __rectangle(x, y, half_width, half_height, True)


def square(x: float, y: float, half_side_length: float):
    __rectangle(x, y, half_side_length, half_side_length, False)


def filled_square(x: float, y: float, half_side_length: float):
    __rectangle(x, y, half_side_length, half_side_length, True)


@keep
def __line(x1: float, y1: float, x2: float, y2: float):
    x1_scaled = scale_x(x1)
    y1_scaled = scale_y(y1)
    x2_scaled = scale_x(x2)
    y2_scaled = scale_y(y2)

    return pg.shapes.Line(x1_scaled, y1_scaled, x2_scaled, y2_scaled, width=scaled_pen_radius(), color=color, batch=BATCH)


def line(x1: float, y1: float, x2: float, y2: float):
    __line(x1, y1, x2, y2)


def _scale_points(*points):
    return (scale_x(p) if i % 2 == 0 else scale_y(p) for (i, p) in enumerate(points))


@keep
@scale_inputs
def filled_polygon(*points):
    if len(points) % 2 != 0:
        raise ValueError(
            "Invalid polygon: must provide an even number of points.")
    zipped_points = zip(points[::2], points[1::2])
    return pg.shapes.Polygon(*zipped_points, color=color, batch=BATCH)


@keep
@scale_inputs
def polygon(*points):
    if len(points) % 2 != 0:
        raise ValueError(
            "Invalid polygon: must provide an even number of points.")
    zipped_points = zip(points[::2], points[1::2])
    return pg.shapes.MultiLine(*zipped_points, color=color, thickness=scaled_pen_radius(), batch=BATCH, closed=True)


@window.event
def on_draw():
    window.clear()
    BATCH.draw()
