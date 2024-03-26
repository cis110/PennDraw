import pyglet as pg

DEFAULT_SIZE: int = 512
BATCH: pg.graphics.Batch = pg.graphics.Batch()
VERTICES: list = []
hight: int = DEFAULT_SIZE
width: int = DEFAULT_SIZE
window: pg.window.Window = pg.window.Window(width, hight)


def run():
    pg.app.run()


def set_canvas_size(w: int, h: int):
    if (w < 1 or h < 1):
        raise ValueError(
            "Invalid canvas size: width and height must be positive.")
    width = w
    height = h
    window.set_size(w, h)


def keep(f):
    def wrapper(*args, **kwargs):
        VERTICES.append(f(*args, **kwargs))
    return wrapper


@keep
def circle(x: int, y: int, radius: int):
    return pg.shapes.Circle(
        x, y, radius, color=(255, 255, 255), batch=BATCH)


@window.event
def on_draw():
    window.clear()
    BATCH.draw()
