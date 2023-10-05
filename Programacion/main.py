import threading
import time
import serial
from excel import agregar_datos_a_excel
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
    excel_thread = threading.Thread(target=agregar_datos_a_excel, args=(archivo_datos, archivo_existente))
    threads.append(excel_thread)

    # Iniciar todos los hilos
    for thread in threads:
        thread.start()

    try:
        # Mantén el programa principal en funcionamiento para monitorear los hilos
        while True:
            # Puedes agregar lógica adicional aquí si es necesario
            time.sleep(1)
    except KeyboardInterrupt:
        # Cuando se presiona Ctrl+C, detén los hilos y finaliza el programa
        for thread in threads:
            thread.join()
