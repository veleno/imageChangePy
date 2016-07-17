import sys
from PIL import Image
import image

orgFileName = sys.argv[1]
hsvFlag = sys.argv[2]   # h/s/v
#newFileName = sys.argv[2]
#valueMin = float(sys.argv[3])
#fMax = float(sys.argv[4])

def createMask(strFileName,hsvFlag,fMin,fMax):
    img = Image.open(strFileName)
    (width,height) = img.size
    pix = img.load()
    for jj in range(height):
        for ii in range(width):
            (r,g,b) = pix[ii,jj]
            (h,s,v) = image.hsvFromRgb(r,g,b)
            val = 0
            if hsvFlag == 'h': val = h
            elif hsvFlag == 's': val = s
            elif hsvFlag == 'v': val = v
            if fMin <= v < fMax:
                (r,g,b) = (255,255,255)
            else:
                (r,g,b) = (0,0,0)
            pix[ii,jj] = (r,g,b)
    #img.save(newFileName)
    img.save(strFileName+hsvFlag+str(fMin)+"-"+str(fMax)+".png")

for min in range(100):
    max = min + 1
    createMask(orgFileName,hsvFlag,min*0.01,max*0.01)
