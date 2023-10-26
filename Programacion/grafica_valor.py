import matplotlib.pyplot as plt

# Leer los datos desde el archivo
horas = []
humedad = []
temperatura = []
co2 = []

with open("C_DIA2.TXT", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(',')
        hora_actual = partes[0]
        humedad_actual = float(partes[1])
        temperatura_actual = float(partes[2])
        co2_actual = float(partes[3])
        
        horas.append(hora_actual)
        humedad.append(humedad_actual)
        temperatura.append(temperatura_actual)
        co2.append(co2_actual)

color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Generar y mostrar el gráfico para la humedad
plt.figure(figsize=(10, 6))
plt.plot(horas, humedad, label='Humedad relativa (%)', color=color_cycle[0])
plt.xlabel('Hora del día')
plt.ylabel('Humedad relativa (%)')
plt.title('Gráfico de Humedad relativa (Cocina - 24/10)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Configurar el intervalo de 30 minutos en el eje X
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1800))  # 1800 segundos = 30 minutos
plt.gcf().autofmt_xdate()  # Formato automático de las etiquetas de fecha y hora

plt.show()

# Generar y mostrar el gráfico para la temperatura (color naranja)
plt.figure(figsize=(10, 6))
plt.plot(horas, temperatura, label='Temperatura (°C)', color=color_cycle[1])
plt.xlabel('Hora del día')
plt.ylabel('Temperatura (°C)')
plt.title('Gráfico de Temperatura (Cocina - 24/10)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Configurar el intervalo de 30 minutos en el eje X
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1800))  # 1800 segundos = 30 minutos
plt.gcf().autofmt_xdate()  # Formato automático de las etiquetas de fecha y hora

plt.show()

# Generar y mostrar el gráfico para el CO2 (color verde)
plt.figure(figsize=(10, 6))
plt.plot(horas, co2, label='CO2 (ppm)', color=color_cycle[2])
plt.xlabel('Hora del día')
plt.ylabel('CO2 (ppm)')
plt.title('Gráfico de CO2 (Cocina - 24/10)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Configurar el intervalo de 30 minutos en el eje X
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1800))  # 1800 segundos = 30 minutos
plt.gcf().autofmt_xdate()  # Formato automático de las etiquetas de fecha y hora

plt.show()
