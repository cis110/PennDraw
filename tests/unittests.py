import unittest
import pyglet as pg
import penndraw as pd
import penndraw.penndraw as core


class SetPenColorErrors(unittest.TestCase):

    def test_set_invalid_color_neg1_0_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(-1, 0, 0)

    def test_set_invalid_color_0_neg1_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, -1, 0)

    def test_set_invalid_color_0_0_neg1(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, -1)

    def test_set_invalid_color_0_0_0_neg1(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, 0, -1)

    def test_set_invalid_color_300_0_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(300, 0, 0)

    def test_set_invalid_color_0_300_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 300, 0)

    def test_set_invalid_color_0_0_300(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, 300)

    def test_set_invalid_color_0_0_0_300(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, 0, 300)

    def test_set_invalid_color_2_args(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0)

    def test_set_invalid_color_5_args(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, 0, 0, 0)

    def test_set_invalid_color_tuple_2(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, 0))

    def test_set_invalid_color_tuple_5(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, 0, 0, 0, 0))

    def test_set_invalid_color_tuple_neg1_0_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((-1, 0, 0))

    def test_set_invalid_color_tuple_0_neg1_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, -1, 0))

    def test_set_invalid_color_tuple_0_0_neg1(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, 0, -1))

    def test_set_invalid_color_tuple_0_0_0_neg1(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, 0, 0, -1))


class SetPenColorAlwaysProducesFourTuple(unittest.TestCase):
    """set_pen_color and clear must always leave color as a 4-tuple (RGBA).
    Previously, the 3-int form returned a 3-tuple without alpha, which
    could crash pyglet when drawing shapes — most visibly via clear(r, g, b),
    which students don't think of as 'setting the pen color'."""

    def setUp(self):
        pd._reset()

    def test_three_ints_produces_four_tuple(self):
        pd.set_pen_color(255, 0, 0)
        self.assertEqual(len(core.color), 4)

    def test_three_ints_alpha_defaults_to_255(self):
        pd.set_pen_color(255, 0, 0)
        self.assertEqual(core.color[3], 255)

    def test_four_ints_produces_four_tuple(self):
        pd.set_pen_color(255, 0, 0, 128)
        self.assertEqual(len(core.color), 4)

    def test_three_tuple_produces_four_tuple(self):
        pd.set_pen_color((255, 0, 0))
        self.assertEqual(len(core.color), 4)

    def test_four_tuple_produces_four_tuple(self):
        pd.set_pen_color((255, 0, 0, 128))
        self.assertEqual(len(core.color), 4)

    def test_clear_with_three_ints_restores_valid_color(self):
        # clear(r, g, b) temporarily sets color to draw the background rect.
        # Afterward it restores the previous color — but the background rect
        # must also be drawn with a valid 4-tuple, not a 3-tuple.
        pd.set_pen_color(0, 0, 255)
        pd.clear(128, 128, 128)
        # pen color should be fully restored
        self.assertEqual(core.color, (0, 0, 255, 255))


class AlwaysPasses(unittest.TestCase):

    def test_always_passes(self):
        self.assertTrue(True)


# ---------------------------------------------------------------------------
# Coordinate transform tests
# ---------------------------------------------------------------------------

