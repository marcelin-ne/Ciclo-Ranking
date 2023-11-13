import kivy
from kivy.app import App
from kivy.uix.widget import Widget #To use the Widget class
from kivy.properties import ObjectProperty #To use the ObjectProperty class
from kivy.lang import Builder
from kivy.core.window import Window
import math
import numpy as np
#from kivy.uix.image import Image
from lines_responsive import  ResponsiveDrawing


#The first way to load the file
Builder.load_file('base.kv')
#import the class
from base_methods import Rankine_P_Close  # Reemplaza "nombre_del_modulo" con el nombre real del archivo que contiene la clase

#Construct the Layout
class MyLayout(Widget):
    #Create calcular function
    def resolve(self):
        #Create the object
        cr_close=Rankine_P_Close({},{})
        #cr_open.calc_ciclo_rankine_in_precal_open_water(float(self.ids.pbbp.text), self.ids.pbap.text, self.ids.psal_cald.text, self.ids.tsal_cald.text, self.ids.ns_turb.text, self.ids.ns_bomba.text)
        cr_close.calc_ciclo_rankine_in_precal_close_water(float(self.ids.p1.text), float(self.ids.x1.text), float(self.ids.p2.text), float(self.ids.p3.text), float(self.ids.x3.text), float(self.ids.T6.text), float(self.ids.mp.text), float(self.ids.nb.text), float(self.ids.nt.text))
        print(cr_close.hs)
        print(cr_close.results)
        self.ids.eficiencia_termica.text = str(cr_close.results['eta']) + " %"
        self.ids.trabajo_neto.text = str(cr_close.results['wturb']) + " kJ/kg"
        h6 = cr_close.hs['h6']
        h6 = float(h6)

        # Definir los valores extremos de H6 y los correspondientes valores de length_h6
        h6_min = 419.24
        h6_max = 5109.09
        length_h6_min = 0.20
        length_h6_max = 0.35

    # Calcular la proporción de H6 en relación con los valores extremos
        proporción_h6 = (h6 - h6_min) / (h6_max - h6_min)

    # Calcular el valor correspondiente para length_h6 en el rango deseado
        length_h6 = length_h6_min + proporción_h6 * (length_h6_max - length_h6_min)

    # Asegurarse de que length_h6 esté dentro del rango [0.20, 0.35]
        length_h6 = max(min(length_h6, length_h6_max), length_h6_min)


        responsive_drawing = ResponsiveDrawing()
        print(responsive_drawing.length_h6)
        length_h6_ajustado = float(length_h6)
        responsive_drawing.on_length_update(h6)
        responsive_drawing.redraw()
        print(responsive_drawing.length_h6)



    #Create clear function
    def clear(self):
        #Clear the TextInputs
        #Clear the label
        pass

#Call the class
class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()


