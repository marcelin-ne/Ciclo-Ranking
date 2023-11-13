from CoolProp.CoolProp import PropsSI
import numpy as np
import matplotlib.pyplot as plt
import math
# Ciclo ideal Rankine  con un calentador cerrado de agua dealimentación y recalentamiento

# Definir las propiedades de entrada
p1 = 30000  # Presión a la salida del condensador en Pa
x1 = 0.0 # Calidad salida del condensador
p2 = 4000000 # Presión a la salida de la segunda bomba en Pa
p3 = 2000000  # Presión a la salida del calentador de agua de alimentación baja en Pa
x3 = 0.0 # condensación completa en el calentador cerrado de agua de alimentación
p4 = p2 # Presión a la salida de la segunda bomba
T6 = 500 # Temperatura en la salida de la caldera/entrada de la turbina en °C
p5 = p2 # Presión a la entrada de la caldera en Pa
mp = 15 # flujo masico en kg/s
p6 = p5 # Presión a la entrada de la turbina en Pa
p7 = p3 # Presión a la salida de la turbina hacia el calentador de agua de alimentacion en Pa
p8 = p1 # Presión a la salida de la turbina hacia el condensador en Pa
p9 = p2 # Presión a la salida del CAA cerrado
nb = 0.85 # Eficiencia para las bombas
nt = 0.95 # Eficiencia de la turbina

# Calcular laS propiedades en cada punto del ciclo
h1 = PropsSI('H', 'Q', x1, 'P', p1, 'Water')
s1 = PropsSI('S', 'Q', x1, 'P', p1, 'Water')
h2s = PropsSI('H', 'S', s1, 'P', p2, 'Water')
wb1 = (h2s-h1)/nb # Trabajo de la bomba 1
h2 = h1+wb1
h3 = PropsSI('H', 'Q', x3, 'P', p3, 'Water')
s3 = PropsSI('S', 'Q', x3, 'P', p3, 'Water')
h4s = PropsSI('H', 'S', s3, 'P', p4, 'Water')
wb2 = (h4s-h3)/nb # Trabajo de la bomba 2
h4 = h3+wb2
h9 = h3

h6 = PropsSI('H', 'T', T6+273.15, 'P', p6, 'Water')
s6 = PropsSI('S', 'T', T6+273.15, 'P', p6, 'Water')
h6s = PropsSI('H', 'S', s6, 'P', p6, 'Water')
h7s = PropsSI('H', 'S', s6, 'P', p7, 'Water')
h7=h6-nt*(h6-h7s)

y  = (h9-h2)/(h7-h3+h9-h2) # Balance energetico en el calentador de aguade alimentación cerrado
h5 = y*h9+(1-y)*h4

h8s = PropsSI('H', 'S', s6, 'P', p8, 'Water')
h8 = h6-nt*(h6-h8s)

# Calcular la eficiencia térmica y el trabajo neto

q_in = h6-h5
q_out = (1-y)*(h8-h1) 
Wnet = mp*(q_in-q_out) # Balance energético del sistema
eta = 1- (q_out/ q_in)

# Imprimir los resultados
print("h1 = {0:.2f} kJ/kg".format(h1/1000))
print("h2s = {0:.2f} kJ/kg".format(h2s/1000))
print("h2 = {0:.2f} kJ/kg".format(h2/1000))
print("h3 = {0:.2f} kJ/kg".format(h3/1000))
print("h4 = {0:.2f} kJ/kg".format(h4/1000))
print("h4s = {0:.2f} kJ/kg".format(h4s/1000))
print("h5 = {0:.2f} kJ/kg".format(h5/1000))
print("h6 = {0:.2f} kJ/kg".format(h6/1000))
print("h7 = {0:.2f} kJ/kg".format(h7/1000))
print("h7s = {0:.2f} kJ/kg".format(h7s/1000))
print("h8 = {0:.2f} kJ/kg".format(h8/1000))
print("h8s = {0:.2f} kJ/kg".format(h8s/1000))
print("h9 = {0:.2f} kJ/kg".format(h9/1000))

print("s1 = {0:.4f} kJ/kgK".format(s1/1000))

print("s3 = {0:.4f} kJ/kgK".format(s3/1000))

print("s6 = {0:.4f} kJ/kgK".format(s6/1000))

print("y = {0:.4f}".format(y))
print("q_in = {0:.2f} kJ/kg".format(q_in/1000))
print("q_out = {0:.2f} kJ/kg".format(q_out/1000))
print("La eficiencia térmica del ciclo es {0:.2f}%".format(eta * 100))
print("El trabajo neto del ciclo es {0:.2f} kW".format(Wnet/1000))

def ajustar_length_h6(valor_H6):
    # Ajusta length_h6 en un rango exponencial entre 0.10 y 0.35
    valor_minimo = 0.20
    valor_maximo = 0.35

    # Ajusta el valor_H6 a un rango exponencial entre 1 y 10000
    valor_H6_ajustado = max(1, min(10000, valor_H6))
    valor_H6_ajustado = math.exp(0.002 * valor_H6_ajustado)  # Puedes ajustar el factor 0.002 según tus necesidades

   # Normaliza el valor_H6 entre 0 y 1
    valor_H6_ajustado = (valor_H6 - 1) / (10000 - 1)

    # Aplica la escala exponencial al rango de 0 a 1
    length_h6_ajustado = valor_minimo + (valor_maximo - valor_minimo) * (
        np.exp(0.002 * valor_H6_ajustado) - np.exp(0)
    ) / (np.exp(0.002 * 1) - np.exp(0))

    return length_h6_ajustado

# Ejemplo de uso
valor_H6 = 3446.02
length_h6_ajustado = ajustar_length_h6(valor_H6)
print(length_h6_ajustado)