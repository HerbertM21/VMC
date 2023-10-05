import csv
import matplotlib.pyplot as plt
import pandas
import openpyxl
from openpyxl.styles import NamedStyle, Alignment, PatternFill, Font

def agregar_datos_a_excel(archivo_datos, archivo_existente):
    try:
        # Carga el archivo de Excel existente
        libro_excel = openpyxl.load_workbook(archivo_existente)
        
        # Abre la hoja de trabajo en la que deseas agregar los datos (puedes cambiar el nombre de la hoja si es diferente)
        hoja = libro_excel.active

        # Escribe los datos en la hoja de trabajo en las columnas A, B, C y D a partir de la fila especificada (fila_inicio)
        if 'A10' not in hoja:
            hoja['A10'] = 'Fecha'
        if 'B10' not in hoja:
            hoja['B10'] = 'Hora'
        if 'C10' not in hoja:
            hoja['C10'] = 'Humedad (%)'
        if 'D10' not in hoja:
            hoja['D10'] = 'Temperatura (°C)'
        if 'E10' not in hoja:
            hoja['E10'] = 'CO2 (ppm)'

        # Aplica el estilo de encabezado existente a las celdas A10, B10, C10 y D10
        hoja['A10'].style = 'encabezado'
        hoja['B10'].style = 'encabezado'
        hoja['C10'].style = 'encabezado'
        hoja['D10'].style = 'encabezado'
        hoja['E10'].style = 'encabezado'

        siguiente_fila = 11  # Empezar desde la fila 11 para los datos

        # Abre el archivo de datos
        with open(archivo_datos, 'r') as archivo:
            lector_csv = csv.reader(archivo)

            for fila in lector_csv:
                fecha, hora, humedad, temperatura, co2 = fila
                hoja[f'A{siguiente_fila}'] = fecha
                hoja[f'B{siguiente_fila}'] = hora
                hoja[f'C{siguiente_fila}'] = float(humedad)
                hoja[f'D{siguiente_fila}'] = float(temperatura)
                hoja[f'E{siguiente_fila}'] = float(co2)

                # Aplica el estilo 'datos' a la fila actual
                for cell in hoja[f'{siguiente_fila}:{siguiente_fila}']:
                    cell.style = 'datos'

                siguiente_fila += 1

        # Guarda el archivo de Excel con los datos agregados
        libro_excel.save(archivo_existente)

        print(f"Los datos se han agregado a {archivo_existente} correctamente.")

    except Exception as e:
        print(f"Ocurrió un error al agregar los datos a Excel: {str(e)}")

if __name__ == "__main__":
    archivo_datos = 'datos.dat'  # Archivo de datos de entrada
    archivo_existente = 'resources\datos.xlsx'  # Reemplaza con el nombre de tu archivo Excel existente
    agregar_datos_a_excel(archivo_datos, archivo_existente)
