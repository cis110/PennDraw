from pyglet import shapes, gl
import math


class UnfilledRectangle(shapes.Rectangle):
    def __init__(self, x, y, width, height, color, batch=None):
        self._draw_mode = gl.GL_LINES
        super().__init__(x, y, width, height, color=color, batch=batch)

    def _create_vertex_list(self):
        positions = ('f', self._get_vertices())
        colors = ('Bn', self._rgba * 8)
        translations = ('f', (self._x, self._y) * 8)
        self._vertex_list = self._group.program.vertex_list(
            8, self._draw_mode, self._batch, self._group,
            position=positions,
            colors=colors,
            translation=translations)

    def _get_vertices(self):
        if not self._visible:
            return (0, 0) * 8
        else:
            x1 = 0
            x2 = self._width
            y1 = 0
            y2 = self._height

            return (x1, y1, x2, y1, x2, y1, x2, y2, x2, y2, x1, y2, x1, y2, x1, y1)


class UnfilledEllipse(shapes.Ellipse):
    def __init__(self, x, y, a, b, color, batch=None):
        self._draw_mode = gl.GL_LINES
        super().__init__(x, y, a, b, color=color, batch=batch)
        self._num_verts = self._segments * 2

    def _create_vertex_list(self):
        positions = ('f', self._get_vertices())
        # TODO: why does self._num_verts give a length off by self._segments here?
        colors = ('Bn', self._rgba * self._segments * 2)
        translations = ('f', (self._x, self._y) * self._segments * 2)
        self._vertex_list = self._group.program.vertex_list(
            self._segments * 2, self._draw_mode, self._batch, self._group,
            position=positions,
            colors=colors,
            translation=translations)

    def _get_vertices(self):
        if not self._visible:
            return (0, 0) * self._segments * 2
        else:
            x = -self._anchor_x
            y = -self._anchor_y
            tau_segs = math.pi * 2 / self._segments

            points = [(x + self._a * math.cos(i * tau_segs),
                       y + self._b * math.sin(i * tau_segs)) for i in range(self._segments)]

            vertices = []
            for i, point in enumerate(points):
                seg = *points[i - 1], *point
                vertices.extend(seg)

            return vertices
