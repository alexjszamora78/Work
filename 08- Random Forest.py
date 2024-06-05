from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Cargar el dataset Iris
iris = load_iris()

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Crear y entrenar el modelo Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo en el conjunto de prueba
score = model.score(X_test, y_test)
print("Puntuación de precisión:", score)

# Hacer predicciones en nuevos datos
new_data = [[5.0, 3.5, 1.3, 0.3]]
prediction = model.predict(new_data)
print("Predicción:", prediction)


#Salida:

#Puntuación de precisión: 1.0
#Predicción: [0]