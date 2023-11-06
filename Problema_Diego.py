import CoolProp.CoolProp as CP
# CICLO RANKINE CON PRECALENTADOR DE AGUA ABIERTO
# Datos de entrada
Pbbp=30         # kPa (Presion bomba baja presion)
Pbap=1000       # kPa (Presion bomba alta presion)
Psal_cald=3000  # kPa (Presion de salida caldera)
Tsal_cald=450   # °C (Temperatura de salida caldera)
ns_turb=0.7     # (Eficiencia turbina isentropica)
ns_bomba=0.7    # (Eficiencia bomba isentropica)

# Resolucion
# Especifica la sustancia como "Water"
sustancia = "Water"
# # a) Calor añadido qin= h5-h4
# Entalpia h5
T5 = Tsal_cald                                                   # °C
P5 = Psal_cald*1000                                              # Pa 
h5 = round(CP.PropsSI("H", "T", T5 + 273.15, "P", P5, sustancia)/1000,2)  # kJ/kg 
s5 = CP.PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)/1000  # kJ/kg K
# Trabajo de la bomba de alta presion
P3 = Pbap*1000                                                   # Pa
x3 = 0 
ve3 = 1/CP.PropsSI("D", "Q", x3, "P", P3, sustancia)             # m3/kg
#Entalpia h3
h3 = CP.PropsSI("H", "Q", x3, "P", P3, sustancia)/1000           # kJ/kg
P4 = P5                                                          # Pa
wbap = ve3*((P4/1000)-(P3/1000))                                 # kJ/kg
# Entalpia h4
h4 = wbap + h3                                                   # kJ/kg
qin = h5-h4                                                      # kJ/kg

                                                   # kJ/kg 

# # c) Trabajo de la turbina 
s6 = s5*1000                                                     # J/kg K 
P6 = Pbap*1000                                                   # Pa
h6s = CP.PropsSI("H", "S", s6, "P", P6, sustancia)/1000          # kJ/kg
h6 = h5-(ns_turb*(h5-h6s))                                       # kJ/kg
ws_turb = (h5-h6)+(h5-h7)                                        # kJ/kg
wturb = ns_turb*ws_turb                                          # kJ/kg

# # d) Potencia neta de las bombas BBP y BAP
ve1 = 1/CP.PropsSI("D", "Q", x, "P", P1, sustancia)             # m3/kg
P2 = Pbap*1000                                                  # Pa
wbbp = ve1*((P2-P1)/1000)                                       # kJ/kg
wnetabombas = wbbp+wbap                                         # kJ/kg

# # e) Calor en el intercambiador
qint = h6-h3                                                    # kJ/kg

# # f) eficiencia termica
w = wturb+wnetabombas                                           # kJ/kg
n = 100*w/qin                                                   # %

print("h1 = ", h1)
print("h3 = ", h3)
print("h4 = ",h4)
print("h5 = ",h5)
print("s5 = ",s5)
print("h6 = ",h6)
print("h6s = ",h6s)
print("s6 = ",s6)
print("h7 = ",h7)
print("h7s = ",h7s)
print("s7 = ",s7)
print("x7 = ",x7)
print("wbap = ",wbap)
print("qin = ",qin)
print("qout = ",qout)
print("ws_turb = ",ws_turb)
print("wturb = ",wturb)
print("wnetabombas = ",wnetabombas)
print("qint = ",qint)
print("eficiencia = ",n,"%")


