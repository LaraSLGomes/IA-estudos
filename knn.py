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
    def calculate_predict(self, x):
        distances = [self.calculate_distances(x, x_train)
                     for x_train in self.X_train]
    #def predict(self, X_test):
    X_train = [[1, 2],
               [2, 3],
               [3, 3],
               [10, 10]]
    y_train = [0, 0, 1, 1]
    x_test = [2.5, 2.5]

    def calculate_distances(x1, x2):
        return np.sqrt(np.sum((x1-x2)**2)) #euclidiana
    distances = [calculate_distances(x_test, x_train)
                 for x_train in X_train]
    print(distances)