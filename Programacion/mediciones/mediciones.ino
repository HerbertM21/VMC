#include <MQ135.h>
#include <DHT.h>
#include <SPI.h>
#include <SD.h>
#include <NTPClient.h>
#include <WiFi.h>
#include <WiFiUdp.h>

#define PIN_MQ135 A2 // MQ135 Analog Input Pin
#define DHTPIN 2 // DHT Digital Input Pin
#define DHTTYPE DHT11 // DHT11
#define CS 8
//File myFile;

MQ135 mq135_sensor(PIN_MQ135);
DHT dht(DHTPIN, DHTTYPE);
//String fileName = "MiArchivo.txt";

float temperature, humidity;
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "1.cl.pool.ntp.org");
char roomName[20] = "Sala"; 

void setup() {
  Serial.begin(9600);
  dht.begin();

  // Inicializar la conexión Wi-Fi
  WiFi.begin("Nova_Kari2.4G", "25051996e");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
  }
  timeClient.begin();

  // Inicializar la tarjeta SD
  //if (!SD.begin(CS)) {
  //  Serial.println(F("Error al inicializar la tarjeta SD"));
  //  return;
  //} else {
  //  myFile = SD.open(fileName, FILE_WRITE);
  //  Serial.println("Inicialización correcta.");
  //}

  // Esperar a recibir el nombre de la habitación desde Python
  //while (!Serial.available()) {
  //  delay(1000);
  //  Serial.println("Esperando el nombre de la habitación desde Python...");
  //}
  
  // Leer el nombre de la habitación desde Python
  //int bytesRead = Serial.readBytesUntil('\n', roomName, sizeof(roomName) - 1); // Lee datos desde el puerto serial hasta que se encuentra el carácter de nueva línea '\n'
  //roomName[bytesRead] = '\0';
  //Serial.print("Habitación actual: ");
  //Serial.println(roomName);
}

void loop() {
  // Obtener la fecha y hora actual a través de la conexión Wi-Fi
  timeClient.update();

  // Leer los datos de los sensores
  humidity = dht.readHumidity();
  temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println(F("Error al leer el sensor DHT11"));
    return;
  }

  float ppm = mq135_sensor.getCorrectedPPM(temperature, humidity);

  // Crear el nombre del archivo basado en la habitación
  //String fileName = String(roomName) + "_data.txt";

  // Imprimir los datos de los sensores en el puerto serial
  //Serial.print("Hora: ");
  //Serial.print(timeClient.getFormattedTime());
  // Imprime los datos separados por comas
  Serial.print(humidity);
  Serial.print(",");
  Serial.print(temperature);
  Serial.print(",");
  Serial.println(ppm);

  // Esperar un tiempo antes de la siguiente lectura
  delay(500);
}

///
//void registrarSD(){

//  float ppm;
//  ppm = mq135_sensor.getCorrectedPPM(temperature, humidity);
  // Escribir los datos en el archivo de texto
//  myFile = SD.open(fileName, FILE_WRITE);

//  if (myFile) {
    // Imprimir un mensaje indicando que se están guardando los datos
//    Serial.println("Guardando datos en la tarjeta SD...");
//    myFile.print(timeClient.getFormattedTime());
//    myFile.print(",");
//    myFile.print(humidity);
//    myFile.print(",");
//    myFile.print(temperature);
//    myFile.print(",");
//    myFile.println(ppm);
//    delay(500);
//    myFile.close();
//    delay(500);
//  } else {
//    Serial.println("Error al abrir el archivo en la tarjeta SD");
//    delay(2000);
 // }
///}
