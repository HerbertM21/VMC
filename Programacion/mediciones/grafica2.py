import csv
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

datos = input("Ingrese el nombre del archivo de datos (CSV): ")
titulo = input("Ingrese el título del gráfico: ")

hora = []
temperatura = []
co2 = []
humedad = []

with open(datos, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        hora.append(row[0])
        humedad.append(float(row[1]))
        temperatura.append(float(row[2]))
        co2.append(float(row[3]))

# Temperatura
fig_temp = px.line(x=hora, y=temperatura, labels={'x': 'Hora del día', 'y': 'Temperatura (°C)'},
                   title=f"Grafico de temperatura: {titulo}", line_shape='linear')
fig_temp.update_xaxes(tickangle=45, tickvals=hora[::500])
fig_temp.update_traces(line=dict(color='#FF5733'))

# CO2
fig_co2 = px.line(x=hora, y=co2, labels={'x': 'Hora del día', 'y': 'CO2 (ppm)'},
                  title=f"Grafico de CO2: {titulo}", line_shape='linear')
fig_co2.update_xaxes(tickangle=45, tickvals=hora[::500])
fig_co2.update_traces(line=dict(color='#27B659'))

# Humedad
fig_humedad = px.line(x=hora, y=humedad, labels={'x': 'Hora del día', 'y': 'Humedad relativa (%)'},
                      title=f"Grafico de humedad relativa: {titulo}", line_shape='linear')
fig_humedad.update_xaxes(tickangle=45, tickvals=hora[::500])
fig_humedad.update_traces(line=dict(color='#27A0B6'))

# Gráfica Combinada
fig_combined = make_subplots(rows=3, cols=1, shared_xaxes=True, subplot_titles=("Temperatura (°C)", "CO2 (ppm)", "Humedad relativa (%)"))

fig_combined.add_trace(fig_temp['data'][0], row=1, col=1)
fig_combined.add_trace(fig_co2['data'][0], row=2, col=1)
fig_combined.add_trace(fig_humedad['data'][0], row=3, col=1)

fig_combined.update_layout(title_text=f"Grafico combinado: {titulo}")

fig_combined.show()

# Crear una figura para mostrar los tres valores en una sola gráfica
fig_t = px.line(x=hora, y=temperatura, labels={'x': 'Hora del día', 'y': 'Temperatura (°C)'}, title=f"Datos resultantes: {titulo}")
fig_t.add_scatter(x=hora, y=co2, mode='lines', name='CO2 (ppm)')
fig_t.add_scatter(x=hora, y=humedad, mode='lines', name='Humedad relativa (%)')

fig_t.show()

# Mostrar gráficas individuales
fig_temp.show()
fig_co2.show()
fig_humedad.show()
