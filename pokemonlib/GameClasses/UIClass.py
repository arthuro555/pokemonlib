import cocos
from cocos.director import director
import pyglet
from pyglet.window import key
from cocos.actions import *

director.init(caption="Pokemon")
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)


class GraphicTest(cocos.layer.Layer):
    def __init__(self):
        super(GraphicTest, self).__init__()
        label = cocos.text.Label(
            'Test Screen',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        size = director.get_window_size()
        middle = size[0] / 2, size[1] / 2
        label.position = middle
        mypokemon = cocos.sprite.Sprite('567_0.png')
        mypokemon.position = middle
        mypokemon.scale = 1.5
        mypokemon.velocity = (0, 0)
        self.add(mypokemon, z=1)
        self.add(label)
        mypokemon.do(InputHandle())


class InputHandle(cocos.actions.Move):
    def step(self, dt):
        super(InputHandle, self).step(dt)
        vel_x = keyboard[key.RIGHT] * 500 - keyboard[key.LEFT] * 500
        vel_y = keyboard[key.UP] * 500 - keyboard[key.DOWN] * 500
        print(str(vel_y) + " " + str(vel_x))
        self.target.velocity = (vel_x, vel_y)


def graphictest():
    graphTestLayer = GraphicTest()
    main_scene = cocos.scene.Scene(graphTestLayer)
    director.run(main_scene)
