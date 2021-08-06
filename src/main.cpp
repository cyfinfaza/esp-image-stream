#include <Arduino.h>
#include <Wire.h>
#include "SPI.h"
#include "Adafruit_GFX.h"
#include "Adafruit_ILI9341.h"
#include <explosion.h>
#include <ESP8266WiFi.h>
#include "../lib/creds.h"

// For the Adafruit shield, these are the default.
#define TFT_DC D3
#define TFT_CS D8

// Use hardware SPI (on Uno, #13, #12, #11) and the above for CS/DC
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC);
// If using the breakout, change pins as desired
#define TFT_MOSI D7
#define TFT_CLK D5
#define TFT_RST D4
#define TFT_MISO D6
// Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC, TFT_MOSI, TFT_CLK, TFT_RST, TFT_MISO);

int port = 8888;  //Port number
WiFiServer server(port);

void setup() {
  Serial.begin(921600);
  
  tft.begin();

  tft.fillScreen(ILI9341_BLACK);

  tft.setRotation(1);

  WiFi.begin(WIFI_SSID, WIFI_PSK);
  tft.println("Connecting to network");
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
  }
  tft.println("Connected");
  tft.print("IP Adress: ");
  tft.println(WiFi.localIP());
  server.begin();
  tft.print("Listening at ");
  tft.print(WiFi.localIP());
  tft.print(" port ");
  tft.println(port);
  // delay(10000);

  // tft.drawBitmap(0, 0, bitmap_gray, 320, 240, 0b0010000011100100);
  // tft.drawBitmap(0, 0, bitmap_white, 320, 240, ILI9341_WHITE);

  tft.startWrite();
  tft.setAddrWindow(0, 0, 320, 240);
  // for (int i = 0; i < 9600; i+=2) {
  //   tft.pushColor(bitmap_gray[i]<<8 | bitmap_gray[i+1]);
  //   // tft.pixel(0xFFFF);
  // }

}


void loop(void) {
  // if(Serial.available()>0) {

    // while(Serial.available()<=0);
    // char msB = Serial.read();
    // while(Serial.available()<=0);
    // char lsB = Serial.read();
    // tft.pushColor(msB<<8 | lsB);

    // char data[2];
    // Serial.read(data, 2);
    // // uint16_t* color = (uint16_t*)data;
    // tft.pushColor(*(uint16_t*)data);
  // }

  WiFiClient client = server.available();
  
  if (client) {
    if(client.connected())
    {
      tft.println("Client Connected");
    }
    while(client.connected()){
      while(client.available()>0){
        uint16_t startx = client.read()<<8 | client.read();
        if(startx>320) continue;
        uint16_t starty = client.read()<<8 | client.read();
        if(starty>240) continue;
        uint16_t width = client.read()<<8 | client.read();
        if(width>320) continue;
        uint16_t height = client.read()<<8 | client.read();
        if(height>240) continue;
        Serial.printf("%d %d %d %d\n", startx, starty, width, height);
        tft.startWrite();
        tft.setAddrWindow(startx, starty, width, height);
        // read data from the connected client
        int i=0;
        while(i<width*height){
          if(client.available()>0){
            tft.pushColor(client.read()<<8 | client.read());
            i++;
          }
        }
        // Serial.write(client.read());
      }
    }
    client.stop();
    tft.println();
    tft.println("Client disconnected");    
  }
}