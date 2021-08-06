# ESP Image Streaming Tool
Use your ESP + ILI9341 TFT as a wireless (or wired) display
## Expectation
Do not expect very much user friendliness. This code is a complete mess. It should not be impossbile to replicate my results, though.
## Functionality
- Full 16-bit/5.5-bit color (looks better than you think)
- Wireless streaming (1/2 fps at max resolution) over Wi-Fi
- Wired "streaming" (1/16 fps at max resolution) over UART (unsupported unless you feel comfortable trying to make `./main-serial.cpp` work, which it did, as of 4 hours ago, at least?)
- Stream a puppeteer-controlled web browser to the display
- Stream desktop to the display
- Send generic images to the display
- Make your own streaming transmitter that only updates certain parts of the screen (since the protocol supports defining the address window of the ILI9341)
## How to use
1. get platformio
1. set your wifi creds in `./lib/creds.h`
1. connect your ili9341 to hardware SPI (the DC and CS pins are in `./src/main.c`)
1. build and upload to your ESP
1. install all the python dependencies
1. run one of the python scripts ending in sendImageTCP.py
## What should happen
- When the system is powered on, the screen should clear and read `Connecting to network`
- After connecting to the network, the screen should read `Connected` and 2 more lines should be displayed with the IP and port of the listening server
- When you start sending data it should just start drawing on the screen
## If that does not happen
1. i believe in you  
always remember that if you can find my contact you are free to use it  
this project is one of those little things no one will probably use, but it might get more documentation later if I find an actual use for it
## Protocol description
### Glossary
Integer: msB, lsB  
Address Window: a box that defines where the screen will draw/scan the image data  
Image Data: 2 bytes per pixel, 16-bit RGB encoding  
16-bit RGB: (msb first) 5 bits red, 6 bits green, 5 bits blue
### Flow
1. Open TCP socket
2. Send 8 byte header describing address window
3. Send image data 
4. After sending exactly `width*height*2` bytes of image data, the ESP will expect a new header, so return to step 2

|Byte(s)|Description|
|-------|-----------|
|0-1	|Address Window X (Integer)|
|2-3	|Address Window Y (Integer)|
|4-5	|Address Window Width (Integer)|
|6-7	|Address Window Height (Integer)|
|8-n	|Image Data (must be exactly `width*height*2` bytes long|
