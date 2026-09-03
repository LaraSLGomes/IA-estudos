import numpy as np
import urllib.request
import math

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
data = np.genfromtxt(urllib.request.urlopen(url), delimiter=",")
print(data)

X = data[:, 1:]
y = data[:, 0]

class KNN:
	def __init__(self, k=5):
		self.k = k

	def fit(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train

	def predict(self, X_test):
		previsoes = []
		for x in X_test:
			distancias = [
				math.sqrt(np.sum((x - treino)**2))
				for treino in self.X_train
			]
			indices = np.argsort(distancias)[:self.k]
			classes = self.y_train[indices]
			valores, contagens = np.unique(classes, return_counts=True)
			previsoes.append(valores[np.argmax(contagens)])
		return np.array(previsoes)

print("Previsoes:", y_pred)
print("Realidade:", np.mean(y_pred == y_test))

