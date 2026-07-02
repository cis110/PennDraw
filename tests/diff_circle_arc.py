"""Diagnostic test: pixel-level diff between circle() and arc(0,360).

Run with:  python -m pytest tests/diff_circle_arc.py -s
"""
import penndraw as pd
import penndraw.penndraw as core
import pyglet.gl as gl


def capture():
    core.window.switch_to()
    core.on_draw()
    gl.glFinish()
    core.window.flip()
    gl.glReadBuffer(gl.GL_FRONT)
    fw, fh = core.window.get_framebuffer_size()
    buf = (gl.GLubyte * (4 * fw * fh))()
    gl.glReadPixels(0, 0, fw, fh, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, buf)
    return bytearray(buf), fw, fh


def test_circle_arc_pixel_diff():
    pd._reset()
    pd.set_pen_radius(0.005)
    pd.set_pen_color(pd.RED)
    pd.circle(0.5, 0.5, 0.3)
    pd.set_pen_color(pd.BLUE)
    pd.arc(0.5, 0.5, 0.3, 0, 360)

    data, w, h = capture()

    only_red = only_blue = mixed = 0
    red_samples, blue_samples = [], []
    for i in range(0, len(data), 4):
        r, g, b = data[i], data[i+1], data[i+2]
        is_red  = r > 200 and g < 50 and b < 50
        is_blue = r < 50  and g < 50 and b > 200
        is_mix  = r > 100 and b > 100 and g < 50
        if is_red:
            only_red += 1
            if len(red_samples) < 8:
                px = i // 4
                red_samples.append((px % w, px // w))
        if is_blue:
            only_blue += 1
            if len(blue_samples) < 8:
                px = i // 4
                blue_samples.append((px % w, px // w))
        if is_mix:
            mixed += 1

    print(f'\nframebuffer: {w}x{h}')
    print(f'red pixels (circle):  {only_red}')
    print(f'blue pixels (arc):    {only_blue}')
    print(f'mixed pixels:         {mixed}')
    print(f'first red  samples:   {red_samples}')
    print(f'first blue samples:   {blue_samples}')

    # Not asserting anything — just reporting the diff
    assert True
