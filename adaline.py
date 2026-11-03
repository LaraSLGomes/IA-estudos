import numpy as np
class Adaline:
    def__init__(self, learning_rate=0.01, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.cost = []
        for epochs in range(self.epochs):
            for i in range(X.shape[0]):
                x_i = X[i]
                target = y[i]
    def net_input(self, X):
        return np.dot(X, self.weights[1:] + self.weights[0])