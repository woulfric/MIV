import numpy as np
import cv2
import warnings
from copy import deepcopy

warnings.filterwarnings("ignore")

# ****************************************** LZW for binary and gray scale images **************************************************************
def compress_bw_grayScale(img):

    result = []

    # Append the size of the image on the result's header
    result.append((img.shape))

    fimg = img.flatten() 
    # Create the initial dictionary 
    dictionary = {}
    DICTIONARY_SIZE = 0
    for p in fimg: 
        # Use 3 digits to encode the value of each pixel  
        p = "{0:03d}".format(p)
        # Insert the pixel's value in the dictionary if it doesn't exist
        if p not in dictionary:
            dictionary[p] = DICTIONARY_SIZE
            DICTIONARY_SIZE += 1
    # Append the initial dictionary on the result's header
    initial_dict = deepcopy(dictionary)
    result.append(initial_dict)
    
    # LZW
    temp = ""
    for p in fimg:
        temp2 = temp+"{0:03d}".format(p)      
        if temp2 in dictionary.keys():
            temp = temp2
        else:
            result.append(dictionary[temp])
            dictionary[temp2] = DICTIONARY_SIZE
            DICTIONARY_SIZE+=1
            temp = ""+"{0:03d}".format(p)
    
    if temp != "":
        result.append(dictionary[temp])  
    
    return result 

def decompress_bw_grayScale(input):
    
    # Get the size of the image and the initial dictionary from the input's header
    height, width = input[0]
    dictionary = input[1]
    DICTIONARY_SIZE = len(dictionary)
    # Switch between the keys and the values of the dictionary
    dictionary = {y: x for x, y in dictionary.items()}
    
    result = []
    previous = dictionary[input[2]]
    input = input[3:]
    result.append(previous)

    for bit in input:
        aux = ""
        if bit in dictionary.keys():
            aux = dictionary[bit]
        else:
            aux = previous+previous[0:3] 
        
        result.append(aux)
        dictionary[DICTIONARY_SIZE] = previous + aux[0:3]
        DICTIONARY_SIZE+= 1
        previous = aux

    result = "".join(result) 
    fimage = np.array([int(result[idx:idx+3]) for idx in range(0, len(result), 3)]).astype(np.uint8)
    image = np.reshape(fimage, (height, width))
    return image

# *********************************************** Test with a binary image ****************************************************************
# Compression
img_gray = cv2.imread('test_image.png', cv2.IMREAD_GRAYSCALE)
thresh, img_bw = cv2.threshold(img_gray, 100, 255, cv2.THRESH_OTSU)
cv2.imshow('Image before compression', img_bw)
cv2.waitKey(0)
compressedImage = compress_bw_grayScale(img_bw)
print (f"Compressed image length: {len(compressedImage[2:])}")

# Decompression
decompressedImage = decompress_bw_grayScale(compressedImage)
cv2.imshow('Image after decompression', decompressedImage)
cv2.waitKey(0)
error_rate = np.count_nonzero(decompressedImage - img_bw)
print (f'Error Rate: {error_rate}')   
   
# *********************************************** Test with a gray scale image ****************************************************************
# Compression
img_gray = cv2.imread('test_image.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image before compression', img_gray)
cv2.waitKey(0)
compressedImage = compress_bw_grayScale(img_gray)
print (f"Compressed image length: {len(compressedImage[2:])}")

# Decompression
decompressedImage = decompress_bw_grayScale(compressedImage)
cv2.imshow('Image after decompression', decompressedImage)
cv2.waitKey(0)
error_rate = np.count_nonzero(decompressedImage - img_gray)
print (f'Error Rate: {error_rate}')   

# ****************************************** LZW for RGB images **************************************************************
def compress_rgb(img):

    result = []

    # Append the size of the image on the result's header
    result.append((img.shape))

    fimg = img.reshape(-1, img.shape[2]) # Flatten only the first two dimensions (height and width) 
    # Create the initial dictionary 
    dictionary = {}
    DICTIONARY_SIZE = 0
    for p in fimg: 
        # p = (B, G, R)
        B, G, R = p
        # Use 3 digits to encode the value of each channel of the pixel => Total: 9 digits 
        BGR = "{0:03d}".format(B)+"{0:03d}".format(G)+"{0:03d}".format(R)
        # Insert the pixel's value in the dictionary if it doesn't exist
        if BGR not in dictionary:
            dictionary[BGR] = DICTIONARY_SIZE # The key of the dictionary is the pixel (B, G, R) values
            DICTIONARY_SIZE += 1
    # Append the initial dictionary on the result's header
    initial_dict = deepcopy(dictionary)
    result.append(initial_dict)
        
    temp = ""
    for p in fimg:
        # p = (B, G, R)
        B, G, R = p
        # Use 3 digits to encode the value of each channel of the pixel => Total: 9 digits 
        BGR = "{0:03d}".format(B)+"{0:03d}".format(G)+"{0:03d}".format(R)
        temp2 = temp+BGR      
        if temp2 in dictionary.keys():
            temp = temp2
        else:
            result.append(dictionary[temp])
            dictionary[temp2] = DICTIONARY_SIZE
            DICTIONARY_SIZE+=1
            # p = (B, G, R)
            B, G, R = p
            # Use 3 digits to encode the value of each channel of the pixel => Total: 9 digits 
            BGR = "{0:03d}".format(B)+"{0:03d}".format(G)+"{0:03d}".format(R)
            temp = ""+BGR
    
    if temp != "":
        result.append(dictionary[temp])  
    
    return result 

def decompress_rgb(input):
    
    # Get the size of the image and the initial dictionary from the input's header
    height, width, ch = input[0]
    dictionary = input[1]
    DICTIONARY_SIZE = len(dictionary)
    # Switch between the keys and the values of the dictionary
    dictionary = {y: x for x, y in dictionary.items()}
    
    result = []
    previous = dictionary[input[2]]
    input = input[3:]
    result.append(previous)

    for bit in input:
        aux = ""
        if bit in dictionary.keys():
            aux = dictionary[bit]
        else:
            aux = previous+previous[0:9] 
        
        result.append(aux)
        dictionary[DICTIONARY_SIZE] = previous + aux[0:9] # Take 9 digits from "aux" to get the BGR values of the pixel
        DICTIONARY_SIZE+= 1
        previous = aux

    result = "".join(result) 
    fimage = np.array([(int(result[idx:idx+3]), int(result[idx+3:idx+6]), int(result[idx+6:idx+9])) # Get the BGR values
                        for idx in range(0, len(result), 9)]).astype(np.uint8)
    image = np.reshape(fimage, (height, width, ch))
    return image

# *********************************************** Test with an RGB image ****************************************************************
# Compression
img_bgr = cv2.imread('test_image.png')
cv2.imshow('Image before compression', img_bgr)
cv2.waitKey(0)
compressedImage = compress_rgb(img_bgr)
print (f"Compressed image length: {len(compressedImage[2:])}")

# Decompression
decompressedImage = decompress_rgb(compressedImage)
cv2.imshow('Image after decompression', decompressedImage)
cv2.waitKey(0)
error_rate = np.count_nonzero(decompressedImage - img_bgr)
print (f'Error Rate: {error_rate}')   
      




