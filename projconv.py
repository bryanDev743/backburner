# Import the Images module from pillow
from PIL import Image

# Open the image by specifying the image path.

#cpic = 

image_path = "img/pic0.jpg"
image_file = Image.open(image_path)

# the default
image_file.save("cpic0.jpg", quality=95)

# Changing the image resolution using quality parameter
# Example-1
image_file.save("cpic1.jpg", quality=25)

# Example-2
image_file.save("cpic2.jpg", quality=1)