class CoordinateTransformTests(unittest.TestCase):

    def setUp(self):
        pd._reset()

    # _scale_x / _scale_y: user position → pixel position (origin-aware)

    def test_scale_x_left_edge(self):
        self.assertAlmostEqual(pd._scale_x(0.0), 0.0)

    def test_scale_x_right_edge(self):
        self.assertAlmostEqual(pd._scale_x(1.0), 512.0)

    def test_scale_x_midpoint(self):
        self.assertAlmostEqual(pd._scale_x(0.5), 256.0)

    def test_scale_y_bottom_edge(self):
        self.assertAlmostEqual(pd._scale_y(0.0), 0.0)

    def test_scale_y_top_edge(self):
        self.assertAlmostEqual(pd._scale_y(1.0), 512.0)

    def test_scale_y_midpoint(self):
        self.assertAlmostEqual(pd._scale_y(0.5), 256.0)

    # _factor_x / _factor_y: user length → pixel length (no origin offset)

    def test_factor_x_full(self):
        self.assertAlmostEqual(pd._factor_x(1.0), 512.0)

    def test_factor_x_half(self):
        self.assertAlmostEqual(pd._factor_x(0.5), 256.0)

    def test_factor_y_full(self):
        self.assertAlmostEqual(pd._factor_y(1.0), 512.0)

    def test_factor_y_half(self):
        self.assertAlmostEqual(pd._factor_y(0.5), 256.0)

    # _user_x / _user_y: pixel position → user position (inverse of _scale)

    def test_user_x_left_edge(self):
        self.assertAlmostEqual(pd._user_x(0.0), 0.0)

    def test_user_x_right_edge(self):
        self.assertAlmostEqual(pd._user_x(512.0), 1.0)

    def test_user_x_midpoint(self):
        self.assertAlmostEqual(pd._user_x(256.0), 0.5)

    def test_user_y_midpoint(self):
        self.assertAlmostEqual(pd._user_y(256.0), 0.5)

    def test_user_x_is_inverse_of_scale_x(self):
        for x in [0.0, 0.25, 0.5, 0.75, 1.0]:
            self.assertAlmostEqual(pd._user_x(pd._scale_x(x)), x)

    def test_user_y_is_inverse_of_scale_y(self):
        for y in [0.0, 0.25, 0.5, 0.75, 1.0]:
            self.assertAlmostEqual(pd._user_y(pd._scale_y(y)), y)

    # Non-default scale

    def test_scale_x_expanded_range(self):
        pd.set_scale(0, 2)
        self.assertAlmostEqual(pd._scale_x(1.0), 256.0)  # midpoint of [0,2]
        self.assertAlmostEqual(pd._scale_x(2.0), 512.0)

    def test_factor_x_expanded_range(self):
        pd.set_scale(0, 2)
        self.assertAlmostEqual(pd._factor_x(1.0), 256.0)  # 1 unit = half the canvas

    def test_user_x_expanded_range(self):
        pd.set_scale(0, 2)
        self.assertAlmostEqual(pd._user_x(256.0), 1.0)

    def test_scale_x_offset_range(self):
        pd.set_scale(-1, 1)
        self.assertAlmostEqual(pd._scale_x(-1.0), 0.0)   # left edge
        self.assertAlmostEqual(pd._scale_x(0.0), 256.0)  # midpoint
        self.assertAlmostEqual(pd._scale_x(1.0), 512.0)  # right edge

    def test_scale_vs_factor_differ_with_offset(self):
        # With a non-zero origin, _scale and _factor give different results
        # for the same numeric input — proving they serve different purposes.
        pd.set_scale(-1, 1)
        # position 0.5 in user space → pixel 384  (origin offset shifts it right)
        self.assertAlmostEqual(pd._scale_x(0.5), 384.0)
        # length 0.5 user units → pixel 128  (no origin offset; range is 2 units wide)
        self.assertAlmostEqual(pd._factor_x(0.5), 128.0)


# ---------------------------------------------------------------------------
# VERTICES inspection tests
# ---------------------------------------------------------------------------

