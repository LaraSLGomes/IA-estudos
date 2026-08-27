import numpy as np
import math

random_state = 42
np.random.seed(random_state)
x = np.array([34, 5, 6, 4])
print(np.random.permutation(x)) #embaralhar dados 

def train_test_split(X, y, test_size=0.3, random_state=42):
    if random_state is not None:
        np.random.seed(random_state)
    if len(X) != len(y):
        raise ValueError("X e y devem ter o mesmo tamanho")
    n_samples = len(x)
    print("Amostra quantidade", n_samples)
    indices = np.random.permutation(n_samples)
    print("indices embaralhados", indices)
    n_test = math.ceil(n_samples * test_size)
    print("tamanho da amostra teste", n_test)
    test_indices = indices[:n_test:]
    print("indices de teste", test_indices)
    train_indices = indices[n_test:]
    print("indices de treino", train_indices)
    