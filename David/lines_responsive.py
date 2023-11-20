from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.properties import NumericProperty
from kivy.properties import AliasProperty
from kivy.core.window import Window
class ResponsiveDrawing(Widget):
    #Inicializar las longitudes
    length_h6=NumericProperty(0.20)
    length_h8=NumericProperty(0.20)
    length_h1=NumericProperty(0.20)
    length_h2=NumericProperty(0.20)
    length_h9=NumericProperty(0.20)
    length_h5=NumericProperty(0.20)
    length_h4=NumericProperty(0.20)
    length_h3=NumericProperty(0.20)
    length_h7=NumericProperty(0.20)

    #Contructor de la clase con h6 de parametro 
    def __init__(self, h6:float, **kwargs):
        super(ResponsiveDrawing, self).__init__(**kwargs)
        self.length_h6 = h6
        self.bind(size=self.redraw)

    def update_and_redraw(self, new_h6):
        # Actualizar el valor de length_h6
        self.length_h6 = new_h6
    # Forzar una actualización de las longitudes dependientes
        self.dispatch('on_length_update')
    # Volver a dibujar el widget
        self.redraw()

    def on_length_update(self, *args):
        length_h6 = NumericProperty(0.20)
        # Creamos un AliasProperty para length_h8 que esté vinculado a length_h6
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
        # Obtener el valor de length_h6 y calcular length_h8
        return self.length_h6 - 0.10
    def _get_length_h1(self):
        # Obtener el valor de length_h6 y calcular length_h8
        return self.length_h6 - 0.25
    def _get_length_h2(self):
        # Obtener el valor de length_h6 y calcular length_h8
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

    def update_and_redraw(self, new_h6):
        # Actualiza el valor de length_h6
        self.length_h6 = new_h6
        # Vuelve a dibujar el widget
        self.redraw()

    def redraw(self, *args):
        self.canvas.clear()
        #Lineas h6a
        start_x, start_y = self.width * 1.2, self.height * 1.0  # Usando porcentajes para adaptar las coordenadas
        end_x6, end_y6 = start_x, start_y - self.height * self.length_h6
        #Linea h6b
        end_x6b, end_y6b = start_x + self.width * self.length_h6, start_y
        #Dibujar linea que une h6a y h8a
        starx_6h8, starty_6h8 = end_x6b, end_y6b
        endx_6h8, endy_6h8 = starx_6h8+self.width * 0.15 , starty_6h8-self.height * 0.15
        # #Lineas h8a
        start_x8, start_y8 = endx_6h8, endy_6h8
        end_x8, end_y8 = start_x8 + self.width * self.length_h8, start_y8
        # Lineas h8b
        start_x8b, start_y8b = end_x8, end_y8
        end_x8b, end_y8b = start_x8b, start_y8b - self.height * self.length_h8
        #Linea que une h8 y h1
        start_x8h1, start_y8h1 = end_x8b, end_y8b
        end_x8h1, end_y8h1 = start_x8h1 - self.width *0.08 , start_y8h1 - self.height * 0.08
        #Lineas de h1
        start_x1, start_y1 = end_x8h1, end_y8h1
        end_x1, end_y1 = start_x1 , start_y1 - self.height * self.length_h1
        #Linea que une h1 y h2
        start_x1h2, start_y1h2 = end_x1, end_y1
        end_x1h2, end_y1h2 = start_x1h2 + self.width * 0.01, start_y1h2 - self.height * 0.06
        #Lineas de h2
        start_x2, start_y2 = end_x1h2, end_y1h2
        end_x2, end_y2 = start_x2 , start_y2 - self.height * self.length_h2
        #Lineas de h2b
        start_x2b, start_y2b = end_x2, end_y2
        end_x2b, end_y2b = start_x2b - self.width * self.length_h2, start_y2b
        #Linea que une h2 y h9
        start_x2h9, start_y2h9 = end_x2b, end_y2b
        end_x2h9, end_y2h9 = start_x2h9 - self.width * 0.09, start_y2h9 - self.height * 0.06
        #Linea h9a
        start_x9, start_y9 = end_x2h9, end_y2h9
        end_x9, end_y9 = start_x9 - self.width * self.length_h9, start_y9
        #Linea h9b
        start_x9b, start_y9b = end_x9, end_y9
        end_x9b, end_y9b = start_x9b, start_y9b + self.height * self.length_h9
        #Linea que une h9 y h5
        start_x9h5, start_y9h5 = end_x9b, end_y9b
        end_x9h5, end_y9h5 = start_x9h5, start_y9h5 + self.height * 0.1
        #Linea h5a
        start_x5, start_y5 = end_x9h5, end_y9h5
        end_x5, end_y5 = start_x5, start_y5 + self.height * self.length_h5
        #Linea que une h5 y h6
        start_x5h6, start_y5h6 = end_x5, end_y5
        end_x5h6, end_y5h6 = end_x6, end_y6
        #Linea que une h5 y h4
        start_x5h4, start_y5h4 = start_x5, start_y5
        end_x5h4, end_y5h4 = start_x5h4 - self.width * 0.04, start_y5h4 - self.height * 0.09
        #Linea h4a
        start_x4, start_y4 = end_x5h4, end_y5h4
        end_x4, end_y4 = start_x4, start_y4 - self.height * self.length_h4
        #Linea h4b
        start_x4b, start_y4b = end_x4, end_y4
        end_x4b, end_y4b = start_x4b + self.width * self.length_h8, start_y4b
        # Linea que une h4 y h7 y h2
        start_x4h7, start_y4h7 = end_x4b, end_y4b
        end_x4h7, end_y4h7 = end_x2h9, end_y2h9
        #Linea h3a
        start_x3, start_y3 = end_x4h7, end_y4h7
        end_x3, end_y3 = start_x3+self.width * self.length_h3, start_y3
        #Linea h3b
        start_x3b, start_y3b = end_x3, end_y3
        end_x3b, end_y3b = start_x3b, start_y3b + self.height * self.length_h2
        #Linea que une h7 y h3
        starx_7h3, starty_7h3 = end_x3b, end_y3b
        endx_7h3, endy_7h3 = start_x3 + self.width * 0.4 , start_y3 + self.height * 0.3
        #Linea h7a
        start_x7, start_y7 = endx_7h3, endy_7h3
        end_x7, end_y7 = start_x7, start_y7 + self.height * self.length_h7
        #Linea h7b
        start_x7b, start_y7b = end_x7, end_y7
        end_x7b, end_y7b = start_x7b - self.width * self.length_h7, start_y7b

        with self.canvas:
            Color(0, 0, 0)
            #Dibujar Lineas h6a
            self.line_6a=Line(points=[start_x, start_y, end_x6, end_y6], width=6)
            self.line_6b=Line(points=[start_x, start_y, end_x6b,end_y6b], width=6)
            # #Dibujar Lineas h8a
            self.line_8a=Line(points=[start_x8, start_y8, end_x8, end_y8], width=6)
            self.line_8b=Line(points=[start_x8b, start_y8b, end_x8b, end_y8b], width=6)
            # #Dibujar linea que une h6a y h8a
            #self.line_6h8=Line(points=[starx_6h8, starty_6h8, endx_6h8, endy_6h8], width=2)
            #Dibujar linea que une h8 y h1
            self.line_8h1=Line(points=[start_x8h1, start_y8h1, end_x8h1, end_y8h1], width=2)
            #Dibujar Lineas h1
            self.line_1=Line(points=[start_x1, start_y1, end_x1, end_y1], width=6)
            #Dibujar lineas que une h1 y h2
            self.line_1h2=Line(points=[start_x1h2, start_y1h2, end_x1h2, end_y1h2], width=2)
            #Dibujar lineas de h2
            self.line_2a=Line(points=[start_x2, start_y2, end_x2, end_y2], width=6)
            self.line_2b=Line(points=[start_x2b, start_y2b, end_x2b, end_y2b], width=6)
            #Dibujar linea que une h2 y h9
            self.line_2h9=Line(points=[start_x2h9, start_y2h9, end_x2h9, end_y2h9], width=2)
            #Dibujar linea h9
            self.line_9a=Line(points=[start_x9, start_y9, end_x9, end_y9], width=6)
            self.line_9b=Line(points=[start_x9b, start_y9b, end_x9b, end_y9b], width=6)
            #Linea que une h9 y h5
            self.line9h5=Line(points=[start_x9h5, start_y9h5, end_x9h5, end_y9h5], width=2)
            #Dibujar linea h5
            self.line_5=Line(points=[start_x5, start_y5, end_x5, end_y5], width=6)
            #Dibujar linea que une h5 y h6
            self.line_5h6=Line(points=[start_x5h6, start_y5h6, end_x5h6, end_y5h6], width=2)
            #Dibujar la linea que une h5 y h4
            self.line_5h4=Line(points=[start_x5h4, start_y5h4, end_x5h4, end_y5h4], width=2)
            #Dibujar linea h4a
            self.line_4a=Line(points=[start_x4, start_y4, end_x4, end_y4], width=6)
            #Dibujar linea h4b
            self.line_4b=Line(points=[start_x4b, start_y4b, end_x4b, end_y4b], width=4)
            #Dibujar linea que une h4 , h3 y h2
            self.line_4h7=Line(points=[start_x4h7, start_y4h7, end_x4h7, end_y4h7], width=2)
            #Dibujar linea h3a
            self.line_3a=Line(points=[start_x3, start_y3, end_x3, end_y3], width=6)
            #Dibujar linea h3b
            self.line_3b=Line(points=[start_x3b, start_y3b, end_x3b, end_y3b], width=6)
            #Dibujar linea que une h7 y h3
            self.line_7h3=Line(points=[starx_7h3, starty_7h3, endx_7h3, endy_7h3], width=2)
            #Dibujar linea h7a
            self.line_7a=Line(points=[start_x7, start_y7, end_x7, end_y7], width=6)
            #Dibujar linea h7b
            self.line_7b=Line(points=[start_x7b, start_y7b, end_x7b, end_y7b], width=6)

class TestApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 0)
        return ResponsiveDrawing()

if __name__ == '__main__':
    TestApp().run()