class VerticesInspectionTests(unittest.TestCase):

    def setUp(self):
        pd._reset()

    def test_line_adds_one_vertex(self):
        pd.line(0, 0, 1, 1)
        self.assertEqual(len(core.VERTICES), 1)

    def test_line_type(self):
        pd.line(0, 0, 1, 1)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.Line)

    def test_filled_square_adds_one_vertex(self):
        pd.filled_square(0.5, 0.5, 0.1)
        self.assertEqual(len(core.VERTICES), 1)

    def test_filled_square_type(self):
        pd.filled_square(0.5, 0.5, 0.1)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.Rectangle)

    def test_square_adds_one_vertex(self):
        pd.square(0.5, 0.5, 0.1)
        self.assertEqual(len(core.VERTICES), 1)

    def test_square_type(self):
        pd.square(0.5, 0.5, 0.1)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.MultiLine)

    def test_filled_circle_adds_one_vertex(self):
        pd.filled_circle(0.5, 0.5, 0.1)
        self.assertEqual(len(core.VERTICES), 1)

    def test_filled_circle_type(self):
        pd.filled_circle(0.5, 0.5, 0.1)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.Ellipse)

    def test_circle_adds_one_tracked_vertex(self):
        pd.circle(0.5, 0.5, 0.1)
        self.assertEqual(len(core.VERTICES), 1)

    def test_circle_type(self):
        pd.circle(0.5, 0.5, 0.1)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.MultiLine)

    def test_filled_polygon_type(self):
        pd.filled_polygon(0.2, 0.2, 0.8, 0.2, 0.5, 0.8)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.Polygon)

    def test_polygon_type(self):
        pd.polygon(0.2, 0.2, 0.8, 0.2, 0.5, 0.8)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.MultiLine)

    def test_arc_type(self):
        pd.arc(0.5, 0.5, 0.1, 0, 90)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.MultiLine)

    def test_filled_pie_type(self):
        pd.filled_pie(0.5, 0.5, 0.1, 0, 90)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.Sector)

    def test_text_type(self):
        pd.text(0.5, 0.5, "hello")
        self.assertIsInstance(core.VERTICES[0], pg.text.Label)

    def test_multiple_draws_accumulate(self):
        pd.line(0, 0, 1, 1)
        pd.filled_square(0.5, 0.5, 0.1)
        pd.circle(0.5, 0.5, 0.1)
        self.assertEqual(len(core.VERTICES), 3)

    def test_multiple_same_type_accumulate(self):
        pd.line(0, 0, 1, 1)
        pd.line(0, 1, 1, 0)
        pd.line(0.5, 0, 0.5, 1)
        self.assertEqual(len(core.VERTICES), 3)
        for shape in core.VERTICES:
            self.assertIsInstance(shape, pg.shapes.Line)

    def test_multiple_mixed_types_correct_order(self):
        pd.line(0, 0, 1, 1)
        pd.filled_square(0.5, 0.5, 0.1)
        pd.circle(0.5, 0.5, 0.1)
        pd.filled_polygon(0.2, 0.2, 0.8, 0.2, 0.5, 0.8)
        pd.arc(0.5, 0.5, 0.1, 0, 90)
        self.assertEqual(len(core.VERTICES), 5)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.Line)
        self.assertIsInstance(core.VERTICES[1], pg.shapes.Rectangle)
        self.assertIsInstance(core.VERTICES[2], pg.shapes.MultiLine)
        self.assertIsInstance(core.VERTICES[3], pg.shapes.Polygon)
        self.assertIsInstance(core.VERTICES[4], pg.shapes.MultiLine)

    def test_draw_clear_draw_gives_correct_vertices(self):
        pd.line(0, 0, 1, 1)
        pd.filled_square(0.5, 0.5, 0.1)
        pd.clear()
        pd.circle(0.5, 0.5, 0.1)
        pd.text(0.5, 0.5, "hello")
        # clear() leaves a background Rectangle, then we add 2 more shapes
        self.assertEqual(len(core.VERTICES), 3)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.Rectangle)
        self.assertIsInstance(core.VERTICES[1], pg.shapes.MultiLine)
        self.assertIsInstance(core.VERTICES[2], pg.text.Label)

    def test_clear_leaves_one_background_rect(self):
        pd.line(0, 0, 1, 1)
        pd.filled_square(0.5, 0.5, 0.1)
        pd.clear()
        self.assertEqual(len(core.VERTICES), 1)
        self.assertIsInstance(core.VERTICES[0], pg.shapes.Rectangle)


# ---------------------------------------------------------------------------
# Arc / circle consistency tests
# ---------------------------------------------------------------------------

def _multiline_bounds(shape):
    """Bounding box (x_min, x_max, y_min, y_max) of a MultiLine's coordinates."""
    xs = [p[0] for p in shape._coordinates]
    ys = [p[1] for p in shape._coordinates]
    return min(xs), max(xs), min(ys), max(ys)


