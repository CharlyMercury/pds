"""
    Simulación de aliasing en Python
    
    Objetivo: Observar el efecto del aliasing
    al muestrear señales con frecuencias inadecuadas.
    
    Herramientas: Python, Numpy, Matplolib
    
    Actividades: 
        a) Generar una señal senoidal continua simulada.
        b) Muestrear la señal con diferentes frecuencias.
        c) Comparar resutlados coando se cumple y cuando no Nyquist.
        d) Graficar la señal original y la muestreada.

"""
import numpy as np
import matplotlib.pyplot as plt

# Generar y graficar la señal sin continua
f_signal = 50 # Frecuencia de la señal senoidal [hertz]
duration = 0.1  # Tiempo de graficación [segundos]
t_continuos = np.linspace(0, duration, 5000)
x_continuos = np.sin(2*np.pi*f_signal*t_continuos)
# Gráfica
"""plt.figure()
plt.plot(t_continuos, x_continuos)
plt.title("Señal continua")
plt.xlabel("Tiempo [seg]")
plt.ylabel("Amplitud")
plt.show()
"""
# Discretizar en el tiempo mi señal seno()
fs = 101 # Frecuencia de muestreo
ts = 1/fs # Periodo de muestreo
n = np.arange(0, duration, ts)
x_n = np.sin(2*np.pi*f_signal*n)
plt.figure()
plt.plot(t_continuos, x_continuos)
plt.stem(n, x_n, linefmt="C1-", markerfmt="C10", basefmt="k-")
plt.title("Señal continua")
plt.xlabel("Tiempo [seg]")
plt.ylabel("Amplitud")
plt.show()


