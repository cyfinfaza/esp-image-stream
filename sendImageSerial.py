from resizeImage import openAndResize
import serial
import time

pixels = openAndResize("www.google.com_.png")

ser = serial.Serial('COM9', 921600)
# ser = serial.Serial('COM9', 1152000)

time.sleep(1)
start = time.perf_counter()
for y in range(240):
	for x in range(320):
		r, g, b, _ = pixels[x, y]
		color = int(r/255*0b11111) << 11 | int(g/255*0b111111) << 5 | int(b/255*0b11111)
		# print(r, g, b)
		# print(color & 0b1111100000000000 >> 11, color & 0b0000011111100000 >> 5, color & 0b0000000000011111)
		# input()
		ser.write(bytes([(color & 0xFF00) >> 8, color & 0x00FF]))
	print(f"Transmitting {int(y/239*100)}%", end="\r")
print()
input(f"Done. {time.perf_counter()-start}s")
ser.close()