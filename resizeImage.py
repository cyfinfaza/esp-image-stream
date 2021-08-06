from PIL import Image

def openAndResize(filename):
	im = Image.open(filename)

	im = im.resize((320, 240), Image.ANTIALIAS)

	# im.save('image_resized.jpg')

	pixels = im.load()

	return pixels