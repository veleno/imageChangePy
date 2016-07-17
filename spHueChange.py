import sys
from PIL import Image
import image

#operation = sys.argv[0]
#print operation
orgFileName = sys.argv[1]
newFileName = sys.argv[2]
#hue = float(sys.argv[3])
hue = 0.75

img = Image.open(orgFileName)
#gray_img = img.convert('L')
#gray_img.save('gray.png')
#img.thumbnail((360,640))
#img.save('thm.png')
#print img.size
(width,height) = img.size
#print width
pix = img.load()
for jj in range(height):
    for ii in range(width):
        #print pix[ii,jj]
        (r,g,b) = pix[ii,jj]
        #print hsvFromRgb(r,g,b)
        (h,s,v) = image.hsvFromRgb(r,g,b)
        if (0.84 <= h <= 1) or (0 <= h <= 0.01):
        #if (0.0 <= h <= 1.0):
            h += hue
            if h >= 1:
                h -= 1
            (r2,g2,b2) = image.rgbFromHsv(h,s,v)
            pix[ii,jj] = (r2,g2,b2)
img.save(newFileName)

