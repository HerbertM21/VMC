import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV sin encabezados
data = pd.read_csv("B_DIA2.csv", header=None, names=["Hora", "Humedad", "Temperatura", "CO2"])

# Dividir los datos en características (X) y la variable objetivo (y)
X = data[["Temperatura", "Humedad"]]
y = data["CO2"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=65)

# Crear y ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular las métricas de rendimiento
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error cuadrático medio (MSE): {mse}")
print(f"Coeficiente de determinación (R^2): {r2}")

# Gráfico de dispersión de las predicciones frente a los valores reales
plt.scatter(y_test, y_pred)
plt.xlabel("CO2 real")
plt.ylabel("CO2 predicho")
plt.title("Predicciones de CO2 vs. Valores reales")
plt.show()
