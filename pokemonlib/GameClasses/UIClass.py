from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Rectangle(pos=(0,0), size=(100,100))


class GameUI(App):
    def build(self):
        return GameWidget()


app = GameUI()
app.run()

def graphictest():
    a