class ArcCircleConsistencyTests(unittest.TestCase):
    """circle(x, y, r) and arc(x, y, r, 0, 360) must trace the same curve.
    Historically arc() scaled its radius with _factor_x only and circle()
    was positioned via an anchor hack, so the two shapes ended up at
    different positions (and different sizes on non-square canvases)."""

    def setUp(self):
        pd._reset()

    def assert_same_bounds(self, x, y, r, delta=1.0):
        pd.circle(x, y, r)
        pd.arc(x, y, r, 0, 360)
        circle_bounds = _multiline_bounds(core.VERTICES[0])
        arc_bounds = _multiline_bounds(core.VERTICES[1])
        for c, a in zip(circle_bounds, arc_bounds):
            self.assertAlmostEqual(c, a, delta=delta)

    def test_same_bounds_default_canvas(self):
        self.assert_same_bounds(0.5, 0.5, 0.3)

    def test_same_bounds_off_center(self):
        self.assert_same_bounds(0.25, 0.7, 0.1)

    def test_same_bounds_wide_canvas(self):
        pd.set_canvas_size(800, 400)
        self.assert_same_bounds(0.5, 0.5, 0.3)

    def test_same_bounds_expanded_scale(self):
        pd.set_scale(0, 100)
        self.assert_same_bounds(50, 50, 30)

    def test_circle_bounds_match_user_space(self):
        pd.circle(0.5, 0.5, 0.3)
        x_lo, x_hi, y_lo, y_hi = _multiline_bounds(core.VERTICES[0])
        self.assertAlmostEqual(x_lo, pd._scale_x(0.2), delta=1.0)
        self.assertAlmostEqual(x_hi, pd._scale_x(0.8), delta=1.0)
        self.assertAlmostEqual(y_lo, pd._scale_y(0.2), delta=1.0)
        self.assertAlmostEqual(y_hi, pd._scale_y(0.8), delta=1.0)

    def test_arc_bounds_match_user_space_on_wide_canvas(self):
        # On a non-square canvas a user-space circle is an ellipse in pixel
        # space; arc() must respect both axes' scales just like circle().
        pd.set_canvas_size(800, 400)
        pd.arc(0.5, 0.5, 0.3, 0, 360)
        x_lo, x_hi, y_lo, y_hi = _multiline_bounds(core.VERTICES[0])
        self.assertAlmostEqual(x_hi - x_lo, 2 * pd._factor_x(0.3), delta=2.0)
        self.assertAlmostEqual(y_hi - y_lo, 2 * pd._factor_y(0.3), delta=2.0)


# ---------------------------------------------------------------------------
# Framerate tests
# ---------------------------------------------------------------------------

class FramerateTests(unittest.TestCase):

    def setUp(self):
        pd._reset()

    def test_set_framerate_updates_global(self):
        pd.set_framerate(24)
        self.assertEqual(core.framerate, 24)

    def test_set_framerate_rejects_zero(self):
        with self.assertRaises(ValueError):
            pd.set_framerate(0)

    def test_set_framerate_rejects_negative(self):
        with self.assertRaises(ValueError):
            pd.set_framerate(-30)

    def test_set_framerate_rejects_non_number(self):
        with self.assertRaises(ValueError):
            pd.set_framerate("60")

    def test_advance_paces_to_framerate(self):
        import time
        pd.set_framerate(50)
        for _ in range(3):  # first frames absorb window-setup cost, un-paced
            pd.advance()
        start = time.perf_counter()
        frames = 10
        for _ in range(frames):
            pd.advance()
        elapsed = time.perf_counter() - start
        expected = frames / 50
        self.assertGreaterEqual(elapsed, expected * 0.9)
        self.assertLessEqual(elapsed, expected * 1.5)


# ---------------------------------------------------------------------------
# p5.js-style setup/draw + event-callback API tests
# ---------------------------------------------------------------------------

