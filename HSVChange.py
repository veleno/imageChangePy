import sys
from PIL import Image

def hsvFromRgb(r,g,b):
    r /= 256.0
    g /= 256.0
    b /= 256.0
    nmax = max(r,g,b)
    nmin = min(r,g,b)
    h = nmax - nmin
    if h > 0.0:
        if nmax == r:
            h = (g - b) / h
            if h < 0:
                h += 6.0
        elif nmax == g:
            h = 2.0 + (b - r) / h
        else:
            h = 4.0 + (r - g) / h
    h /= 6.0
    s = nmax - nmin
    if nmax != 0.0:
        s  /= nmax
    v = nmax
    return (h,s,v)

def rgbFromHsv(h,s,v):
    r = g = b = v
    if s > 0.0:
        h *= 6.0
        i = int(h)
        f = h - i
        if i==0:
            g *= 1 - s * (1 - f)
            b *= 1 - s
        elif i==1:
            r *= 1 - s * f
            b *= 1 - s
        elif i==2:
            r *= 1 - s
            b *= 1 - s * (1 - f)
        elif i==3:
            r *= 1 - s
            g *= 1 - s * f
        elif i==4:
            r *= 1 - s * (1 - f)
            g *= 1 - s
        elif i==5:
            g *= 1 - s
            b *= 1 - s * f
    return (int(r*256),int(g*256),int(b*256))

    

def imageFilter(img, args):
    width, height = img.size
    pix = img.load()
    for jj in range(height):
        for ii in range(width):
            #print pix[ii,jj]
            (r,g,b) = pix[ii,jj]
            (h,s,v) = hsvFromRgb(r,g,b)
            #print r,g,b,a
            #print h
            #print len(args)
            for arg in args:
                #print arg
                if 'hueMax' in arg and 'hueMax' in arg and (h < arg['hueMin'] or h > arg['hueMax']):
                    continue
                if 'satMax' in arg and 'satMax' in arg and (s < arg['satMin'] or s > arg['satMax']):
                    continue
                if 'valMax' in arg and 'valMax' in arg and (v < arg['valMin'] or v > arg['valMax']):
                    continue
                if 'hueAdd' in arg:
                    h += arg['hueAdd']
                if 'satAdd' in arg:
                    s += arg['satAdd']
                if 'valAdd' in arg:
                    v += arg['valAdd']
                if h >= 1:
                    h -= 1
                #print h
                (r2,g2,b2) = rgbFromHsv(h,s,v)
                pix[ii,jj] = (r2,g2,b2)
                    

# #operation = sys.argv[0]
# #print operation
# orgFileName = sys.argv[1]
# newFileName = sys.argv[2]
# hue = float(sys.argv[3])

# img = Image.open(orgFileName)
# #gray_img = img.convert('L')
# #gray_img.save('gray.png')
# #img.thumbnail((360,640))
# #img.save('thm.png')
# #print img.size
# (width,height) = img.size
# #print width
# pix = img.load()
# for jj in range(height):
#     for ii in range(width):
#         #print pix[ii,jj]
#         (r,g,b) = pix[ii,jj]
#         #print hsvFromRgb(r,g,b)
#         (h,s,v) = hsvFromRgb(r,g,b)
#         h += hue
#         if h >= 1:
#             h -= 1
#         (r2,g2,b2) = rgbFromHsv(h,s,v)
#         pix[ii,jj] = (r2,g2,b2)
# img.save(newFileName)


