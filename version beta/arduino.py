import serial
import time
from datetime import datetime
from datetime import date

def leer(fichero, arduino):
    try:
        with open(fichero, 'a') as archivo:  # Abre el archivo en modo "añadir"
            while True:
                # Lee una línea de datos del Arduino
                dato = arduino.readline().decode().strip()

                # Divide los datos usando la coma como separador
                datos = dato.split(',')
            
                if len(datos) == 3:  
                    humedad = float(datos[0])
                    temperatura = float(datos[1])
                    co2 = float(datos[2])

                    # Imprime los datos leídos
                    #print(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Humedad: {humedad}%, Temperatura: {temperatura}°C, CO2: {co2} ppm") # Imprime la fecha y hora actual

                    hora_actual = datetime.now().strftime('%H:%M:%S')
                    fecha_actual = date.today().strftime('%d/%m/%Y')
                    archivo.write(f"{fecha_actual},{hora_actual},{humedad},{temperatura},{co2}\n")
                    archivo.flush()  # Forzar la escritura inmediata al archivo

    except KeyboardInterrupt:
        # Cierra la conexión serial y el archivo cuando se presiona Ctrl+C
        arduino.close()

if __name__ == '__main__':
    puerto = 'COM4'  # Cambia al puerto correcto de Arduino

    # Configura la conexión serial
    arduino = serial.Serial(puerto, baudrate=9600, timeout=1)
    fichero = "datos.dat"

    try:
        open(fichero, "a").close()
        leer(fichero, arduino)
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
