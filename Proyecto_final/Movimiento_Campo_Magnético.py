import matplotlib.pyplot as plt 
import numpy as np
from numpy import linspace
from mpl_toolkits.mplot3d import axes3d
import string
#import random
#import sys
from pip._vendor.distlib.compat import raw_input
from math import sin
from math import cos
import math as ma
import matplotlib.animation as ani

masa = 1
carga = 1
posicion = np.array([-1000, 0, -1000])
velocidad = np.array([0, 0, 0])
B = np.array([0, 0, 0])
print(" ")
print(" ")
print("Este programa calcula y crea una animación de la trayectoria que sigue una partícula cargada que se mueve en el eje x al entrar en interacción con un campo magnético en dirección del eje z.")
print(" ")
print("Ingrese solo los valores que se le piden sin unidades.")
print("La masa está en kilogramos, la carga en coulombs, la velocidad en metro sobre segundo.")
while True:
    texto = raw_input("Ingrese la masa de la partícula:\n")
    masa = float(texto)
    if masa == 0:
        print("Dato erroneo. La partícula debe tener masa.")
    else:
        break
while True:
    texto = raw_input("Ingrese la carga de la partícula:\n")
    carga = float(texto)
    if carga == 0:
        print("Dato erroneo. La partícula debe tener carga.")
    else:
        break
while True:
    texto = raw_input("Ingrese la posición de la carga separada por espacios:\n")
    ind = texto.split(" ")
    if len(ind) != 3:
        print("Ingrese tres entradas.")
    else:
        posicion[0] = float(ind[0])
        posicion[1] = float(ind[1])
        posicion[2] = float(ind[2])
        break
while True:
    texto = raw_input("Ingrese la velocidad inicial de la partícula separada por espacios:\n")
    ind = texto.split(" ")
    if len(ind) != 3:
        print("Ingrese velocidad en tres entradas para que haya movimiento en la partícula.")
    else:
        velocidad[0] = float(ind[0])
        velocidad[1] = float(ind[1])
        velocidad[2] = float(ind[2])
        break
while True:
    texto = raw_input("Ingrese el campo magnetico separado por espacios:\n")
    ind = texto.split(" ")
    if len(ind) != 3:
        print("Ingrese el campo en tres entradas para que haya interacción.")
    else:
        B[0] = float(ind[0])
        B[1] = float(ind[1])
        B[2] = float(ind[2])
        break
        
print(masa)
print(carga)
print(posicion)
print(velocidad)
print(B)

v0 = float(ma.sqrt((velocidad[0])**2 +(velocidad[1])**2 + (velocidad[2])**2))
B2 = float(ma.sqrt((B[0])**2 +(B[1])**2 + (B[2])**2))


k = float(((masa*v0)/(carga*B2)))
k2 = float((carga*B2)/masa)

#print(k)
#print(k2)

t = np.linspace(0,10,58)

x=[]
y=[]
z=[]
for i in t:
    x.append(float((k)*(sin(np.deg2rad(k2*i)))+posicion[0]))
    y.append(float((-(k))*(cos(np.deg2rad((k2*i))))+posicion[1]))
    z.append(float(i*0+posicion[2]))
    
fig=plt.figure()
ax=fig.gca()

def anima(j):
    ax.clear()
    ax.plot(x[:j],y[:j])
    plt.title(str(x[j]))
    
animacion=ani.FuncAnimation(fig, anima, len(x))

plt.show()
