import threading
import time
import serial
from excel import agregar_datos_a_excel, generar_grafico
from arduino import leer

if __name__ == "__main__":
    archivo_datos = 'datos.dat'  # Archivo de datos de entrada
    archivo_existente = 'resources\datos.xlsx'  # Reemplaza con el nombre de tu archivo Excel existente

    # Configura la conexión serial para Arduino
    puerto_arduino = 'COM4'  # Cambia al puerto correcto de Arduino
    arduino = serial.Serial(puerto_arduino, baudrate=9600, timeout=1)

    # Crear una lista para almacenar los hilos
    threads = []

    # Inicia un hilo para la lectura de Arduino desde arduino.py
    arduino_thread = threading.Thread(target=leer, args=(archivo_datos, arduino))
    threads.append(arduino_thread)

    # Inicia un hilo para la actualización en tiempo real del archivo Excel desde excel.py
    excel_thread = threading.Thread(target=agregar_datos_a_excel, args=(archivo_datos, archivo_existente, 'Sheet'))
    threads.append(excel_thread)

    # Iniciar el hilo de Arduino
    arduino_thread.start()

    try:
        while True:
            # Solicitar al usuario si desea generar gráficos con Excel
            generar_grafico_opcion = input("¿Desea generar gráficos con Excel? (s/n): ")

            if generar_grafico_opcion.lower() == 's':
                # Solicitar el nombre de la hoja en Excel
                nombre_hoja = input("Ingrese el nombre de la hoja para los datos y el gráfico (sin espacios): ")
                
                # Crear una nueva hoja de Excel con los datos del rango especificado
                agregar_datos_a_excel(archivo_datos, archivo_existente, nombre_hoja)

                # Generar un gráfico con los datos de la nueva hoja
                generar_grafico(archivo_existente, nombre_hoja)

            # Esperar un segundo antes de volver a verificar
            time.sleep(1)

    except KeyboardInterrupt:
        # Cuando se presiona Ctrl+C, detén los hilos y finaliza el programa
        for thread in threads:
            thread.join()