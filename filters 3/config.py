### CONFIG ###
import numpy as np
import skimage
import time

NUMBER_OF_PICTURES_TO_CREATE = 10

COVER_IMG_TYPE = 'pgm'
STEGO_IMG_TYPE = 'png'

PAYLOAD = [3,5,10,15,25,35]

BASE_PATH = '/Users/paul.tgr/aPavel/VAE_diploma/DB/'

path_cover = BASE_PATH + 'cover/'  # pgm

path_stego_mg_3 = BASE_PATH + 'stego_mg/mg_payload_3/' #png
path_stego_mg_5 = BASE_PATH + 'stego_mg/mg_payload_5/'
path_stego_mg_10 = BASE_PATH + 'stego_mg/mg_payload_10/'
path_stego_mg_15 = BASE_PATH + 'stego_mg/mg_payload_15/'
path_stego_mg_25 = BASE_PATH + 'stego_mg/mg_payload_25/'
path_stego_mg_35 = BASE_PATH + 'stego_mg/mg_payload_35/'


path_stego_uniward_3 = BASE_PATH + 'stego_uniward/uniward_payload_3/' #png
path_stego_uniward_5 = BASE_PATH + 'stego_uniward/uniward_payload_5/'
path_stego_uniward_10 = BASE_PATH + 'stego_uniward/uniward_payload_10/'
path_stego_uniward_15 = BASE_PATH + 'stego_uniward/uniward_payload_15/'
path_stego_uniward_25 = BASE_PATH + 'stego_uniward/uniward_payload_25/'
path_stego_uniward_35 = BASE_PATH + 'stego_uniward/uniward_payload_35/'

path_stego_mg = [
    path_stego_mg_3,
    path_stego_mg_5,
    path_stego_mg_10,
    path_stego_mg_15,
    path_stego_mg_25,
    path_stego_mg_35
]

path_stego_uniward = [
      path_stego_uniward_3,
      path_stego_uniward_5,
      path_stego_uniward_10,
      path_stego_uniward_15,
      path_stego_uniward_25,
      path_stego_uniward_35
]


def TicTocGenerator():
    # Generator that returns time differences
    ti = 0           # initial time
    tf = time.time() # final time
    while True:
        ti = tf
        tf = time.time()
        yield tf-ti # returns the time difference

TicToc = TicTocGenerator() # create an instance of the TicTocGen generator

# This will be the main function through which we define both tic() and toc()
def toc(tempBool=True):
    # Prints the time difference yielded by generator instance TicToc
    tempTimeInterval = next(TicToc)
    if tempBool:
        #print( "Elapsed time: %f seconds.\n" %tempTimeInterval )
        return tempTimeInterval

def tic():
    # Records a time in TicToc, marks the beginning of a time interval
    toc(False)




def dataset_importing(path = 0, file_extention = "pgm", n_samples = 100):
    if path_cover:
        tic()
        
        dataset = [ np.array( skimage.color.rgb2gray(skimage.io.imread(path + '{}.{}'.format(i,file_extention)))) for i in range(1,n_samples+1) ]
        dataset =  np.array(dataset).astype( "float64") 
        print("Creating dataset of {} samples in {:.2f}s".format(n_samples,toc()))
        
    return dataset