class CallbackAPITests(unittest.TestCase):

    def setUp(self):
        pd._reset()

    def test_setup_decorator_registers_function(self):
        def my_setup():
            pass
        pd.setup(my_setup)
        self.assertIs(core._SETUP_FN, my_setup)

    def test_draw_decorator_registers_function(self):
        def my_draw():
            pass
        pd.draw(my_draw)
        self.assertIs(core._DRAW_FN, my_draw)

    def test_on_mouse_pressed_decorator_registers(self):
        def handler(x, y):
            pass
        pd.on_mouse_pressed(handler)
        self.assertIs(core._ON_MOUSE_PRESSED, handler)

    def test_on_mouse_released_decorator_registers(self):
        def handler(x, y):
            pass
        pd.on_mouse_released(handler)
        self.assertIs(core._ON_MOUSE_RELEASED, handler)

    def test_on_mouse_dragged_decorator_registers(self):
        def handler(x, y):
            pass
        pd.on_mouse_dragged(handler)
        self.assertIs(core._ON_MOUSE_DRAGGED, handler)

    def test_on_mouse_moved_decorator_registers(self):
        def handler(x, y):
            pass
        pd.on_mouse_moved(handler)
        self.assertIs(core._ON_MOUSE_MOVED, handler)

    def test_on_key_pressed_decorator_registers(self):
        def handler(key):
            pass
        pd.on_key_pressed(handler)
        self.assertIs(core._ON_KEY_PRESSED, handler)

    def test_on_key_released_decorator_registers(self):
        def handler(key):
            pass
        pd.on_key_released(handler)
        self.assertIs(core._ON_KEY_RELEASED, handler)

    def test_decorator_returns_function_unchanged(self):
        def my_draw():
            pass
        result = pd.draw(my_draw)
        self.assertIs(result, my_draw)

    def test_decorator_overwrites_not_stacks(self):
        calls = []
        pd.on_mouse_pressed(lambda x, y: calls.append("first"))
        pd.on_mouse_pressed(lambda x, y: calls.append("second"))
        core._dispatch_mouse_press(100, 100, None, 0)
        self.assertEqual(calls, ["second"])

    def test_dispatch_mouse_press_transforms_coordinates(self):
        received = []
        pd.on_mouse_pressed(lambda x, y: received.append((x, y)))
        core._dispatch_mouse_press(256, 128, None, 0)
        self.assertAlmostEqual(received[0][0], core._user_x(256))
        self.assertAlmostEqual(received[0][1], core._user_y(128))

    def test_dispatch_mouse_release_transforms_coordinates(self):
        received = []
        pd.on_mouse_released(lambda x, y: received.append((x, y)))
        core._dispatch_mouse_release(256, 128, None, 0)
        self.assertAlmostEqual(received[0][0], core._user_x(256))
        self.assertAlmostEqual(received[0][1], core._user_y(128))

    def test_dispatch_mouse_drag_transforms_coordinates(self):
        received = []
        pd.on_mouse_dragged(lambda x, y: received.append((x, y)))
        core._dispatch_mouse_drag(256, 128, 5, 5, None, 0)
        self.assertAlmostEqual(received[0][0], core._user_x(256))
        self.assertAlmostEqual(received[0][1], core._user_y(128))

    def test_dispatch_mouse_motion_transforms_coordinates(self):
        received = []
        pd.on_mouse_moved(lambda x, y: received.append((x, y)))
        core._dispatch_mouse_motion(256, 128, 5, 5)
        self.assertAlmostEqual(received[0][0], core._user_x(256))
        self.assertAlmostEqual(received[0][1], core._user_y(128))

    def test_dispatch_mouse_press_noop_when_unregistered(self):
        core._dispatch_mouse_press(0, 0, None, 0)  # should not raise

    def test_dispatch_key_press_invokes_with_char(self):
        received = []
        pd.on_key_pressed(lambda k: received.append(k))
        core._dispatch_key_press(ord('a'), 0)
        self.assertEqual(received, ['a'])

    def test_dispatch_key_release_invokes_with_char(self):
        received = []
        pd.on_key_released(lambda k: received.append(k))
        core._dispatch_key_release(ord('b'), 0)
        self.assertEqual(received, ['b'])

    def test_dispatch_key_press_uppercases_with_shift_modifier(self):
        received = []
        pd.on_key_pressed(lambda k: received.append(k))
        core._dispatch_key_press(ord('a'), pg.window.key.MOD_SHIFT)
        self.assertEqual(received, ['A'])

    def test_dispatch_key_press_skips_non_printable(self):
        received = []
        pd.on_key_pressed(lambda k: received.append(k))
        core._dispatch_key_press(1, 0)
        self.assertEqual(received, [])

    def test_dispatch_key_press_noop_when_unregistered(self):
        core._dispatch_key_press(ord('a'), 0)  # should not raise

    def test_reset_clears_setup_and_draw(self):
        pd.setup(lambda: None)
        pd.draw(lambda: None)
        pd._reset()
        self.assertIsNone(core._SETUP_FN)
        self.assertIsNone(core._DRAW_FN)

    def test_reset_clears_mouse_callbacks(self):
        pd.on_mouse_pressed(lambda x, y: None)
        pd.on_mouse_released(lambda x, y: None)
        pd.on_mouse_dragged(lambda x, y: None)
        pd.on_mouse_moved(lambda x, y: None)
        pd._reset()
        self.assertIsNone(core._ON_MOUSE_PRESSED)
        self.assertIsNone(core._ON_MOUSE_RELEASED)
        self.assertIsNone(core._ON_MOUSE_DRAGGED)
        self.assertIsNone(core._ON_MOUSE_MOVED)

    def test_reset_clears_key_callbacks(self):
        pd.on_key_pressed(lambda k: None)
        pd.on_key_released(lambda k: None)
        pd._reset()
        self.assertIsNone(core._ON_KEY_PRESSED)
        self.assertIsNone(core._ON_KEY_RELEASED)


