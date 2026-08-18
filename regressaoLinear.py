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
#funcao estimada 
y_pred = b_0 + b_1 * xdata
print("a funcao estimada é:", y_pred)

# coeficiente de determinacao R
soma_erros = np.sum((ydata - y_pred)**2)
soma_total = np.sum((ydata - ybar)**2)
r_2 = 1 - soma_erros / soma_total
print("o coeficiente de determinacao R é:", r_2)


