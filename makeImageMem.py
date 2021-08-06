from resizeImage import openAndResize

pixels = openAndResize("image2.jpg")

whitePixels = []
grayPixels = []

for y in range(240):
	for x in range(320):
		r, g, b = pixels[x, y]
		avg = (r + g + b) // 3
		whitePixels.append(True if avg >= 160 else False)
		grayPixels.append(True if avg >= 80 else False)

def arrayNotate(data):
	return ', '.join(f'0b{"".join("1" if bit else "0" for bit in data[i*8:i*8+8])}' for i in range(9600))

code = f"""
#include <Arduino.h>
uint8_t bitmap_white[] = {{
    {arrayNotate(whitePixels)}
}};
uint8_t bitmap_gray[] = {{
    {arrayNotate(grayPixels)}
}};
"""

with open(input("Save as: "), 'w') as file:
	file.write(code)