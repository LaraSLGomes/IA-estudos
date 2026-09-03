import numpy as np

class KNN:
    def __init__(self, k=5, task="classification"):
         self.k = k
         self.task = task
    def fit(self, X_train, y_train):
        #metodo do treinamento da maquina
        self.X_train = X_train
        self.y_train = y_train
    def calculate_distances(self, x1, x2):
        return np.sqrt(np.sum((x1-x2)**2)) #euclidiana
    