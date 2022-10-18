#import libraries
from PIL import Image, ImageChops

#file path for images
img1 = Image.open('2.jpg')
img2 = Image.open('7.jpg')

#Main difference syntax
diff = ImageChops.difference(img1, img2)
if diff.getbbox():
    diff.show()
    print('Difference Present')

else:
    print('No Difference')