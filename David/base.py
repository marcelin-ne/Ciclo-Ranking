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

        # Ajusta length_h6 en un rango logarítmico entre 0.10 y 0.35
        # Ajusta length_h6 en un rango exponencial entre 0.10 y 0.35
        valor_minimo = 0.20
        valor_maximo = 0.35

    # Ajusta el valor_H6 a un rango exponencial entre 1 y 10000
        valor_H6_ajustado = max(1, min(10000, h6))
        valor_H6_ajustado = math.exp(0.002 * valor_H6_ajustado)  # Puedes ajustar el factor 0.002 según tus necesidades

    # Normaliza el valor_H6 entre 0 y 1
        valor_H6_ajustado = (h6 - 1) / (10000 - 1)

    # Aplica la escala exponencial al rango de 0 a 1
        length_h6_ajustado = valor_minimo + (valor_maximo - valor_minimo) * (
        np.exp(0.002 * valor_H6_ajustado) - np.exp(0)
    ) / (np.exp(0.002 * 1) - np.exp(0))
        responsive_drawing = ResponsiveDrawing()
        print(responsive_drawing.length_h6)
        length_h6_ajustado = float(length_h6_ajustado)
        responsive_drawing.length_h6= length_h6_ajustado
        print(responsive_drawing.length_h6)

        return responsive_drawing

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


