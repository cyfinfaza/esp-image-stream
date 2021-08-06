from PIL import Image

def openAndResize(filename, width=320, height=240):
	im = Image.open(filename)

	im = im.resize((width, height), Image.ANTIALIAS)

	# im.save('image_resized.jpg')

	pixels = im.load()

	return pixels