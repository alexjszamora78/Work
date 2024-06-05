import numpy as np
from sklearn.svm import OneClassSVM

data = np.random.randn(100, 10)  # 100 muestras, 10 características

# Etiquetar los datos como normales
labels = np.ones(data.shape[0])  # Todos los datos son normales

# Crear y entrenar el modelo One-Class SVM
model = OneClassSVM(kernel='rbf', gamma=0.1, nu=0.1)
model.fit(data)

# Generar datos de prueba con algunas anomalías
test_data = np.random.randn(10, 10)
test_data[2, :] += 5  # Introducir una anomalía en la tercera muestra
test_data[7, :] -= 3  # Introducir otra anomalía en la octava muestra

# Predecir las etiquetas de los datos de prueba
predictions = model.predict(test_data)

# Imprimir las predicciones
print(predictions)

# Imprimir las etiquetas reales de los datos de prueba (para fines de evaluación)
print(np.ones(test_data.shape[0]))


#Salida:

#[-1  1 -1  1  1  1  1 -1  1  1]
#[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]