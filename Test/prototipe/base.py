import kivy
from kivy.app import App
from kivy.uix.widget import Widget #To use the Widget class
from kivy.properties import ObjectProperty #To use the ObjectProperty class
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.image import Image
from lines_responsive import  ResponsiveDrawing


#The first way to load the file
Builder.load_file('base.kv')
#import the class
from base_methods import Rankine_P_Open  # Reemplaza "nombre_del_modulo" con el nombre real del archivo que contiene la clase

#Construct the Layout
class MyLayout(Widget):
    #Create calcular function
    def resolve(self):
        #Create the object
        cr_open=Rankine_P_Open({},{})
        #cr_open.calc_ciclo_rankine_in_precal_open_water(float(self.ids.pbbp.text), self.ids.pbap.text, self.ids.psal_cald.text, self.ids.tsal_cald.text, self.ids.ns_turb.text, self.ids.ns_bomba.text)
        cr_open.calc_ciclo_rankine_in_precal_open_water(float(self.ids.pbbp.text), float(self.ids.pbap.text), float(self.ids.psal_cald.text), float(self.ids.tsal_cald.text), float(self.ids.ns_turb.text), float(self.ids.ns_bomba.text))
        print(cr_open.hs)
        print(cr_open.results)
        self.ids.eficiencia_termica.text = str(cr_open.results['e_termica']) + " %"
        self.ids.trabajo_neto.text = str(cr_open.results['wturb']) + " kJ/kg"
    #Create clear function
    def clear(self):
        #Clear the TextInputs
        #Clear the label
        pass

#Call the class
class AwesomeApp(App):
    def build(self):
        #Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()


