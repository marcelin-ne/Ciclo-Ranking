# responsive_drawing.py
from kivy.uix.widget import Widget
from kivy.graphics import InstructionGroup, Line
from kivy.properties import NumericProperty
from kivy.properties import AliasProperty
from kivy.core.window import Window

class ResponsiveDrawing(Widget):
    length_h6 = NumericProperty(0.45)

    length_h8 = AliasProperty(lambda self: self._get_length_h8(), 
                        None, bind=('length_h6',))
    length_h1 = AliasProperty(lambda self: self._get_length_h1(),
                        None, bind=('length_h6',))
    length_h2 = AliasProperty(lambda self: self._get_length_h2(),
                        None, bind=('length_h6',))
    length_h9 = AliasProperty(lambda self: self._get_length_h9(),
                        None, bind=('length_h6',))
    length_h5 = AliasProperty(lambda self: self._get_length_h5(),
                        None, bind=('length_h6',))
    length_h4 = AliasProperty(lambda self: self._get_length_h4(),
                        None, bind=('length_h6',))
    length_h3 = AliasProperty(lambda self: self._get_length_h3(),
                        None, bind=('length_h6',))
    length_h7= AliasProperty(lambda self: self._get_length_h7(),
                        None, bind=('length_h6',))

    def _get_length_h8(self):
        return self.length_h6 - 0.10
    def _get_length_h1(self):
        return self.length_h6 - 0.25
    def _get_length_h2(self):
        return self.length_h6 - 0.15
    def _get_length_h9(self):
        return self.length_h6 - 0.05
    def _get_length_h5(self):
        return self.length_h6 - 0.23
    def _get_length_h4(self):
        return self.length_h9 + 0.05
    def _get_length_h3(self):
        return self.length_h6 - 0.02
    def _get_length_h7(self):
        return self.length_h6 + 0.11

    def __init__(self, **kwargs):
        super(ResponsiveDrawing, self).__init__(**kwargs)
        self.bind(size=self.redraw)

    def redraw(self, *args):
        self.canvas.clear()

        # Las líneas se dibujan usando Line en lugar de las coordenadas con Line.points
        with self.canvas:
            self.draw_line('line_6a', [1.1, 1.9, 1.1, 1.9 - self.height * self.length_h6])
            self.draw_line('line_6b', [1.1, 1.9, 1.1 + self.width * self.length_h6, 1.9])
            self.draw_line('line_8a', [1.25, 1.75, 1.25 + self.width * self.length_h8, 1.75])
            self.draw_line('line_8b', [1.35, 1.75, 1.35, 1.75 - self.height * self.length_h8])
            self.draw_line('line_8h1', [1.35, 1.65, 1.27, 1.57])
            self.draw_line('line_1', [1.27, 1.57, 1.27, 1.57 - self.height * self.length_h1])
            self.draw_line('line_1h2', [1.28, 1.51, 1.29, 1.45])
            self.draw_line('line_2a', [1.29, 1.45, 1.29, 1.45 - self.height * self.length_h2])
            self.draw_line('line_2b', [1.29 - self.width * self.length_h2, 1.45, 1.29, 1.45])
            self.draw_line('line_2h9', [1.2, 1.39, 1.11, 1.33])
            self.draw_line('line_9a', [1.11, 1.33, 1.11 - self.width * self.length_h9, 1.33])
            self.draw_line('line_9b', [1.11, 1.33, 1.11, 1.33 + self.height * self.length_h9])
            self.draw_line('line9h5', [1.11, 1.43, 1.11, 1.43 + self.height * 0.1])
            self.draw_line('line_5', [1.11, 1.53, 1.11, 1.53 + self.height * self.length_h5])
            self.draw_line('line_5h6', [1.11, 1.53, 1.1, 1.9 - self.height * self.length_h6])
            self.draw_line('line_5h4', [1.07, 1.53, 1.03, 1.44])
            self.draw_line('line_4a', [1.03, 1.44, 1.03, 1.44 - self.height * self.length_h4])
            self.draw_line('line_4b', [1.03 + self.width * self.length_h8, 1.44, 1.03, 1.44])
            self.draw_line('line_4h7', [1.03, 1.54, 1.03, 1.54 + self.height * 0.1])
            self.draw_line('line_3a', [1.03, 1.64, 1.03 + self.width * self.length_h3, 1.64])
            self.draw_line('line_3b', [1.03, 1.64, 1.03, 1.64 + self.height * self.length_h2])
            self.draw_line('line_7h3', [1.16, 1.76, 1.2, 2.06])
            self.draw_line('line_7a', [1.2, 2.06, 1.2, 2.06 + self.height * self.length_h7])
            self.draw_line('line_7b', [1.2 - self.width * self.length_h7, 2.06, 1.2, 2.06])

    def draw_line(self, line_id, points):
        group = InstructionGroup()
        line = Line(points=points, width=2)
        group.add(line)
        self.ids[line_id] = group
        self.canvas.add(group)

# main.py
from kivy.app import App

class TestApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 0)
        return ResponsiveDrawing()

if __name__ == '__main__':
    TestApp().run()
