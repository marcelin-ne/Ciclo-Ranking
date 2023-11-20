from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.animation import Animation
from coordinates_control import CoordinatesControl
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import NumericProperty
from kivy.properties import AliasProperty

# Builder.load_file('line_drawer.kv')

class LineDrawer(Widget):
    def __init__(self, **kwargs):
        super(LineDrawer, self).__init__(**kwargs)
        self.bind(size=self.redraw)
        self.redraw()


    #Inicializar las longitudes
    length_h6 = NumericProperty(0.30)
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


        # Inicialización de las coordenadas de la línea
    def draw_line(self, x1, y1, x2, y2, line_id):
        with self.canvas:
            Color(0, 0, 0, 1)
            # Dibuja la línea y almacena una referencia en el diccionario de identificadores
            self.ids[line_id] = Line(points=[x1, y1, x2, y2])

    def modify_line(self, line_id, new_points):
        # Modifica la línea con el identificador dado
        line = self.ids[line_id]
        line.points = new_points

    def animate_line(self, line_id, new_points, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line = self.ids[line_id]
        anim = Animation(points=new_points, duration=duration)
        anim.start(line)
    #Get coordenate of the line
    def get_line_coordinates(self, line_id):
        line = self.ids[line_id]
        return line.points

    def animate_lines_vertical(self,line_id, hs, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line = self.ids[line_id]
        points=[line.points[0], line.points[1]+hs, line.points[2], line.points[3]+hs]
        print(points)
        anim = Animation(points=[line.points[0], line.points[1]+hs, line.points[2], line.points[3]+hs], duration=duration)
        anim.start(line)
        print(line.points)

    def animate_lines_horizontal(self,line_id, hs, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line = self.ids[line_id]
        anim = Animation(points=[line.points[0]+hs, line.points[1], line.points[2]+hs, line.points[3]], duration=duration)
        anim.start(line)

    def draw_base(self):
        # Dibuja las líneas base
        self.draw_line(100, 700, 100, 1000, 'h6a')
        self.draw_line(100, 1000, 400, 1000, 'h6b')
        self.draw_line(890, 950, 890, 550, 'h7a')
        self.draw_line(890, 950, 500, 950, 'h7b')
        self.draw_line(850, 900, 850, 700, 'h8a')
        self.draw_line(625, 900, 850, 900, 'h8b')
        self.draw_line(250, 100, 250, 250, 'h4a')
        self.draw_line(250, 100, 500, 100, 'h4b')
        self.draw_line(275, 125, 275, 250, 'h9a')
        self.draw_line(275, 125, 575, 125, 'h9b')
        self.draw_line(775, 120, 775, 250, 'h3a')
        self.draw_line(575, 120, 775, 120, 'h3b')
        self.draw_line(260, 400, 260, 500, 'h5a')
        self.draw_line(675, 300, 675, 400, 'h2a')
        self.draw_line(675, 400, 680, 460, 'h1a')

    def redraw(self, *args):
        self.canvas.clear()
        #Lineas h6a
        start_x, start_y = self.width * 1.1, self.height * 0.9  # Usando porcentajes para adaptar las coordenadas
        end_x6, end_y6 = start_x, start_y - self.height * 0.15
        self.draw_line(start_x, start_y, end_x6, end_y6, 'h6a')
        #Linea h6b
        end_x6b, end_y6b = start_x + self.width * self.length_h6, start_y
        self.draw_line(start_x,start_y, end_x6b, end_y6b, 'h6b')
        #Dibujar linea que une h6a y h8a
        starx_6h8, starty_6h8 = end_x6b, end_y6b
        endx_6h8, endy_6h8 = starx_6h8+self.width * 0.15 , starty_6h8-self.height * 0.15
        self.draw_line(starx_6h8, starty_6h8, endx_6h8, endy_6h8, '6h8')
        # #Lineas h8a
        start_x8, start_y8 = endx_6h8, endy_6h8
        end_x8, end_y8 = start_x8 + self.width * self.length_h8, start_y8
        self.draw_line(start_x8, start_y8, end_x8, end_y8, 'h8a')
        # Lineas h8b
        start_x8b, start_y8b = end_x8, end_y8
        end_x8b, end_y8b = start_x8b, start_y8b - self.height * self.length_h8
        self.draw_line(start_x8b, start_y8b, end_x8b, end_y8b, 'h8b')
        #Linea que une h8 y h1
        start_x8h1, start_y8h1 = end_x8b, end_y8b
        end_x8h1, end_y8h1 = start_x8h1 - self.width *0.08 , start_y8h1 - self.height * 0.08
        self.draw_line(start_x8h1, start_y8h1, end_x8h1, end_y8h1, 'h8h1')
        #Lineas de h1
        start_x1, start_y1 = end_x8h1, end_y8h1
        end_x1, end_y1 = start_x1 , start_y1 - self.height * self.length_h1
        self.draw_line(start_x1, start_y1, end_x1, end_y1, 'h1')
        #Linea que une h1 y h2
        start_x1h2, start_y1h2 = end_x1, end_y1
        end_x1h2, end_y1h2 = start_x1h2 + self.width * 0.01, start_y1h2 - self.height * 0.06
        self.draw_line(start_x1h2, start_y1h2, end_x1h2, end_y1h2, 'h1h2')
        #Lineas de h2
        start_x2, start_y2 = end_x1h2, end_y1h2
        end_x2, end_y2 = start_x2 , start_y2 - self.height * self.length_h2
        self.draw_line(start_x2, start_y2, end_x2, end_y2, 'h2a')
        #Lineas de h2b
        start_x2b, start_y2b = end_x2, end_y2
        end_x2b, end_y2b = start_x2b - self.width * self.length_h2, start_y2b
        self.draw_line(start_x2b, start_y2b, end_x2b, end_y2b, 'h2b')
        #Linea que une h2 y h9
        start_x2h9, start_y2h9 = end_x2b, end_y2b
        end_x2h9, end_y2h9 = start_x2h9 - self.width * 0.09, start_y2h9 - self.height * 0.06
        self.draw_line(start_x2h9, start_y2h9, end_x2h9, end_y2h9, 'h2h9')
        #Linea h9a
        start_x9, start_y9 = end_x2h9, end_y2h9
        end_x9, end_y9 = start_x9 - self.width * self.length_h9, start_y9
        self.draw_line(start_x9, start_y9, end_x9, end_y9, 'h9a')
        #Linea h9b
        start_x9b, start_y9b = end_x9, end_y9
        end_x9b, end_y9b = start_x9b, start_y9b + self.height * self.length_h9
        self.draw_line(start_x9b, start_y9b, end_x9b, end_y9b, 'h9b')
        #Linea que une h9 y h5
        start_x9h5, start_y9h5 = end_x9b, end_y9b
        end_x9h5, end_y9h5 = start_x9h5, start_y9h5 + self.height * 0.1
        self.draw_line(start_x9h5, start_y9h5, end_x9h5, end_y9h5, 'h9h5')
        #Linea h5a
        start_x5, start_y5 = end_x9h5, end_y9h5
        end_x5, end_y5 = start_x5, start_y5 + self.height * self.length_h5
        self.draw_line(start_x5, start_y5, end_x5, end_y5, 'h5a')
        #Linea que une h5 y h6
        start_x5h6, start_y5h6 = end_x5, end_y5
        end_x5h6, end_y5h6 = end_x6, end_y6
        self.draw_line(start_x5h6, start_y5h6, end_x5h6, end_y5h6, 'h5h6')
        #Linea que une h5 y h4
        start_x5h4, start_y5h4 = start_x5, start_y5
        end_x5h4, end_y5h4 = start_x5h4 - self.width * 0.04, start_y5h4 - self.height * 0.09
        self.draw_line(start_x5h4, start_y5h4, end_x5h4, end_y5h4, 'h5h4')
        #Linea h4a
        start_x4, start_y4 = end_x5h4, end_y5h4
        end_x4, end_y4 = start_x4, start_y4 - self.height * self.length_h4
        self.draw_line(start_x4, start_y4, end_x4, end_y4, 'h4a')
        #Linea h4b
        start_x4b, start_y4b = end_x4, end_y4
        end_x4b, end_y4b = start_x4b + self.width * self.length_h8, start_y4b
        self.draw_line(start_x4b, start_y4b, end_x4b, end_y4b, 'h4b')
        # Linea que une h4 y h7 y h2
        start_x4h7, start_y4h7 = end_x4b, end_y4b
        end_x4h7, end_y4h7 = end_x2h9, end_y2h9
        self.draw_line(start_x4h7, start_y4h7, end_x4h7, end_y4h7, 'h4h7')
        #Linea h3a
        start_x3, start_y3 = end_x4h7, end_y4h7
        end_x3, end_y3 = start_x3+self.width * self.length_h3, start_y3
        self.draw_line(start_x3,start_y3, end_x3, end_y3, 'h3a')
        #Linea h3b
        start_x3b, start_y3b = end_x3, end_y3
        end_x3b, end_y3b = start_x3b, start_y3b + self.height * self.length_h2
        self.draw_line(start_x3b, start_y3b, end_x3b, end_y3b, 'h3b')
        #Linea que une h7 y h3
        starx_7h3, starty_7h3 = end_x3b, end_y3b
        endx_7h3, endy_7h3 = start_x3 + self.width * 0.4 , start_y3 + self.height * 0.3
        self.draw_line(starx_7h3, starty_7h3, endx_7h3, endy_7h3, '7h3')
        #Linea h7a
        start_x7, start_y7 = endx_7h3, endy_7h3
        end_x7, end_y7 = start_x7, start_y7 + self.height * self.length_h7
        self.draw_line(start_x7, start_y7, end_x7, end_y7, 'h7a')
        #Linea h7b
        start_x7b, start_y7b = end_x7, end_y7
        end_x7b, end_y7b = start_x7b - self.width * self.length_h7, start_y7b
        self.draw_line(start_x7b, start_y7b, end_x7b, end_y7b, 'h7b')



    def get_lines_ids(self):
        # Devuelve los identificadores de las líneas
        return self.ids

class LineDrawingApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        # No realices operaciones relacionadas con la interfaz de usuario aquí
        line_drawer = LineDrawer()

        # Llama a la función draw_base para dibujar las líneas base
        line_drawer.redraw()

        return line_drawer

    def on_start(self):
        pass# Establecer la raíz después de realizar las operaciones

if __name__ == '__main__':
    LineDrawingApp().run()
