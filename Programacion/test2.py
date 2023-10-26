def leer_archivo(archivo_nombre):
    horas = []
    co2 = []
    temperatura = []
    humedad = []

    with open(archivo_nombre, "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            hora_actual = partes[0]
            co2_actual = float(partes[3])
            temperatura_actual = float(partes[2])
            humedad_actual = float(partes[1])

            horas.append(hora_actual)
            co2.append(co2_actual)
            temperatura.append(temperatura_actual)
            humedad.append(humedad_actual)

    return horas, co2, temperatura, humedad

def calcular_min_max(valores):
    min_valor = min(valores)
    max_valor = max(valores)
    hora_min = horas[valores.index(min_valor)]
    hora_max = horas[valores.index(max_valor)]

    return min_valor, max_valor, hora_min, hora_max

def calcular_promedio(valores):
    promedio = round(sum(valores) / len(valores), 2)
    return promedio

archivos = ["C_DIA1.txt", "C_DIA2.txt"]

for archivo_nombre in archivos:
    horas, co2, temperatura, humedad = leer_archivo(archivo_nombre)

    min_co2, max_co2, hora_min_co2, hora_max_co2 = calcular_min_max(co2)
    min_temp, max_temp, hora_min_temp, hora_max_temp = calcular_min_max(temperatura)
    min_hum, max_hum, hora_min_hum, hora_max_hum = calcular_min_max(humedad)

    promedio_co2 = calcular_promedio(co2)
    promedio_temp = calcular_promedio(temperatura)
    promedio_hum = calcular_promedio(humedad)

    print(f"{archivo_nombre}:\n")
    print("CO2:")
    print(f"- Mínimo: {min_co2} - {hora_min_co2}")
    print(f"- Máximo: {max_co2} - {hora_max_co2}")
    print(f"- Promedio: {promedio_co2}")
    print("\nTemperatura:")
    print(f"- Mínimo: {min_temp} - {hora_min_temp}")
    print(f"- Máximo: {max_temp} - {hora_max_temp}")
    print(f"- Promedio: {promedio_temp}")
    print("\nHumedad:")
    print(f"- Mínimo: {min_hum} - {hora_min_hum}")
    print(f"- Máximo: {max_hum} - {hora_max_hum}")
    print(f"- Promedio: {promedio_hum}")
    print("\n")
