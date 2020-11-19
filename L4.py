# Se importa la librerí­a NumPy.
import numpy as np

# Se importa el módulo stats de SciPy.
from scipy import stats

# Se importa la biblioteca "matplotlib" junto con la función "pyplot".
import matplotlib.pyplot as plt


# Variables aleatorias X y Y.
va_X = stats.norm(0, np.sqrt(8))
va_Y = stats.norm(0, np.sqrt(8))

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio W(t) con N realizaciones
N = 1000
W_t = np.empty((N, len(t)))	# N funciones del tiempo w(t) con T puntos

# Creación de las muestras del proceso w(t)
for i in range(N):
	X = va_X.rvs()
	Y = va_Y.rvs()
	w_t = X * np.cos(np.pi*t) + Y * np.sin(np.pi*t)
	W_t[i,:] = w_t
	plt.plot(t, w_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(W_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6, label='Valor esperado de 1000 realizaciones')

# Graficar el resultado teórico del valor esperado
E = 0*t
plt.plot(t, E, '-.', lw=4, label='Valor esperado teórico')

# Mostrar las realizaciones del promedio calculado y teÃ³rico.
plt.title('Realizaciones del proceso aleatorio $W(t)$')
plt.xlabel('$t$')
plt.ylabel('$w_i(t)$')
plt.legend() # Se imprime las leyendas de la grÃ¡fica.
plt.show()   # Muestra la gráfica.

# T valores de desplazamiento tau.
desplazamiento = np.arange(T) 
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones.
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación.
plt.figure()

# Cálculo de autocorrelación para cada valor de tau.
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(W_t[n,:], np.roll(W_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de autocorrelación.
Rww = 8 * np.cos(np.pi*taus)

# GrÃ¡ficas de autocorrelación para cada realización del proceso.
plt.plot(taus, Rww, '-.', lw=4, label='Autocorrelación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{WW}(\tau)$')
plt.legend() # Se imprime la leyenda de la gráfica.
plt.show()   # Muestra la gráfica.