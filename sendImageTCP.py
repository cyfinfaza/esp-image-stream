from resizeImage import openAndResize
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.205", 8888))

def send(filename):
	pixels = openAndResize(filename)
	start = time.perf_counter()
	for y in range(240):
		for x in range(320):
			try:
				r, g, b = pixels[x, y]
			except:
				r, g, b, _ = pixels[x, y]
			color = int(r/255*0b11111) << 11 | int(g/255*0b111111) << 5 | int(b/255*0b11111)
			# print(r, g, b)
			# print(color & 0b1111100000000000 >> 11, color & 0b0000011111100000 >> 5, color & 0b0000000000011111)
			# input()
			s.send(bytes([(color & 0xFF00) >> 8, color & 0x00FF]))
		print(f"Transmitting {int(y/239*100)}%", end="\r")
	print()
	print(f"Done. {time.perf_counter()-start}s")


if __name__ == "__main__":
	while True:
		for i in [
				"image1.jpg",
				"image2.jpg",
				"image3.jpg",
				"image4.png",
				"image5.jpg",
			]:
			send(i)
			input()

	s.close()