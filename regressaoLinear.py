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
numerador = np.sum((ydata - y_pred)**2)
denominador = np.sum((ydata - ybar)**2)
r_2 = 1 - numerador / denominador
print("o coeficiente de determinacao R é:", r_2)

class LinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.b_0 = None
        self.b_1 = None 
    def fit(self): #treinamento
        xbar = np.mean(self.x)
        ybar = np.mean(self.y)

        self.b_1 = np.sum((self.y - ybar) * (self.x - xbar)) / np.sum((self.x - xbar)**2)
        self.b_0 = ybar - self.b_1 * xbar
        return self

    def predict(self, x_new):
        return self.b_0 + self.b_1 * np.array(x_new)
    def summary(self):
        print(f"Modelo: y = {self.b_0:.2f} + {self.b_1:.2f} * x")
        print(f"Intercepto = {self.b_0}")
        print(f"Coeficiente angular = {self.b_1}") 



