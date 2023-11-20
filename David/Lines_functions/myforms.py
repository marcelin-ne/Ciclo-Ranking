from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from calculator import Rankine_P_Close
from delimeter import Delimiter
from line_drawer import LineDrawer

Builder.load_file('myform.kv')

class MyForm(BoxLayout):
    line_drawer = LineDrawer()
    def __init__(self,**kwargs):
        super(MyForm, self).__init__(**kwargs)
        self.hs= {}
        self.line_drawer = LineDrawer()
        self.add_widget(self.line_drawer)

    def resolve(self):
        #Create the object
        cr_close=Rankine_P_Close({},{})
        delimeter=Delimiter()
        #cr_open.calc_ciclo_rankine_in_precal_open_water(float(self.ids.pbbp.text), self.ids.pbap.text, self.ids.psal_cald.text, self.ids.tsal_cald.text, self.ids.ns_turb.text, self.ids.ns_bomba.text)
        cr_close.calc_ciclo_rankine_in_precal_close_water(float(self.ids.p1.text), float(self.ids.x1.text), float(self.ids.p2.text), float(self.ids.p3.text), float(self.ids.x3.text), float(self.ids.T6.text), float(self.ids.mp.text), float(self.ids.nb.text), float(self.ids.nt.text))
        print(cr_close.hs)
        print(cr_close.results)
        self.ids.eficiencia_termica.text = str(cr_close.results['eta']) + " %"
        self.ids.trabajo_neto.text = str(cr_close.results['wturb']) + " kJ/kg"
        hs=delimeter.transform_to_distance(cr_close.hs)
        print("Hs desde delimeter")
        print(hs)
        ids=self.line_drawer.get_lines_ids()
        print(ids)
        self.redraw_based_on_hs( hs)

    def redraw_based_on_hs(self, hs):
        #h1a
        self.line_drawer.animate_lines_vertical('h1', hs['h1'])
        #h2
        self.line_drawer.animate_lines_vertical('h2a', hs['h2'])
        #h3
        self.line_drawer.animate_lines_vertical('h3a', hs['h3'])
        #h3b
        self.line_drawer.animate_lines_horizontal('h3b', hs['h3'])
        #h4
        self.line_drawer.animate_lines_vertical('h4a', hs['h4'])
        #h4b
        self.line_drawer.animate_lines_horizontal('h4b', hs['h4s'])
        #h5
        self.line_drawer.animate_lines_vertical('h5a', hs['h5'])
        #h6
        self.line_drawer.animate_lines_vertical('h6a', hs['h6'])
        #h6b
        self.line_drawer.animate_lines_horizontal('h6b', hs['h6s'])
        #h7
        self.line_drawer.animate_lines_vertical('h7a', hs['h7'])
        #h7b
        self.line_drawer.animate_lines_horizontal('h7b', hs['h7s'])
        #h8
        self.line_drawer.animate_lines_vertical('h8a', hs['h8'])
        #h8b
        self.line_drawer.animate_lines_horizontal('h8b', hs['h8'])
        #h9
        self.line_drawer.animate_lines_vertical('h9a', hs['h9'])
        #h9b
        self.line_drawer.animate_lines_horizontal('h9b', hs['h9'])



    def get_hs(self):
        return self.hs
    def set_hs(self, hs):
        self.hs = hs

class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        myform_instance = MyForm()
        return MyForm()

if __name__ == '__main__':
    MyApp().run()
