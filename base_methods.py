#Build functions to use in the logical part ok kivy

#Problema Diego 

import CoolProp.CoolProp as CP
# CICLO RANKINE CON PRECALENTADOR DE AGUA ABIERTO
# Datos de entrada variables
Pbbp=30         # kPa (Presion bomba baja presion)
Pbap=1000       # kPa (Presion bomba alta presion)
Psal_cald=3000  # kPa (Presion de salida caldera)
Tsal_cald=450   # °C (Temperatura de salida caldera)
ns_turb=0.7     # (Eficiencia turbina isentropica)
ns_bomba=0.7    # (Eficiencia bomba isentropica) 

#Datos Fijos 
# Especifica la sustancia como "Water"
sustancia = "Water" 

#Create a class CR_PAA
class CR_P_Agua_Abierto:
#objects 
    int Pbbp
    int Pbap
    int Psal_cald
    int Tsal_cald
    int ns_turb
    int ns_bomba
    String sustancia="Water"
#Constructor 
    def __init__(self, Pbbp, Pbap, Psal_cald, Tsal_cald, ns_turb, ns_bomba):
        self.Pbbp = Pbbp
        self.Pbap = Pbap
        self.Psal_cald = Psal_cald
        self.Tsal_cald = Tsal_cald
        self.ns_turb = ns_turb
        self.ns_bomba = ns_bomba 
    
#methods
#1. Calculo Entalpia h5
def calcular_entalpia_h5(Tsal_cald, Psal_cald, sustancia):
    P5 = Psal_cald*1000                                              # Pa 
    h5 = round(CP.PropsSI("H", "T", T5 + 273.15, "P", P5, sustancia)/1000,2)  # kJ/kg 
    s5 = CP.PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)/1000  # kJ/kg K
    return h5

#2. TRabajo de la bomba de alta presion 
def calcular_trabajo_bomba_alta_presion(Pbap, sustancia):
    P3 = Pbap * 1000  # Pa
    x3 = 0
    ve3 = 1 / CP.PropsSI("D", "Q", x3, "P", P3, sustancia)  # m3/kg
    return P3 #Cual es la presion? 

#X3 es fijo? se puede poner como atributo de la clase? 

#3. Calculo entalpia h3
def calcular_entalpia_h3(P3, P5, x3):
    h3 = CP.PropsSI("H", "Q", x3, "P", P3, sustancia)/1000           # kJ/kg
    P4 = P5                                                          # Pa
    wbap = ve3*((P4/1000)-(P3/1000))  
    return h3

#4. Calculo entalpia h4
def calcular_entalpia_h4(wbap, h3, h5):
    # Entalpia h4
    h4 = wbap + h3                                                   # kJ/kg
    qin = h5-h4  
    return h4