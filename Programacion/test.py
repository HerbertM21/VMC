import serial

# Configura el puerto serial (ajusta el puerto y la velocidad en baudios según tu configuración)
ser = serial.Serial('COM4', 9600)

valid_rooms = ["L", "C", "B", "D", "X"]  # Lista de habitaciones válidas

room_name = input("Escribe el nombre de la habitación (L, C, B, D, X): ")

if room_name not in valid_rooms:
    print("Nombre de habitación no válido. Debe ser L, C, B, D o X.")
else:
    ser.write(room_name.encode() + b'\n')  # Envía el nombre de la habitación a Arduino

ser.close()  # Cierra la conexión serial
