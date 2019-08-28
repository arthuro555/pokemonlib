from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Rectangle.


class GameUI(App):
    def bulid(self):
        return GameWidget()


def graphictest():
    app = GameUI()
    app.run()