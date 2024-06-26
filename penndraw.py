import pyglet as pg
from dataclasses import dataclass

from unfilled_shapes import *

DEFAULT_SIZE: int = 512
DEFAULT_MIN_COORD: float = 0.0
DEFAULT_MAX_COORD: float = 1.0
BATCH: pg.graphics.Batch = pg.graphics.Batch()
VERTICES: list = []
BORDER: float = 0.0

BLACK: tuple[int, int, int, int] = (0, 0, 0, 255)
WHITE: tuple[int, int, int, int] = (255, 255, 255, 255)
RED: tuple[int, int, int, int] = (255, 0, 0, 255)
GREEN: tuple[int, int, int, int] = (0, 255, 0, 255)
BLUE: tuple[int, int, int, int] = (0, 0, 255, 255)
YELLOW: tuple[int, int, int, int] = (255, 255, 0, 255)
CYAN: tuple[int, int, int, int] = (0, 255, 255, 255)
MAGENTA: tuple[int, int, int, int] = (255, 0, 255, 255)
DARK_GRAY: tuple[int, int, int, int] = (64, 64, 64, 255)
GRAY: tuple[int, int, int, int] = (128, 128, 128, 255)
LIGHT_GRAY: tuple[int, int, int, int] = (192, 192, 192, 255)
ORANGE: tuple[int, int, int, int] = (255, 200, 0, 255)
PINK: tuple[int, int, int, int] = (255, 175, 175, 255)

HSS_BLUE: tuple[int, int, int] = (31, 119, 180)
HSS_ORANGE: tuple[int, int, int] = (255, 126, 14)
HSS_RED: tuple[int, int, int] = (219, 49, 34)
HSS_YELLOW: tuple[int, int, int] = (255, 219, 128)

TQM_NAVY: tuple[int, int, int] = (0, 51, 102)
TQM_BLUE: tuple[int, int, int] = (24, 123, 205)
TQM_WHITE: tuple[int, int, int] = (245, 240, 236)


height: int = DEFAULT_SIZE
width: int = DEFAULT_SIZE
x_min: float = DEFAULT_MIN_COORD
x_max: float = DEFAULT_MAX_COORD
y_min: float = DEFAULT_MIN_COORD
y_max: float = DEFAULT_MAX_COORD
x_scale: float = width / (x_max - x_min)
y_scale: float = height / (y_max - y_min)

window: pg.window.Window = pg.window.Window(width, height, config=pg.gl.Config(
    double_buffer=True, sample_buffers=1, samples=2))
color: tuple[int, int, int, int] = (255, 255, 255, 255)
pen_radius: float = 0.002

DEFAULT_FONT_NAME: str = "SansSerif"
DEFAULT_FONT_SIZE: float = 12


@dataclass
class FontProperties:
    """Stores all of the current font properties."""
    name: str = DEFAULT_FONT_NAME
    size: float = DEFAULT_FONT_SIZE


font = FontProperties()


def run():
    pg.app.run()


def set_canvas_size(w: int, h: int):
    """Set the size of the canvas to the specified width and height in pixels.
    Raises a ValueError if the width or height is less than 1.
    """

    global width, height
    if (w < 1 or h < 1):
        raise ValueError(
            "Invalid canvas size: width and height must be positive.")
    width = w
    height = h
    window.set_size(w, h)
    set_scale(x_min, x_max)


def set_pen_radius(r: float):
    """Set the radius of the pen to the specified width. The default width is 0.002.
    Raises a ValueError if the radius is negative.
    Raises a TypeError if the radius is not a number.
    """
    if not isinstance(r, (int, float)):
        raise TypeError(
            "Invalid pen radius: must be a number between 0 and 1")
    if r <= 0:
        raise ValueError("Invalid pen radius: must be positive.")
    global pen_radius
    pen_radius = r


def set_pen_color(*args):
    """Set the color of the pen to the specified RGB or RGBA color.

    Usages:
    set_pen_color(r: int, g: int, b: int) -> None
    set_pen_color(r: int, g: int, b: int, a: int) -> None
    set_pen_color(color: tuple[int, int, int]) -> None
    set_pen_color(color: tuple[int, int, int, int]) -> None

    Raises a ValueError if the color is invalid.
    """
    global color
    color = _validate_color(args)


def set_font(*args):
    """Set the font to the specified font name, or reset to the default font if no font is specified.

    Input must be a valid font name.
    Raises a TypeError if the input is not a string.
    Raises a ValueError if the font is not found.
    """
    global font
    if len(args) == 0:
        font.name = DEFAULT_FONT_NAME
    elif not isinstance(args[0], str):
        raise TypeError("Invalid font: must be a string.")
    elif not pg.font.have_font(args[0]):
        raise ValueError("Invalid font: must be a valid font name.")
    font.name = args[0]


def get_font() -> str:
    """Return the current font.
    """
    return font.name


def list_fonts():
    """List all available fonts.

    Raises a NotImplementedError for now. IDK how to do
    this with pyglet; may need to think about it differently.
    """
    raise NotImplementedError("Not yet implemented. 🤷")


def set_font_size(pointSize: float):
    """Set the font size to the specified point size.

    Raises a ValueError if the point size is less than 1.
    """
    if pointSize < 0:
        raise ValueError("Invalid font size: must be non-negative.")
    font.size = pointSize


