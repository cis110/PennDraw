"""Visual tests for penndraw.

These tests render shapes and sample the resulting pixel data to verify
correctness. They require a display (macOS or X11) and are intended to
be run locally rather than in headless CI.

Rendering constraint: without a running pyglet event loop, only
pg.shapes.MultiLine reliably commits its pixels to the framebuffer in time
for glReadPixels. pg.shapes.Line, pg.shapes.Ellipse and pg.shapes.Arc (for
partial angles) do not. Tests that need a line use polyline() (two-point
MultiLine) rather than line() (pg.shapes.Line). The arc/circle consistency
tests work because circle() uses MultiLine for its outline.

"""

import unittest
import pyglet.gl as gl
import penndraw as pd
import penndraw.penndraw as core


# ---------------------------------------------------------------------------
# Pixel capture helpers
# ---------------------------------------------------------------------------

def _capture():
    """Render the current frame and return (pixels, width, height).

    pixels is a bytearray in RGBA format with OpenGL's bottom-left origin.
    """
    w, h = core.width, core.height
    core.window.switch_to()
    core.on_draw()
    gl.glFinish()
    core.window.flip()
    gl.glReadBuffer(gl.GL_FRONT)
    buf = (gl.GLubyte * (4 * w * h))()
    gl.glReadPixels(0, 0, w, h, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, buf)
    return bytearray(buf), w, h


def _pixel(data, x, y, w, h):
    """Return (R, G, B, A) at screen coordinate (x, y) where (0, 0) is top-left."""
    gl_y = h - 1 - y  # flip: OpenGL y=0 is bottom, screen y=0 is top
    idx = (gl_y * w + x) * 4
    return tuple(data[idx: idx + 4])


def _count_matching(data, r, g, b, tol=20):
    """Count pixels within `tol` of (r, g, b) across the entire frame."""
    count = 0
    for i in range(0, len(data), 4):
        if (abs(data[i]     - r) <= tol and
                abs(data[i + 1] - g) <= tol and
                abs(data[i + 2] - b) <= tol):
            count += 1
    return count


# ---------------------------------------------------------------------------
# Basic rendering tests
# (using MultiLine-based shapes, which reliably commit without an event loop)
# ---------------------------------------------------------------------------

class BasicRenderingTests(unittest.TestCase):

    def setUp(self):
        pd._reset()

    def test_polyline_has_colored_pixels(self):
        # polyline() uses MultiLine which renders without an event loop.
        # line() uses pg.shapes.Line which does not render without an event loop.
        pd.set_pen_color(pd.RED)
        pd.set_pen_radius(0.01)
        pd.polyline(0.2, 0.5, 0.8, 0.5)
        data, w, h = _capture()
        self.assertGreater(_count_matching(data, 255, 0, 0), 10)

    def test_polyline_far_corner_is_background(self):
        pd.set_pen_color(pd.RED)
        pd.set_pen_radius(0.01)
        pd.polyline(0.2, 0.5, 0.8, 0.5)
        data, w, h = _capture()
        r, g, b, _ = _pixel(data, 5, 5, w, h)
        self.assertGreater(r, 200)
        self.assertGreater(g, 200)
        self.assertGreater(b, 200)

    def test_circle_outline_has_colored_pixels(self):
        pd.set_pen_color(pd.RED)
        pd.set_pen_radius(0.01)
        pd.circle(0.5, 0.5, 0.25)
        data, w, h = _capture()
        self.assertGreater(_count_matching(data, 255, 0, 0), 10)

    def test_square_outline_has_colored_pixels(self):
        pd.set_pen_color(pd.BLUE)
        pd.set_pen_radius(0.01)
        pd.square(0.5, 0.5, 0.2)
        data, w, h = _capture()
        self.assertGreater(_count_matching(data, 0, 0, 255), 10)

    def test_full_arc_has_colored_pixels(self):
        # arc(0, 360) produces a closed MultiLine (full circle) which renders
        # without an event loop. Partial arcs (pg.shapes.Arc) do not.
        pd.set_pen_color(pd.RED)
        pd.set_pen_radius(0.01)
        pd.arc(0.5, 0.5, 0.25, 0, 360)
        data, w, h = _capture()
        self.assertGreater(_count_matching(data, 255, 0, 0), 10)

    def test_pen_color_change_is_reflected(self):
        # Capture a red circle, then reset and capture a blue circle.
        # Two MultiLine shapes in the same batch don't both render reliably
        # without the event loop, so we verify each color independently.
        pd.set_pen_color(pd.RED)
        pd.set_pen_radius(0.01)
        pd.circle(0.5, 0.5, 0.2)
        data_red, _, _ = _capture()
        red_count = _count_matching(data_red, 255, 0, 0)

        pd._reset()
        pd.set_pen_color(pd.BLUE)
        pd.set_pen_radius(0.01)
        pd.circle(0.5, 0.5, 0.2)
        data_blue, _, _ = _capture()
        blue_count = _count_matching(data_blue, 0, 0, 255)

        self.assertGreater(red_count, 5)
        self.assertGreater(blue_count, 5)


