import CoolProp.CoolProp as CP
# CICLO RANKINE CON PRECALENTADOR DE AGUA ABIERTO
# Datos de entrada
Pbbp=30000        # Pa (Presion bomba baja presion)
Pbap=1000000      # Pa (Presion bomba alta presion)
Psal_cald=3000000 # Pa (Presion de salida caldera)
Tsal_cald=450     # °C (Temperatura de salida caldera)
ns_turb=0.7       # (Eficiencia turbina isentropica)
ns_bomba=0.7      # (Eficiencia bomba isentropica)

# Resolucion
# Especifica la sustancia como "Water"
sustancia = "Water"

# CALCULO DE ENTALPIAS
# h1
x1 = 0
P1 = Pbbp         # Presion 1                                       # Pa
h1 = CP.PropsSI("H", "Q", x1, "P", P1, sustancia)    

# h2
ve1 = 1/CP.PropsSI("D", "Q", x1, "P", P1, sustancia)                # m3/kg
P2 = Pbap         # Presion 2                                       # Pa
wbbp = ve1*((P2-P1))/ns_bomba   
h2 = (wbbp + h1)

# h3
P3 = Pbap         # Presion 3                                        # Pa
x3 = 0 
h3 = CP.PropsSI("H", "Q", x3, "P", P3, sustancia)                    # J/kg

# h4
ve3 = 1/CP.PropsSI("D", "Q", x3, "P", P3, sustancia)                 # m3/kg
P4 = Psal_cald    # Presion 4                                        # Pa
wbap = ve3*(P4-P3)/ns_bomba                                          # J/kg
h4 = wbap + h3

# h5
T5 = Tsal_cald                                                       # °C
P5 = Psal_cald    # Presion 5                                        # Pa 
h5 = CP.PropsSI("H", "T", T5 + 273.15, "P", P5, sustancia)           # J/kg 
s5 = CP.PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)           # J/kg K

# h6
s6 = s5                                                              # J/kg K 
P6 = Pbap         # Presion 6                                        # Pa
h6s = CP.PropsSI("H", "S", s6, "P", P6, sustancia)                   # J/kg
h6 = h5-(ns_turb*(h5-h6s))                                           # J/kg

# h7
P7 = Pbbp         # Presion 7                                        # Pa
s7 = s5 
h7s = CP.PropsSI("H", "P", P7, "S", s7, sustancia)                   # J/kg                                         # kJ/kg 
h7 = h5-(ns_turb*(h5-h7s))                                           # J/kg 

# RESOLUCION
# a) Calor añadido qin= h5-h4
qin = h5-h4       
                                                           
# b) calor rechazado qout=h7-h1  
qout = h7-h1                                                     # J/kg 

# c) Trabajo de la turbina 
ws_turb = (h5-h6)+(h5-h7)                                        # J/kg
wturb = ns_turb*ws_turb                                          # J/kg

# d) Trabajo neta de las bombas BBP y BAP
wnetabombas = wbbp+wbap                                          # J/kg

# e) trabajo neto
wneto=wturb+wnetabombas

# e) Calor en el intercambiador
qint = h6-h3                                                    # J/kg

# f) eficiencia termica
w = wturb+wnetabombas                                           # J/kg
n = 100*w/qin                                                   # %

# g) fraccion de vapor
# qout=(1-y)(h7-h1)
# h7-h1-yh7+yh1=qouy
# y(h1-h7)=qout-h7+h1
y=(qout-h7-h1)/(h1-h7)
z=1-y

# CALCULO DE ENTROPIAS
s1 = CP.PropsSI("S", "Q", x1, "P", P1, sustancia)                    # J/kg K
s2 = CP.PropsSI("S", "H", h2, "P", P2, sustancia)                    # J/kg K
s3 = CP.PropsSI("S", "Q", x3, "P", P3, sustancia)                    # J/kg K
s4 = CP.PropsSI("S", "H", h4, "P", P4, sustancia)                    # J/kg K
s5 = CP.PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)           # J/kg K
s6 = s5                                                              # J/kg K
s7 = s5                                                              # J/kg K

print("h1 = {0:.2f} ".format(h1/1000),"kJ/kg")
print("h2 = {0:.2f} ".format(h2/1000),"kJ/kg")
print("h3 = {0:.2f} ".format(h3/1000)," kJ/kg")
print("h4 = {0:.2f} ".format(h4/1000)," kJ/kg")
print("h5 = {0:.2f} ".format(h5/1000)," kJ/kg")
print("h6 = {0:.2f} ".format(h6/1000)," kJ/kg")
print("h7 = {0:.2f} ".format(h7/1000)," kJ/kg")
print("Calor de entrada = {0:.2f} ".format(qin/1000),"kJ/kg")
print("Calor de salida = {0:.2f} ".format(qout/1000),"kJ/kg")
print("Calor intercambiador = {0:.2f} ".format(qint/1000),"kJ/kg")
print("Trabajo isentropico turbina = {0:.2f} ".format(ws_turb/1000),"kJ/kg")
print("Trabajo turbina = {0:.2f} ".format(wturb/1000),"kJ/kg")
print("Trabajo bomba alta presion = {0:.2f} ".format(wbap/1000),"kJ/kg")
print("Trabajo bomba baja presion = {0:.2f} ".format(wbbp/1000),"kJ/kg")
print("Trabajo neto = {0:.2f} ".format(wneto/1000),"kJ/kg")
print("eficiencia = {0:.2f} ".format(n),"%")
print("La fracción de vapor y = {0:.2f} ".format(y))
print("La fracción de vapor 1-y = {0:.2f} ".format(z))
print("s1 = {0:.2f} ".format(s1/1000),"kJ/kg K")
print("s2 = {0:.2f} ".format(s2/1000),"kJ/kg K")
print("s3 = {0:.2f} ".format(s3/1000),"kJ/kg K")
print("s4 = {0:.2f} ".format(s4/1000),"kJ/kg K")
print("s5 = {0:.2f} ".format(s5/1000),"kJ/kg K")
print("s6 = {0:.2f} ".format(s6/1000),"kJ/kg K")
print("s7 = {0:.2f} ".format(s7/1000),"kJ/kg K")



