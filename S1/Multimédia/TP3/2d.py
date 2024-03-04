import math

def g(x,u,N):
    return math.cos(((2*x+1)*u*math.pi)/(2*N))

def c(u):
    if u == 0:
        return 1/math.sqrt(2)
    else:
        return 1

def DCT(u,v,img):
    sum = 0
    N = len(img)
    M = len(img[0])
    for x in range(N):
        for y in range(M):
            sum = sum + img[x][y]*g(x,u,N)*g(y,v,M)
    return 2*math.sqrt(1/(N*M))*c(u)*c(v)*sum

def DCTL(img):
    dct = []
    N = len(img)
    M = len(img[0])
    for u in range(N):
        line = []
        for v in range(M):
            line.append(DCT(u,v,img))
        dct.append(line)
    return dct

img = [[200,200,200,200,100,100,100,100],
        [200,200,100,100,200,200,100,100],
        [200,100,200,100,200,100,200,100]]

def inv(x,y,dct):
    N = len(dct)
    M = len(dct[0])
    sum = 0
    for u in range(N):
        for v in range(M):
            sum = sum + c(u)*c(v)*dct[u][v]*g(x,u,N)*g(y,v,M)
    return 2*math.sqrt(1/(N*M))*sum

def DCTinv(dct):
    img = []
    N = len(dct)
    M = len(dct[0])
    for u in range(N):
        line = []
        for v in range(M):
            line.append(inv(u,v,dct))
            
        img.append(line)
    return img

img = [   
            [140, 144, 147, 140, 140, 155, 179, 175],
            [144, 152, 140, 147, 140, 148, 167, 179],
            [152, 155, 136, 167, 163, 162, 152, 172],
            [168, 145, 156, 160, 152, 155, 136, 160],
            [162, 148, 156, 148, 140, 136, 147, 162],
            [147, 167, 140, 155, 155, 140, 136, 162],
            [136, 156, 123, 167, 162, 144, 140, 147],
            [148, 155, 136, 155, 152, 147, 147, 136],
        ]


dct = DCTL(img)


for i in dct:
    for j in i:
        print(j)


# print(img)