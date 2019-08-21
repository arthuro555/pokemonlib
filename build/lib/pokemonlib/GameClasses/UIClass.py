import pyglet
from pyglet.window import key


keyboard = key.KeyStateHandler()
window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world', x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    label.draw()


def graphictest():
    pyglet.app.run()
