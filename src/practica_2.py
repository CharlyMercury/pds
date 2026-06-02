"""
    Práctica 2: Sistemas Discretos en Python

    Objetivos:
        - Representar señales discretos utilizando arreglos de NumPy.
        - Implementar sistemas discretos básicos en Python.
        - Comparar gráficamente la señal de entrada y la señal de salida.
        - Interpretar el efecto de cada sistema sobre la señal original.
        
    Sistemas a implementar:
        1. Sistema de ganancia constante: y[n] = A * x[n]
        2. Sistema de retardo: y[n] = x[n - 1]
        3. Sistema acumulador: y[n] = y[n - 1] + x[n]
        4. Sistema de media móvil: y[n] = (x[n] + x[n - 1] + x[n - 2]) / 3
"""
import numpy as np
import matplotlib.pyplot as plt

# Definir el número de muestras
n = np.arange(0, 20)
x = np.array(
    [0, 1, 2, 3, 2,
     1, 0, -1, -2, -1,
     0, 1, 3, 5, 3,
     1, 0, -1, 0, 1]
    , dtype=float
)

# Gráfica de la señal de entrada
plt.figure(figsize=(12, 8))
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Señal de Entrada')
plt.grid(True)
plt.show()

# Sistema de ganancia constante A = 2
y_gain = 2*x

# Sistema de retardo de una muestra
y_delay = np.zeros_like(x)
for i in range(1, len(x)):
    y_delay[i] = x[i-2]

# Sistema acumulador
y_accumulator = np.zeros_like(x)
for i in range(1, len(x)):
    y_accumulator[i] = y_accumulator[i-1] + x[i]

# Sistema de media móvil
y_moving_average = np.zeros_like(x)
for i in range(len(x)):
    if i == 0: 
        y_moving_average[i] = x[i]/3
    elif i == 1:
        y_moving_average[i] = (x[i] + x[i-1]) / 3
    else:
        y_moving_average[i] = (x[i] + x[i-1] + x[i-2]) / 3

# Graficas del sistema de ganancia constante A = 2
plt.figure(figsize=(12, 8))
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt=' ', label='x[n]')
plt.stem(n, y_gain, linefmt='r-', markerfmt='ro', basefmt=' ', label='y[n] = 2*x[n]')
plt.title("Sistema de Ganancia Constante A=2")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(False)
plt.show()

# Graficas del sistema con retardo de una muestra
plt.figure(figsize=(12, 8))
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt=' ', label='x[n]')
plt.stem(n, y_delay, linefmt='r-', markerfmt='ro', basefmt=' ', label='y[n] = x[n-1]')
plt.title("Sistema de Retardo")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(False)
plt.show()

# Graficas  del sistema acumulador
plt.figure(figsize=(12, 8))
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt=' ', label='x[n]')
plt.stem(n, y_accumulator, linefmt='r-', markerfmt='ro', basefmt=' ', label='y[n] = y[n-1] + x[n]')
plt.title("Sistema de Acumulador")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(False)
plt.show()

# Grafica del sistema de media móvil
plt.figure(figsize=(12, 8))
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt=' ', label='x[n]')
plt.stem(n, y_moving_average, linefmt='r-', markerfmt='ro', basefmt=' ', label='y[n] = (x[n] + x[n-1] + x[n-2]) / 3')
plt.title("Sistema de Media Móvil")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(False)
plt.show()
