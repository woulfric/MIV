import argparse
from PIL import Image
import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

ABSOLUTE_PATH = os.getcwd()

def compress(input):
    DICTIONARY_SIZE = 256
    dictionary = {}
    result = []
    temp = ""

    # initialiser la table ascii => fiha 256 
    for i in range(0, DICTIONARY_SIZE):
        dictionary[str(chr(i))] = i

    for c in input:
        temp2 = temp+str(chr(c))
        if temp2 in dictionary.keys():
            temp = temp2
        else:
            result.append(dictionary[temp])
            dictionary[temp2] = DICTIONARY_SIZE
            DICTIONARY_SIZE+=1
            temp = ""+str(chr(c))

    if temp != "":
        result.append(dictionary[temp])  
    
    rate = (1-(len(result)/2)/len(input))*100
        
    return result, rate

def decompress(input):
    DICTIONARY_SIZE = 256
    dictionary = {}
    result = []

    for i in range(0, DICTIONARY_SIZE):
        dictionary[i] = str(chr(i))

    previous = chr(input[0])
    input = input[1:]
    result.append(previous)

    for bit in input:
        aux = ""
        if bit in dictionary.keys():
            aux = dictionary[bit]
        else:
            aux = previous+previous[0] 
        result.append(aux)
        dictionary[DICTIONARY_SIZE] = previous + aux[0]
        DICTIONARY_SIZE+= 1
        previous = aux
    return result

def compressImage(image):
    # transformation de l'image en un tableau
    input = np.array(image)

    # sauvegarde de la taille et du mode de l'image (au debut de la chaine) pour pouvoir reconstruire l'image d'origine
    w,h = image.size
    mode = image.mode    

    # image en niveau de gris ou en couleur
    compressedImage = [h,w,1 if mode =='L' else 3]

    compressedResults = compress(input.flatten())
    compressedImage.extend(compressedResults[0])
    print(f"taux de compression {compressedResults[1]}")
    return compressedImage

def decompressImage(input):
    # récuperer la taille et le mode
    w=input.pop(0)
    h=input.pop(0)
    mode=input.pop(0)

    if mode== 1:
        s=tuple([w,h])
    else :
        s=tuple([w,h,mode])

    decompressed="".join(decompress(input))

    # conversion de la chaine (retourné par LZW) en entier
    image = np.array([ord(x) for x in decompressed])
    return image.reshape(s)


def main():
    parser = argparse.ArgumentParser(description = 'Text compressor and decompressor.')
    parser.add_argument('action', choices={"compress", "decompress"}, help="Define action to be performed.")

    # choisir le mode de compression
    parser.add_argument('mode', choices={"image", "text"}, help="Define mode to be performed on.")
    parser.add_argument('-i', action = 'store', dest = 'input', required = True,
                            help = 'Input file.')
    parser.add_argument('-o', action = 'store', dest = 'output', required = True,
                            help = 'Output file.')
    arguments = parser.parse_args()

    
    if arguments.action == 'compress':
        if arguments.mode == 'text' :
            input = open(ABSOLUTE_PATH+"//"+arguments.input, "rb").read()  
        else:
            input = Image.open(ABSOLUTE_PATH+"//"+arguments.input).convert("L")

        output = open(ABSOLUTE_PATH+"//"+arguments.output, "wb")

        compressFn= compress if arguments.mode == 'text' else compressImage
        
        compressedFile = compressFn(input)
        pickle.dump(compressedFile, output)
    
    else:
        input = pickle.load(open(ABSOLUTE_PATH+"//"+arguments.input, "rb"))

        decompressFn= decompress if arguments.mode == 'text' else decompressImage
        uncompressedFile = decompressFn(input)

        if arguments.mode == 'text' :
            output = open(ABSOLUTE_PATH+"//"+arguments.output, "w")
            for l in uncompressedFile:
                    output.write(l)
            output.close()
        else:
            image=Image.fromarray(np.uint8(uncompressedFile))
            image.save(ABSOLUTE_PATH+"//"+arguments.output)

if __name__ == "__main__":
    main()