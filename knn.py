import numpy as np

class KNN:

    def __init__(self, k=5, task="classification"):

        self.k = k
        self.task = task

    def fit(self, X_train, y_train):

        self.X_train = X_train
        self.y_train = y_train

    def calculate_distance(self, x1, x2):

        x1 = np.array(x1)
        x2 = np.array(x2)

        return np.sqrt(np.sum((x1 - x2) ** 2)) # euclidiana

    def calculate_predict(self, x):

        distances = [self.calculate_distance(x, x_train)
                     for x_train in self.X_train]

        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        if self.task == "classification":
            return unique[np.argmax(counts)]
        if self.task == "regression":
            return np.mean(k_nearest_labels)
        else:
            return ValueError("Tarefa sera regressao ou classificacao!")

    # def predict(self, X_test):


X_train = np.array([
    [1, 2],
    [2, 3],
    [3, 3],
    [10, 10]
])

y_train = [0, 0, 1, 1]

x_test = [2.5, 2.5]

knn = KNN()

knn.fit(X_train, y_train)

distances = [
    knn.calculate_distance(x_test, x_train)
    for x_train in knn.X_train
]

print(distances)

k = 3

k_indices = np.argsort(distances)[:k]

print(k_indices)