# ---------------------------------------------------------------------------
# _reset() correctness tests
# ---------------------------------------------------------------------------

class ResetTests(unittest.TestCase):

    def test_reset_empties_vertices(self):
        pd.line(0, 0, 1, 1)
        pd.line(0, 1, 1, 0)
        pd._reset()
        self.assertEqual(len(core.VERTICES), 0)

    def test_reset_restores_color(self):
        pd.set_pen_color(255, 0, 0)
        pd._reset()
        self.assertEqual(core.color, pd.BLACK)

    def test_reset_restores_pen_radius(self):
        pd.set_pen_radius(0.05)
        pd._reset()
        self.assertAlmostEqual(core.pen_radius, core.DEFAULT_PEN_RADIUS)

    def test_reset_restores_canvas_size(self):
        pd.set_canvas_size(800, 600)
        pd._reset()
        self.assertEqual(core.width, core.DEFAULT_SIZE)
        self.assertEqual(core.height, core.DEFAULT_SIZE)

    def test_reset_restores_scale(self):
        pd.set_scale(0, 100)
        pd._reset()
        self.assertAlmostEqual(core.x_min, core.DEFAULT_MIN_COORD)
        self.assertAlmostEqual(core.x_max, core.DEFAULT_MAX_COORD)
        self.assertAlmostEqual(core.y_min, core.DEFAULT_MIN_COORD)
        self.assertAlmostEqual(core.y_max, core.DEFAULT_MAX_COORD)

    def test_reset_restores_font_size(self):
        pd.set_font_size(48)
        pd._reset()
        self.assertEqual(core.font.size, core.DEFAULT_FONT_SIZE)

    def test_reset_restores_framerate(self):
        pd.enable_animation(30)
        pd._reset()
        self.assertEqual(core.framerate, core.DEFAULT_FRAMERATE)

    def test_reset_is_idempotent(self):
        pd._reset()
        pd._reset()
        self.assertEqual(len(core.VERTICES), 0)
        self.assertEqual(core.color, pd.BLACK)
        self.assertAlmostEqual(core.pen_radius, core.DEFAULT_PEN_RADIUS)


if __name__ == '__main__':
    unittest.main()
