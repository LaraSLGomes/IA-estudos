import numpy as np 

#vetor - unidimensional -> l minusculas
v = np.array([1, 2, 3])
print(type(v))

#matriz - 2d -> l maiusculas
A = np.array([[1, 2, 3, 4, 5],
              [2, 4, 5, 6, 8],
              [3, 7, 1, 6, 9],
              [4, 8, 2, 5, 0],
              [7, 3, 9, 2, 4]]) #(5x5)
#a[j][i] i-linha, j-coluna
print(A[3][3])

M1 = np.array([[1, 2, 3],
               [4, 5, 6],
               [1, 2, 3]])
M2 = np.array([[5, 6, 7],
               [8, 9, 1],
               [3, 4, 2]])

print(M1+2)
print(M1@M2) #multipicacao matricial
print(M1.T) #transposta
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.empty((2, 3))) #cria com base no lixo da memoria 
r = np.random.random_sample(5) #cria numeros aleatorios 
print(r)
p = np.random.permutation(15) #gera tb número aleatorios
print(p)
u = np.random.uniform(10, 20, 5) #10<=x<20
print(u) #[f"{x: .2f}" for x in u]) para casas decimais 

np.random.seed(42)
u = np.random.uniform(10, 20, 5)
print(u)