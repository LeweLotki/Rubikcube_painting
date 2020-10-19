from PIL import Image, ImageDraw
import random

im = Image.open('wenus.jpg')  
n = 0
R = 0
G = 0
B = 0
cord1 = 0
cord2 = 0
m = 5
q = 1
width, height = im.size
print(width, height)

#pamietaj o average samplingu

colors = {'red' : (255, 0, 0),
          'green' : (0,255,0),
          'white' : ( 255, 255, 255 ),
          'blue' : ( 0, 0, 255 ),
          'yellow' : ( 255, 255, 0 ),
          'orange' : ( 255, 69, 0 )
          #,'black' : ( 0, 0, 0 )
          }

def classify(rgb_tuple):
    # eg. rgb_tuple = (2,44,300)

    # add as many colors as appropriate here, but for
    # the stated use case you just want to see if your
    # pixel is 'more red' or 'more green'
    colors = {'red' : (255, 0, 0),
              'green' : (0,255,0),
              'white' : ( 255, 255, 255 ),
              'blue' : ( 0, 0, 255 ),
              'yellow' : ( 255, 255, 0 ),
              'orange' : ( 255, 69, 0 )
              #,'black' : ( 0, 0, 0 )
              }

    manhattan = lambda x,y : abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2]) 
    distances = {k: manhattan(v, rgb_tuple) for k, v in colors.items()}
    color = min(distances, key=distances.get)
    return color

def average(cord1,cord2,m):
    n = 0
    R = 0
    G = 0
    B = 0
    while n < 10:
        x = random.randint(cord1, cord1 + m)
        y = random.randint(cord2, cord2 + m)
        pixel = im.getpixel((x,y))
      # print(color[0])
        R += pixel[0]
      # print(R)
        G += pixel[1]
        B += pixel[2]
        n += 1
        
      # print(n)
    avR = int(R/n)
    avG = int(G/n)
    avB = int(B/n)
    output = (avR, avG, avB)
    return output

def draw(cord1,cord2,m,tuple):
    for x in range(cord1,cord1 + m):
        for y in range(cord2,cord2 + m):
            im.putpixel((x, y), tuple)
    #im.save('F:\\art_programs\croped\saved.png')
def subdivide(cord1,cord2,m,q):
    im1 = im.crop((cord1,cord2,cord1 + 3*m,cord2 + 3*m))
    im1.save('F:\\art_programs\croped\cubes\saved'+str(q)+'.png')
    #print(cord1, cord2, cord1 + 3*m, cord2 + 3*m, q)
# print('average value in square ((0,30),(0,30)) is equal to: ', average(cord1,cord2, m))
# # print(n)
# print('It is aproximetlly: ', classify(average(cord1,cord2,m)))
# print(colors[classify(average(cord1,cord2,m))])

while True: 
    if cord1 + m >= width:
        cord1 = 0
        cord2 += m
    if cord2 + m >= height:
        break
    else:
        draw(cord1,cord2,m,colors[classify(average(cord1,cord2,m))])
        cord1 += m
        #print(cord1,cord2)
        
im.save('F:\\art_programs\croped\saved.png')

cord1 = 0
cord2 = 0

while True: 
    if cord1 + 3*m >= width:
        cord1 = 0
        cord2 += 3*m
        print(q-1)
    if cord2 + 3*m >= height:
        break
    else:
        subdivide(cord1,cord2,m,q)
        cord1 += 3*m
        q += 1
        #print(cord1,cord2)
        
        
        
        
        
        
        
        
        