def _validate_color(args):
    if len(args) == 1:
        if not isinstance(args[0], tuple) or len(args[0]) not in (3, 4) or not all(isinstance(x, int) and 0 <= x <= 255 for x in args[0]):
            raise ValueError(
                "Invalid color: input tuple must consist of 3 or 4 integers between 0-255.")
        if len(args[0]) == 3:
            return args[0] + (255,)
        else:
            return args[0]
    elif len(args) in (3, 4):
        if not all(isinstance(x, int) and 0 <= x <= 255 for x in args):
            raise ValueError(
                "Invalid colors: must have 3 or 4 integer components between 0-255.")
        return args
    else:
        raise ValueError(
            "Invalid number of arguments. Must provide a color in RGB or RGBA format.")


def set_scale(min_c: float, max_c: float):
    """Set the scale of the canvas to the specified minimum and maximum coordinates.
    """

    global x_min, x_max, y_min, y_max
    size = max_c - min_c
    x_min = min_c - BORDER * size
    x_max = max_c + BORDER * size
    y_min = min_c - BORDER * size
    y_max = max_c + BORDER * size
    _set_transform()


def _set_transform():
    global x_scale, y_scale
    x_scale = width / (x_max - x_min)
    y_scale = height / (y_max - y_min)


def _scale_x(x: float) -> float:
    return (x - x_min) * x_scale


def _scale_y(y: float) -> float:
    return (y - y_min) * y_scale


def _factor_x(w: float) -> float:
    return w * width / abs(x_max - x_min)


def _factor_y(h: float) -> float:
    return h * height / abs(y_max - y_min)


def _scaled_pen_radius() -> float:
    return pen_radius * width


def keep(f):
    def wrapper(*args, **kwargs):
        VERTICES.append(f(*args, **kwargs))
    return wrapper


def scale_inputs(f):
    def wrapper(*args, **kwargs):
        return f(*_scale_points(*args), **kwargs)
    return wrapper


def clear(*args):
    """Clear the canvas to a given color.
    """
    global color
    old_color = color
    color = WHITE if not args else _validate_color(args)
    for shape in VERTICES:
        shape.delete()
    VERTICES.clear()
    filled_rectangle((x_min + x_max) / 2, abs(y_min + y_max) / 2,
                     (x_max - x_min) / 2, abs(y_max - y_min) / 2)
    color = old_color


@keep
def __ellipse(x: float, y: float, a: float, b: float, filled: bool):
    x_scaled = _scale_x(x)
    y_scaled = _scale_y(y)
    a_scaled = _factor_x(a)
    b_scaled = _factor_y(b)
    segments = max(50, int(max(a_scaled, b_scaled) / 1.25))

    if (a_scaled < 1 or b_scaled < 1):
        raise ValueError(
            "Invalid ellipse size: width and height must be positive.")

    if not filled:
        _e = UnfilledEllipse(x_scaled, y_scaled, a_scaled,
                             b_scaled, segments, color, batch=BATCH)
        paired = [[a + x_scaled, b + y_scaled] for a, b in zip(
            _e._get_vertices()[::2], _e._get_vertices()[1::2])]
        return pg.shapes.MultiLine(*paired, thickness=_scaled_pen_radius(), closed=True, color=color, batch=BATCH)
    else:
        return pg.shapes.Ellipse(x_scaled, y_scaled, a_scaled, b_scaled, color=color, batch=BATCH, segments=50)


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

    w_scaled = _factor_x(half_width)
    h_scaled = _factor_y(half_height)
    x_scaled = _scale_x(x) - w_scaled
    y_scaled = _scale_y(y) - h_scaled

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
        return pg.shapes.MultiLine(*paired, thickness=_scaled_pen_radius(), closed=True, color=color, batch=BATCH)
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
    x1_scaled = _scale_x(x1)
    y1_scaled = _scale_y(y1)
    x2_scaled = _scale_x(x2)
    y2_scaled = _scale_y(y2)

    return pg.shapes.Line(x1_scaled, y1_scaled, x2_scaled, y2_scaled, width=_scaled_pen_radius(), color=color, batch=BATCH)


def line(x1: float, y1: float, x2: float, y2: float):
    __line(x1, y1, x2, y2)


def _scale_points(*points):
    return (_scale_x(p) if i % 2 == 0 else _scale_y(p) for (i, p) in enumerate(points))


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
    return pg.shapes.MultiLine(*zipped_points, color=color, thickness=_scaled_pen_radius(), batch=BATCH, closed=True)


@keep
def text(x: float, y: float, s: str, angle: float = 0.0, orientation: str = "center") -> pg.text.Label:
    x_scaled = _scale_x(x)
    y_scaled = _scale_y(y)
    return pg.text.Label(s, font_name=font.name, font_size=font.size, rotation=angle, x=x_scaled, y=y_scaled, color=color, batch=BATCH, anchor_x=orientation, anchor_y='center')


def text_left(x: float, y: float, s: str, angle: float = 0.0):
    text(x, y, s, orientation='left')


def text_right(x: float, y: float, s: str, angle: float = 0.0):
    text(x, y, s, orientation='right')


@window.event
def on_draw():
    window.clear()
    BATCH.draw()
