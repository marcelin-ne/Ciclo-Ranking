from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics import Line


class MyLayout(Widget):
    length = NumericProperty(500)
    length8 = NumericProperty(300)

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

        self.create_lines()  # Llamada al método para crear las líneas

    def create_lines(self):
        start_x, start_y = 100, 100
        start_x6, start_y6 = 100, 1000
        end_x, end_y = start_x + self.length, start_y
        
        start_x8, start_y8 = 800, 900

        with self.canvas:
            # Línea 1
            #Lineas de h6
            self.line_6a= Line(points=[start_x6, start_y6, start_x6, start_y6 - self.length], width=2)
            self.line_6b= Line(points=[start_x6, start_y6, start_x6+self.length, start_y6], width=2)
            #Lineas de h8
            self.line_8a= Line(points=[start_x8, start_y8, start_x8+self.length8, start_y8], width=2)
            self.line_8a= Line(points=[start_x8+self.length8, start_y8, start_x8+self.length8, start_y8-self.length8], width=2)
            
    def on_length(self, instance, value):
        end_x = 100 + value  # Actualiza el punto final basado en el valor de la longitud

        # Actualiza las líneas con la nueva longitud
        self.line_1.points = [100, 100, end_x, 100]
        self.line_2.points = [100, 150, end_x, 150]
        self.line_3.points=[100, 200, end_x, 200]

class TestApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    TestApp().run()
