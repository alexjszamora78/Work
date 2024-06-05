#Array de 10 elementos enteros aleatorios:
#pip install numpy

import numpy as np

array = np.random.randint(10, size=10)
print(array)

#Suma de todos los elementos del array:
sum = np.sum(array)
print(sum)

#Calculo del producto de todos los elementos del array:
product = np.prod(array)
print(product)

#Array en orden ascendente:
sorted_array = np.sort(array)
print(sorted_array)

#Encontrar el índice del elemento máximo del array:
max_index = np.argmax(array)
print(max_index)

#Matriz de 3x3 con valores enteros aleatorios:
matrix = np.random.randint(10, size=(3, 3))
print(matrix)

#Transpuesta de la matriz:
transposed_matrix = np.transpose(matrix)
print(transposed_matrix)

#Calculo de la inversa de la matriz (si es invertible):
try:
    inverse_matrix = np.linalg.inv(matrix)
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("La matriz no es invertible")

#Valores propios y vectores propios de la matriz:
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Valores propios:", eigenvalues)
print("Vectores propios:", eigenvectors)

#Array de ceros de tamaño 5x5:
zeros_array = np.zeros((5, 5))
print(zeros_array)