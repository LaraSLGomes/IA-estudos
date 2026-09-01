import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

x1 = np.array([2,8,11,10,8,4,2,2,9,8])
x2 = np.array([50, 110, 120,550,295, 200, 375,52, 100, 300])
y = np.array([9.95,24.45,31.75, 35, 25.02, 16.86, 14.38,9.6,24.35,27.5])

print(x2.shape[0])
X = np.column_stack((np.ones(x1.shape[0]), x1, x2))
print(X)
class MRegression:
    def __init__(self, X, y):
        self.X = X 
        self.y = y
        self.beta = None
        self.N = X.shape[0]
    def fit(self):
        self.X = np.column_stack((np.ones(self.N), self.X))
        self.beta = np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.y
        #pseudo inversa (casos sem matriz quadratica, nao possui inversa)
        #Moore Pensore
    def predict(self, X_new):
        N = X_new.shape[0]
        X_new = np.column_stack((np.ones(N), X_new))
        return X_new @ self.beta
    
X = np.column_stack((x1, x2))  
modelo = MRegression(X, y)
modelo.fit()
print("Os parametros sao ", modelo.beta)
y_pred = modelo.predict(X)
print(y_pred)

def r2_score(y_true, y_pred):
    numerador = np.sum((y_true-y_pred)**2)
    denominador = np.sum((y_true-np.mean(y_pred))**2)
    r2_score = 1 - (numerador/denominador)
    return r2_score
print(r2_score(y, y_pred))

fig = go.Figure()
fig.add_scatter3d(x=x1, y=x2, z=y, mode="markers", 
                  marker = dict(color="red", size=5), name="Dados originais")
fig.add_scatter3d(x=x1, y=x2, z=y_pred, mode="markers", 
                  marker = dict(color="green", size=5), name="Dados Previstos")
fig.show()

#print(np.linspace(min(x1), max(x1), 5))
#print(np.linspace(min(x2), max(x2), 5))
x1_grid, x2_grid = np.meshgrid( #cria varias coodernadas de acordo com a regiao dos meus dados
    np.linspace(min(x1), max(x1), 10),
    np.linspace(min(x2), max(x2), 10)
)#cria a malha de coordenadas para descobrir como o modelo de comporta nessa regiao
#cria um mesh com varias coordenadas de x1 e x2
y_grid = modelo.beta[0] + modelo.beta[1]*x1_grid + modelo.beta[2]*x2_grid
print(y_grid)
#calcular as previsoes para as coordenadas e usa os pontos para visualziar o hiperplano
#descrobir como o modleo se comporta em todas a regiao
fig = go.Figure()
fig.add_scatter3d(x=x1, y=x2, z=y, mode="markers", 
                  marker = dict(color="red", size=5), name="Dados originais")
fig.add_scatter3d(x=x1, y=x2, z=y_pred, mode="markers", 
                  marker = dict(color="green", size=5), name="Dados Previstos")
fig.add_surface(x=x1_grid, y=x2_grid, z=y_grid, opacity=0.5, name="Hiperplano")
fig.show()
#se os pontos vermelhos estao proximos da superficie, o modelo esta capturando bem a relacao
#se os pontos vermelhos estao bem afsttados, indica erro na previsao