# ---------------------------------------------------------------------------
# Arc/ellipse consistency tests
# ---------------------------------------------------------------------------

class ArcEllipseConsistencyTests(unittest.TestCase):
    """Tests for consistency between arc() and circle().

    arc() computes its radius using only _factor_x, while circle() uses both
    _factor_x and _factor_y. On a square canvas with equal scales they look
    the same; on a non-square canvas they diverge.
    """

    def setUp(self):
        pd._reset()

    def test_full_arc_and_circle_similar_pixel_count_square_canvas(self):
        # On a square canvas _factor_x == _factor_y, so arc(0,360) and circle()
        # should produce nearly the same number of colored pixels.
        pd.set_pen_color(pd.RED)
        pd.set_pen_radius(0.005)
        pd.arc(0.5, 0.5, 0.2, 0, 360)
        data_arc, w, h = _capture()
        count_arc = _count_matching(data_arc, 255, 0, 0)

        pd._reset()
        pd.set_pen_color(pd.RED)
        pd.set_pen_radius(0.005)
        pd.circle(0.5, 0.5, 0.2)
        data_circle, w, h = _capture()
        count_circle = _count_matching(data_circle, 255, 0, 0)

        self.assertGreater(count_arc, 0)
        self.assertGreater(count_circle, 0)
        ratio = count_arc / count_circle
        self.assertAlmostEqual(ratio, 1.0, delta=0.25,
            msg=f"arc(0,360) covers {count_arc}px, circle() covers {count_circle}px "
                f"(ratio {ratio:.2f}) — should be ~1.0 on a square canvas")

    def test_full_arc_and_circle_similar_pixel_count_nonsquare_canvas(self):
        # On a non-square canvas, arc() and circle() should still cover a
        # similar number of pixels because both now use _factor_x and _factor_y.
        pd.set_canvas_size(512, 256)
        pd.set_pen_color(pd.RED)
        pd.set_pen_radius(0.005)
        pd.arc(0.5, 0.5, 0.2, 0, 360)
        data_arc, w, h = _capture()
        count_arc = _count_matching(data_arc, 255, 0, 0)

        pd._reset()
        pd.set_canvas_size(512, 256)
        pd.set_pen_color(pd.RED)
        pd.set_pen_radius(0.005)
        pd.circle(0.5, 0.5, 0.2)
        data_circle, w, h = _capture()
        count_circle = _count_matching(data_circle, 255, 0, 0)

        self.assertGreater(count_arc, 0)
        self.assertGreater(count_circle, 0)
        ratio = count_arc / count_circle
        self.assertAlmostEqual(ratio, 1.0, delta=0.25,
            msg=f"arc(0,360) covers {count_arc}px, circle() covers {count_circle}px "
                f"(ratio {ratio:.2f}) — should be ~1.0 on any canvas")


if __name__ == '__main__':
    unittest.main()
