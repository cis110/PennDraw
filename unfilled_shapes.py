from pyglet import shapes, gl
import math


class UnfilledEllipse(shapes.Ellipse):
    def __init__(self, x, y, a, b, color, batch=None):
        self._draw_mode = gl.GL_LINES
        super().__init__(x, y, a, b, color=color, batch=batch)
        self._num_verts = self._segments * 2

    def _create_vertex_list(self):
        positions = ('f', self._get_vertices())
        colors = ('Bn', self._rgba * self._segments * 2)
        translations = ('f', (self._x, self._y) * self._segments * 2)
        print(len(positions[1]))
        print(len(colors[1]))
        print(len(translations[1]))
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
