import numpy as np 

xdata = np.array([1, 2, 3])
print("Dados de entrada:", xdata)
ydata = np.array([1, 4, 8])
print("Dados de saida:", ydata)


#calcular as medias
xbar = np.mean(xdata)
print("a media de X é:", xbar)
ybar = np.mean(ydata)
print("a media de Y é:", ybar)
b_1 = np.sum((ydata-ybar) * (xdata-xbar)) / np.sum((xdata-xbar)**2)
print("o valor do coeficiente angular:", b_1)
b_0 = ybar - b_1 * xbar
print("o intercepto é:", b_0)
