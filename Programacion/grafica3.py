import matplotlib.pyplot as plt

# Crear listas para los datos
horas = []
humedad = []
temperatura = []
co2 = []

# Leer los datos de los tres archivos
archivos = ["B_DIA1.TXT", "B_DIA2.TXT", "B_DIA3.TXT"]

# Asumir que los datos de cada archivo pertenecen a un día diferente
for i, archivo in enumerate(archivos):
    with open(archivo, "r") as file:
        for linea in file:
            partes = linea.strip().split(',')
            hora_actual = partes[0]
            humedad_actual = float(partes[1])
            temperatura_actual = float(partes[2])
            co2_actual = float(partes[3])

            horas.append(f'Día {i + 1} - {hora_actual}')
            humedad.append(humedad_actual)
            temperatura.append(temperatura_actual)
            co2.append(co2_actual)

# Generar y mostrar el gráfico
plt.figure(figsize=(10, 6))
plt.plot(horas, humedad, label='Humedad relativa (%)')
plt.plot(horas, temperatura, label='Temperatura (°C)')
plt.plot(horas, co2, label='CO2 (ppm)')
plt.xlabel('Hora del día')
plt.ylabel('Valores')
plt.title('Datos de mediciones por Día')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.show()
