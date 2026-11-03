import numpy as np
class Adaline:
    def__init__(self, learning_rate=0.01, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.cost = []
        for epochs in range(self.epochs):
            cost = 0
            for i in range(X.shape[0]):
                x_i = X[i]
                target = y[i]
                output = self.net_input(x_i)
                error = target - output
                self.weights[1:] += self.learning_rate * error * x_i
                self.weights[0] += self.learning_rate * error
                cost += (error ** 2) / 2.0
            self.cost.append(cost)
            print(f"epochs {epochs} Cost {cost}")
    def net_input(self, X):
        return np.dot(X, self.weights[1:] + self.weights[0])

    