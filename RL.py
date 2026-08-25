import numpy as np

x1 = np.array([2, 8, 11, 10, 8, 4, 2, 2, 9, 8])
x2 = np.array([50, 110, 120, 550, 295, 200, 375, 52, 100, 300])
y = np.array([9.95, 24.45, 31.75, 34, 25.02, 18.86, 14.38, 9.6, 24.35, 27.5])

print(x1.shape[0])
X = np.column_stack((np.ones(x2.shape[0]), x1, x2))
class MRegression:
    def __init__(sel, x, y):
        self.x = x
        self.y = y
        sel.beta = None
    def fit(self):
        self.X = np.column_stack((np.ones(self.N), self.X))
        self.beta = np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.y
        #pseudo inversa (casos sem matriz quadratica, nao possui inversa)
        #Moore Pensore
    def predict(self, X_new):
        N = X_new.shape[0]
        X_new = np.column_stack(np.ones(N), X_new)
        return X_new @ self.beta

X = np.column_stack((x1, x2))
modelo = MRegression()
modelo.fit()
print("Os parametros sao: ", modelo.beta)
y_pred = modelo.predict(X)
print(y_pred)