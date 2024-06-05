import numpy as np

def cosine_similarity(vector1, vector2):
  vector1 = np.array(vector1)
  vector2 = np.array(vector2)

  # Calcular el producto punto y las magnitudes de los vectores
  dot_product = np.dot(vector1, vector2)
  magnitude1 = np.linalg.norm(vector1)
  magnitude2 = np.linalg.norm(vector2)

  # Calcular la similitud del coseno
  similarity = dot_product / (magnitude1 * magnitude2)

  return similarity


vector1 = [0.5, 0.3, 0.2]
vector2 = [0.4, 0.6, 0.1]

similarity = cosine_similarity(vector1, vector2)
print(similarity)  # Salida: 0.8913130356431729