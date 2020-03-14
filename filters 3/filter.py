from skimage.restoration import denoise_bilateral
from scipy.signal import wiener
from config import tic, toc 

### Bilateral ###
def bilateral_filter_(dataset,kernel = 5):
    filtered_bilateral= []
    time_array_bilateral = []

    for image in dataset:
        tic()
        filtered_bilateral.append( denoise_bilateral( image, kernel ) )
        time_array_bilateral.append(toc())
    return filtered_bilateral, time_array_bilateral

### Wiener ###
def wiener_filter_(dataset,kernel = (5,5)):
    filtered_wiener = []
    time_array_wiener = []

    for image in dataset:
        tic()
        filtered_wiener.append(wiener( image, kernel)) 
        time_array_wiener.append(toc())
    return filtered_wiener, time_array_wiener