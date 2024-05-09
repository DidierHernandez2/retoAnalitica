import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Cargar datos
df = pd.read_csv("C:/Users/didie/Documents/retoAnalitica/arteDeLaAnalitica/twitter_dataset.csv")

# Mostrar las primeras filas del DataFrame para inspección
print(df.head())

# Quitar variables no relevantes y justificar
# En este caso, pareces estar interesado en la relación entre retweets y likes, por lo tanto, eliminaremos la columna "tweet_id" ya que no es relevante para este análisis.
df = df.drop(columns=['Tweet_ID', 'Username', 'Text', 'Timestamp'])

# Determinar el valor de k
# Podemos utilizar el método del codo (elbow method) para determinar un valor óptimo de k
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df[['Retweets', 'Likes']])
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Numero de Clusters')
plt.title('Metodo del Codo')
plt.show()

# Basándonos en el gráfico, podemos seleccionar un valor de k que esté en el "codo", que parece ser 2 en este caso.

# Utilizando scikit-learn para calcular los centros del algoritmo k-means
k = 2  # Valor de k seleccionado
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(df[['Retweets', 'Likes']])
centers = kmeans.cluster_centers_
print("Centros de los clusters:")
print(centers)

# Basado en los centros, responde las siguientes preguntas
# Puedes examinar las características de cada cluster comparando los centros

# Por ejemplo, si los centros son [x1, y1] y [x2, y2], puedes decir que un cluster tiene más retweets y menos likes, mientras que el otro tiene menos retweets y más likes.
