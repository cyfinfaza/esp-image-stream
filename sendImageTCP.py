from resizeImage import openAndResize
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.205", 8888))

def byteify(number):
	return [(number & 0xFF00) >> 8, number & 0x00FF]

def send(filename, startx=0, starty=0, width=320, height=240, verbose=True, progressCounter=True):
	start = time.perf_counter()
	pixels = openAndResize(filename, width, height)
	s.send(bytes([*byteify(startx), *byteify(starty), *byteify(width), *byteify(height)]))
	for y in range(height):
		for x in range(width):
			try:
				r, g, b = pixels[x, y]
			except:
				r, g, b, _ = pixels[x, y]
			color = int(r/255*0b11111) << 11 | int(g/255*0b111111) << 5 | int(b/255*0b11111)
			# print(r, g, b)
			# print(color & 0b1111100000000000 >> 11, color & 0b0000011111100000 >> 5, color & 0b0000000000011111)
			# input()
			s.send(bytes([(color & 0xFF00) >> 8, color & 0x00FF]))
		if verbose and progressCounter: print(f"Transmitting {int(y/(height-1)*100)}%", end="\r")
	if verbose and progressCounter: print()
	if verbose: print(f"Done. {time.perf_counter()-start}s")


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