import sys
from PIL import Image
import HSVChange

hueRange = 10
for ii in range(hueRange):
    img = Image.open('sample.png')
    #img = Image.open('test.png')
    hueAdd = (ii + 1) / float(hueRange)
    print hueAdd
    HSVChange.imageFilter(img,
                          [
                              #{'hueMin':0,          'hueMax':0.1,   'hueAdd':0.2},
                              #{'hueMin':0.83,       'hueMax':0.84,  'hueAdd':0.2},
                              #{'hueMin':0.82,       'hueMax':1,     'hueAdd':0.75},
                              #{'hueMin':0,          'hueMax':0.01,   'hueAdd':0.75},
                              #{'hueMin':0,          'hueMax':0.1,   'hueAdd':0.75},
                              #{'hueMin':0.64,          'hueMax':0.65,   'hueAdd':0.75},
                              #{'hueMin':0.97,       'hueMax':1,     'hueAdd':hueAdd, 'satMin':0, 'satMax':0.19},
                              #{'hueMin':0.97,       'hueMax':1,     'hueAdd':hueAdd, 'satMin':0.41, 'satMax':1},
                              {'hueMin':0.8,       'hueMax':1,     'hueAdd':hueAdd, 'satMin':0, 'satMax':0.19},
                              {'hueMin':0.8,       'hueMax':1,     'hueAdd':hueAdd, 'satMin':0.41, 'satMax':1},
                              {'hueMin':0,          'hueMax':0.01,   'hueAdd':hueAdd},
                              #{'hueMin':0.80,       'hueMax':1,   'hueAdd':hueAdd},
                          ])
    img.save('sample.change.' + str(hueAdd) + '.png')
#img.save('test.change.png')
