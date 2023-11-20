from line_drawer import LineDrawer

class Delimiter:
    #This class is a delimiter for the drawing of the lines

    def __init__(self, **kwargs):
        super(Delimiter, self).__init__(**kwargs)
        self.distance = {}
        self.hs= {}

    def get_hs_from_form(self):
        self.hs = self.form.get_hs()
        return self.hs

    def transform_to_distance(self,hs):
        # Nuevo diccionario para almacenar los valores transformados
        for key, value in hs.items():
        # Convierte el valor a un entero dividiéndolo por 10
            transformed_value = int(float(value) / 10)
        # Agrega el par clave-valor al diccionario distance
            self.distance[key] = transformed_value
        # Devuelve el diccionario distance
        return self.distance


    #Return every element of the dictionary distance individually
    def get_distance(self, key):
        return self.distance[key]



