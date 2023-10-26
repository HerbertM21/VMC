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

# Generar y mostrar el gráfico
plt.figure(figsize=(10, 6))
plt.plot(horas, humedad, label='Humedad relativa (%)')
plt.plot(horas, temperatura, label='Temperatura (°C)')
plt.plot(horas, co2, label='CO2 (ppm)')
plt.xlabel('Hora del día')
plt.ylabel('Valores')
plt.title('Datos de mediciones (Cocina | 00 AM - 20 PM | 24/10)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Configurar el intervalo de 30 minutos en el eje X
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1800))  # 1800 segundos = 30 minutos
plt.gcf().autofmt_xdate()  # Formato automático de las etiquetas de fecha y hora

plt.show()
