import pyglet
from pyglet.window import key


def graphictest():
    keyboard = key.KeyStateHandler()
    window = pyglet.window.Window()
    label = pyglet.text.Label('Hello, world', x=window.width // 2, y=window.height // 2,
                              anchor_x='center', anchor_y='center')

    def update(dt):
        print(dt)  # time elapsed since last time we were called
        label.x += 1
        label.y += 1

    @window.event
    def on_draw():
        window.clear()
        label.draw()

    pyglet.clock.schedule(update)
    pyglet.app.run()
