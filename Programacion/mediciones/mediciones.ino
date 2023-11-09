#include <SPI.h>
#include <SD.h>
#include <MQ135.h>
#include <DHT.h>
#include <NTPClient.h>
#include <WiFi.h>
#include <WiFiUdp.h>

#define PIN_MQ135 A2 // MQ135 
#define DHTPIN 2 
#define DHTTYPE DHT11 // DHT11
const int chipSelect = 8; // SD

MQ135 mq135_sensor(PIN_MQ135);
DHT dht(DHTPIN, DHTTYPE);

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");

void setup() {
  Serial.begin(9600);
  while (!Serial);
  dht.begin();

  // Inicializar la tarjeta SD
  if (!SD.begin(chipSelect)) {
     Serial.println(F("Error al inicializar la tarjeta SD"));
     while (true);
  }

  // Intentar conectarse al Wi-Fi
  WiFi.begin("Kari", "17987721"); 

  // Esperar un tiempo razonable para la conexión WiFi
  int wifiTimeout = 30; 
  while (WiFi.status() != WL_CONNECTED && wifiTimeout > 0) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
    wifiTimeout--;
  }

  if (WiFi.status() == WL_CONNECTED) {
    timeClient.begin();
    Serial.println("Conexión exitosa a WiFi.");
  } else {
    Serial.println("No se pudo conectar a WiFi.");
  }

  Serial.println("Inicialización correcta de la SD.");
}

void loop() {
  String dataString = "";

  // Leer los datos de los sensores
  float humidityV = dht.readHumidity();
  float temperatureV = dht.readTemperature();

  if (isnan(humidityV) || isnan(temperatureV)) {
    Serial.println(F("Error al leer el sensor DHT11"));
    return;
  }

  float ppmV = mq135_sensor.getCorrectedPPM(temperatureV, humidityV);

  dataString += String(humidityV);
  dataString += ",";
  dataString += String(temperatureV);
  dataString += ",";
  dataString += String(ppmV);

  if (WiFi.status() == WL_CONNECTED) {
    // Si hay conexión Wi-Fi, agrega la hora del servidor NTP
    timeClient.update();
    dataString = String(timeClient.getFormattedTime()) + "," + dataString;
  }

  File dataFile = SD.open("datalog.txt", FILE_WRITE);

  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    Serial.println(dataString);
  } else {
    Serial.println("Error al abrir el archivo en la tarjeta SD");
    delay(2000);
  }

  // Esperar un tiempo antes de la siguiente lectura
  delay(10000);
}
