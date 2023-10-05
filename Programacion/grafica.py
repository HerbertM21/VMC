import matplotlib.pyplot as plt

# Función para filtrar datos según el rango de horas
def filtrar_datos(hora_inicio, hora_fin):
    datos_filtrados = []
    with open("datos.dat", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            hora_actual = partes[1]
            if hora_inicio <= hora_actual <= hora_fin:
                humedad, temperatura, co2 = float(partes[2]), float(partes[3]), float(partes[4])
                datos_filtrados.append((hora_actual, humedad, temperatura, co2))
    return datos_filtrados

# Función para generar y mostrar el gráfico
def generar_grafico(datos, hora_inicio, hora_fin):
    if not datos:
        print("No hay datos disponibles para el rango de horas especificado.")
        return

    horas, humedad, temperatura, co2 = zip(*datos)

    # Genera el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(horas, humedad, label='Humedad (%)')
    plt.plot(horas, temperatura, label='Temperatura (°C)')
    plt.plot(horas, co2, label='CO2 (ppm)')
    plt.xlabel('Hora del día')
    plt.ylabel('Valor')
    plt.title(f'Datos en el rango de {hora_inicio} a {hora_fin}')
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para una mejor legibilidad
    plt.legend()
    plt.grid(True)
    
    # Configurar el intervalo de 30 minutos en el eje X
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1000))  # 1800 segundos = 30 minutos
    plt.gcf().autofmt_xdate()  # Formato automático de las etiquetas de fecha y hora
    
    plt.show()

# Solicitar al usuario el rango de horas
hora_inicio = input("Ingrese la hora de inicio del rango en formato HH:MM:SS: ")
hora_fin = input("Ingrese la hora de fin del rango en formato HH:MM:SS: ")

# Filtrar los datos según el rango de horas especificado
datos_filtrados = filtrar_datos(hora_inicio, hora_fin)

generar_grafico(datos_filtrados, hora_inicio, hora_fin)
