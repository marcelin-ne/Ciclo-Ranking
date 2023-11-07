import CoolProp.CoolProp as CP 

# CICLO RANKINE CON PRECALENTADOR DE AGUA ABIERTO
class Rankine_P_Open:    
    def __init__(self, hs: dict, results: dict):
        """
        Constructor de la clase Rankine_P_Open.

        :param hs: Un diccionario de valores hs.
        :type hs: dict
        :param results: Un diccionario de resultados.
        :type results: dict
        """
        self.hs = hs
        self.results = results
#Metodos

    def calc_ciclo_rankine_in_precal_open_water(self,pbbp, pbap, psal_cald, tsal_cald, ns_turb, ns_bomba):
        sustancia = "Water"
    # Entalpia h5
        T5 = tsal_cald                                                   # °C
        P5 = psal_cald*1000                                              # Pa 
    #Guardar h5
        h5 = round(CP.PropsSI("H", "T", T5 + 273.15, "P", P5, sustancia)/1000,2)  # kJ/kg 
        self.hs['h5'] = h5
        s5 = CP.PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)/1000  # kJ/kg K
# Trabajo de la bomba de alta presion
        P3 = pbap*1000                                                   # Pa
        x3 = 0
        ve3 = 1/CP.PropsSI("D", "Q", x3, "P", P3, sustancia)             # m3/kg
#Entalpia h3
        h3 = CP.PropsSI("H", "Q", x3, "P", P3, sustancia)/1000           # kJ/kg
        self.hs['h3'] = h3
        P4 = P5                                                          # Pa
        wbap = ve3*((P4/1000)-(P3/1000))                                 # kJ/kg
# Entalpia h4
        h4 = wbap + h3                                                   # kJ/kg
        self.hs['h4'] = h4
        qin = h5-h4                                                      # kJ/kg

# # b) calor rechazado qout=h7-h1
        P7 = pbbp*1000                                                   # Pa
        s7 = s5*1000                                                     # J/kg K
        x7 = CP.PropsSI("Q", "P", P7, "S", s7, sustancia)
        x = 0
        hf = CP.PropsSI("H", "P", P7, "Q", x, sustancia)/1000            # kJ/kg
        hfg = 2335 # kJ/kg                                               # kJ/kg
        h7s = hf+x7*hfg                                                  # kJ/kg 
        h7 = h5-(ns_turb*(h5-h7s))                                       # kJ/kg 
        self.hs['h7'] = h7
        P1 = pbbp*1000                                                   # Pa
        h1 = CP.PropsSI("H", "Q", x, "P", P1, sustancia)/1000            # kJ/kg 
        self.hs['h1'] = h1
        qout = h7-h1                                                     # kJ/kg 

# # c) Trabajo de la turbina 
        s6 = s5*1000                                                     # J/kg K 
        P6 = pbap*1000                                                   # Pa
        h6s = CP.PropsSI("H", "S", s6, "P", P6, sustancia)/1000          # kJ/kg
        h6 = h5-(ns_turb*(h5-h6s))                                       # kJ/kg
        self.hs['h6'] = h6
        ws_turb = (h5-h6)+(h5-h7)                                        # kJ/kg
        wturb = ns_turb*ws_turb                                          # kJ/kg
        self.results['wturb'] = wturb
# # d) Potencia neta de las bombas BBP y BAP
        ve1 = 1/CP.PropsSI("D", "Q", x, "P", P1, sustancia)             # m3/kg
        P2 = pbap*1000                                                  # Pa
        wbbp = ve1*((P2-P1)/1000)                                       # kJ/kg
        wnetabombas = wbbp+wbap                                         # kJ/kg

# # e) Calor en el intercambiador
        qint = h6-h3                                                    # kJ/kg

# # f) eficiencia termica
        w = wturb+wnetabombas                                           # kJ/kg
        n = 100*w/qin   
        self.results['e_termica']=n                                            # %


#test methods

# Datos de entrada
#Pbbp=30         # kPa (Presion bomba baja presion)
#Pbap=1000       # kPa (Presion bomba alta presion)
##Psal_cald=3000  # kPa (Presion de salida caldera)#
#Tsal_cald=450   # °C (Temperatura de salida caldera)
#ns_turb=0.7     # (Eficiencia turbina isentropica)
#ns_bomba=0.7    # (Eficiencia bomba isentropica)

# Resolucion
