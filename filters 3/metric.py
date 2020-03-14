from  sklearn import preprocessing 
from keras import backend as K
import tensorflow as tf 
import numpy as np

# FS_SCORE METRIC FOR BATCH OF SAMPLES #
def fs_score(img_cover,img_stego,img_stego_filtered):
    
    
    #threshold = 0.1
    
    delta_cs = np.abs(np.array(img_cover) - np.array(img_stego))
    
 
    idx_eq_zero = np.where( delta_cs == 0 )
    
    img_stego_filtered[idx_eq_zero] = img_stego[idx_eq_zero]
    
    delta_cs_filtered = np.abs(np.array(img_stego) - np.array(img_stego_filtered))
    
    
    
    #### How many bits with payload was changed ####
    #return np.sum(( delta_cs_filtered !=0) ) / np.sum(delta_cs != 0)

    
    #### How strong all bits were changed  ####

    min_max_scaler = preprocessing.MinMaxScaler()
    delta_cs_filtered.reshape(-1, 1)
    delta_cs.reshape(-1, 1)
    delta_cs_filtered_normalized = min_max_scaler.fit_transform(delta_cs_filtered).ravel()
    delta_cs_normalized = min_max_scaler.fit_transform(delta_cs).ravel()

    return np.sum(delta_cs_filtered_normalized) / np.sum(delta_cs_normalized)

def FS_SCORE(cover, stego, stego_filtered):
    len_ = len(cover)
    fs = []
    for i in range(len_):
        fs.append( fs_score(cover[i], stego[i], stego_filtered[i] )  )
        
    return fs



# MSE METRIC FOR BATCH OF SAMPLES #

def MSE(imageA,imageB):
    err = []
    len_ = min(len(imageA),len(imageB))
    for i in range(len_):
        err.append(
            np.sqrt(np.sum((imageA[i].astype("float") - imageB[i].astype("float")) ** 2) / float(imageA[i].shape[0]*imageA[i].shape[1]))
        )
    return err


def np_to_tf_tensor(arg):
    return tf.convert_to_tensor(arg, dtype=tf.float32)

# SSIM METRIC FOR BATCH OF SAMPLES #

def ssim_decorator(y_true,y_pred):
    max_val = 255

    y_true = np_to_tf_tensor(y_true)
    y_pred = np_to_tf_tensor(y_pred)
    return tf.image.ssim(y_true,y_pred,max_val)

def SSIM(imageA,imageB):
    imageA = np.array([ np.reshape( imageA[i], (512,512,1)) for i in range(len(imageA))])
    imageB = np.array([ np.reshape( imageB[i], (512,512,1)) for i in range(len(imageB))])
    
    err = []
    len_ = min(len(imageA),len(imageB))
    for i in range(len_):
        err.append( ssim_decorator(imageA[i],imageB[i]) )
    return err



# NCC METRIC FOR BATCH OF SAMPLES #

def correlation_coefficient(patch1, patch2):
    product = np.mean((patch1 - patch1.mean()) * (patch2 - patch2.mean()))
    stds = patch1.std() * patch2.std()
    if stds == 0:
        return 0
    else:
        product /= stds
        return product

def NCC(imageA,imageB):
    imageA = np.array([ np.reshape( imageA[i], (512,512,1)) for i in range(len(imageA))])
    imageB = np.array([ np.reshape( imageB[i], (512,512,1)) for i in range(len(imageB))])
    err = []
    len_ = min(len(imageA),len(imageB))
    for i in range(len_):
        err.append( correlation_coefficient(imageA[i],imageB[i]) )
    return err
    


