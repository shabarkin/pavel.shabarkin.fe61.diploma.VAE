
from config import dataset_importing
from config import NUMBER_OF_PICTURES_TO_CREATE,COVER_IMG_TYPE,STEGO_IMG_TYPE

from filter import bilateral_filter_, wiener_filter_

from metric import MSE, SSIM, NCC, FS_SCORE

# GENERATE SAMPLES FOR FILTERING #
def generate_all_type_of_samples(path_cover,path_stego_mg,path_stego_uniward):
    
    # COVER SAMPLES #
    print("COVER:")
    cover = dataset_importing(path_cover,COVER_IMG_TYPE,NUMBER_OF_PICTURES_TO_CREATE)

    print("\nMG:")
    # MG STEGO SAMPLES #

    stego_mg = []
    for path_stego_mg_payload in path_stego_mg:
        stego_mg.append(dataset_importing( path_stego_mg_payload, STEGO_IMG_TYPE, NUMBER_OF_PICTURES_TO_CREATE))



    print("\nS-UNIWARD:")
    # UNIWARD STEGO SAMPLES #
    stego_uniward = []
    for path_stego_uniward_payload in path_stego_uniward:
        stego_uniward.append(dataset_importing( path_stego_uniward_payload, STEGO_IMG_TYPE, NUMBER_OF_PICTURES_TO_CREATE))

    return cover, stego_mg, stego_uniward


# PASS SAMPLES VIA BILATERAL FILTER #
def bilateral_all_samples(cover,stego_mg,stego_uniward):
    # COVER SAMPLES #
    bilateral_cover , time_array_bilateral_cover = bilateral_filter_(cover)


    # MG STEGO SAMPLES #
    bilateral_stego_mg = [] 
    time_array_bilateral_stego_mg = []

    for stego_mg_payload in stego_mg:

        bilateral_stego_payload , time_array_bilateral_stego_mg_payload = bilateral_filter_( stego_mg_payload )

        bilateral_stego_mg.append( bilateral_stego_payload )
        time_array_bilateral_stego_mg.append( time_array_bilateral_stego_mg_payload )



    # UNIWARD STEGO SAMPLES #
    bilateral_stego_uniward = [] 
    time_array_bilateral_stego_uniward = []

    for stego_uniward_payload in stego_uniward:

        bilateral_stego_payload , time_array_bilateral_stego_uniward_payload = bilateral_filter_( stego_uniward_payload )

        bilateral_stego_uniward.append( bilateral_stego_payload )
        time_array_bilateral_stego_uniward.append( time_array_bilateral_stego_uniward_payload )
        
    return bilateral_cover, bilateral_stego_mg, bilateral_stego_uniward


# PASS SAMPLES VIA WIENER FILTER #

# COVER SAMPLES #
def wiener_all_samples(cover,stego_mg,stego_uniward):
    
    wiener_cover , time_array_wiener_cover = wiener_filter_(cover)


    # MG STEGO SAMPLES #
    wiener_stego_mg = [] 
    time_array_wiener_stego_mg = []

    for stego_mg_payload in stego_mg:

        wiener_stego_payload , time_array_wiener_stego_mg_payload = wiener_filter_( stego_mg_payload )

        wiener_stego_mg.append( wiener_stego_payload )
        time_array_wiener_stego_mg.append( time_array_wiener_stego_mg_payload )



    # UNIWARD STEGO SAMPLES #
    wiener_stego_uniward = [] 
    time_array_wiener_stego_uniward = []

    for stego_uniward_payload in stego_uniward:

        wiener_stego_payload , time_array_wiener_stego_uniward_payload = wiener_filter_( stego_uniward_payload )

        wiener_stego_uniward.append( wiener_stego_payload )
        time_array_wiener_stego_uniward.append( time_array_wiener_stego_uniward_payload )
        
    return wiener_cover, wiener_stego_mg, wiener_stego_uniward


# MSE FOR ALL DATASETS # 
def mse_all_samples(cover, bilateral_cover,wiener_cover, 
                    stego_mg, bilateral_stego_mg, wiener_stego_mg,  
                    stego_uniward, bilateral_stego_uniward, wiener_stego_uniward):
    # COVER BILATERAL#

    MSE_bilateral_cover = MSE(cover,bilateral_cover)

    # COVER WIENER #
    MSE_wiener_cover = MSE(cover,wiener_cover)



    # MG BILATERAL #
    MSE_bilateral_stego_mg = []
    for i in range(len(stego_mg)):
        MSE_bilateral_stego_mg.append( MSE( stego_mg[i], bilateral_stego_mg[i] ))

    # MG WIENER #
    MSE_wiener_stego_mg = []
    for i in range(len(stego_mg)):
        MSE_wiener_stego_mg.append( MSE( stego_mg[i], wiener_stego_mg[i] ))



        
    # S-UNIWARD BILATERAL #
    MSE_bilateral_stego_uniward = []
    for i in range(len(stego_uniward)):
        MSE_bilateral_stego_uniward.append( MSE( stego_uniward[i], bilateral_stego_uniward[i] ))

    # S-UNIWARD WIENER #
    MSE_wiener_stego_uniward = []
    for i in range(len(stego_uniward)):
        MSE_wiener_stego_uniward.append( MSE( stego_uniward[i], wiener_stego_uniward[i] ))
        
    return MSE_bilateral_cover, MSE_wiener_cover, MSE_bilateral_stego_mg, MSE_wiener_stego_mg, MSE_bilateral_stego_uniward, MSE_wiener_stego_uniward


# SSIM FOR ALL DATASETS # 

def ssim_all_samples(cover, bilateral_cover, wiener_cover, 
                    stego_mg, bilateral_stego_mg, wiener_stego_mg,  
                    stego_uniward, bilateral_stego_uniward, wiener_stego_uniward):
    # COVER BILATERAL#
    SSIM_bilateral_cover = SSIM(cover,bilateral_cover)

    # COVER WIENER #
    SSIM_wiener_cover = SSIM(cover,wiener_cover)



    # MG BILATERAL #
    SSIM_bilateral_stego_mg = []
    for i in range(len(stego_mg)):
        SSIM_bilateral_stego_mg.append( SSIM( stego_mg[i], bilateral_stego_mg[i] ))

    # MG WIENER #
    SSIM_wiener_stego_mg = []
    for i in range(len(stego_mg)):
        SSIM_wiener_stego_mg.append( SSIM( stego_mg[i], wiener_stego_mg[i] ))




    # S-UNIWARD BILATERAL #
    SSIM_bilateral_stego_uniward = []
    for i in range(len(stego_uniward)):
        SSIM_bilateral_stego_uniward.append( SSIM( stego_uniward[i], bilateral_stego_uniward[i] ))

    # S-UNIWARD WIENER #
    SSIM_wiener_stego_uniward = []
    for i in range(len(stego_uniward)):
        SSIM_wiener_stego_uniward.append( SSIM( stego_uniward[i], wiener_stego_uniward[i] ))

    return SSIM_bilateral_cover, SSIM_wiener_cover, SSIM_bilateral_stego_mg, SSIM_wiener_stego_mg, SSIM_bilateral_stego_uniward, SSIM_wiener_stego_uniward



# NCC FOR ALL DATASETS # 

def ncc_all_samples(cover, bilateral_cover, wiener_cover, 
                    stego_mg, bilateral_stego_mg, wiener_stego_mg,  
                    stego_uniward, bilateral_stego_uniward, wiener_stego_uniward):
    # COVER BILATERAL#
    NCC_bilateral_cover = NCC(cover,bilateral_cover)

    # COVER WIENER #
    NCC_wiener_cover = NCC(cover,wiener_cover)



    # MG BILATERAL #
    NCC_bilateral_stego_mg = []
    for i in range(len(stego_mg)):
        NCC_bilateral_stego_mg.append( NCC( stego_mg[i], bilateral_stego_mg[i] ))

    # MG WIENER #
    NCC_wiener_stego_mg = []
    for i in range(len(stego_mg)):
        NCC_wiener_stego_mg.append( NCC( stego_mg[i], wiener_stego_mg[i] ))




    # S-UNIWARD BILATERAL #
    NCC_bilateral_stego_uniward = []
    for i in range(len(stego_uniward)):
        NCC_bilateral_stego_uniward.append( NCC( stego_uniward[i], bilateral_stego_uniward[i] ))

    # S-UNIWARD WIENER #
    NCC_wiener_stego_uniward = []
    for i in range(len(stego_uniward)):
        NCC_wiener_stego_uniward.append( NCC( stego_uniward[i], wiener_stego_uniward[i] ))
    
    return NCC_bilateral_cover, NCC_wiener_cover, NCC_bilateral_stego_mg, NCC_wiener_stego_mg, NCC_bilateral_stego_uniward, NCC_wiener_stego_uniward



# FS_SCORE FOR ALL DATASETS # 

def fs_score_all_samples(cover, stego_mg, bilateral_stego_mg, wiener_stego_mg,  stego_uniward, bilateral_stego_uniward, wiener_stego_uniward):
    # MG BILATERAL #
    FS_SCORE_bilateral_stego_mg = []
    for i in range(len(stego_mg)):
        FS_SCORE_bilateral_stego_mg.append( FS_SCORE(cover, stego_mg[i], bilateral_stego_mg[i] ))

    # MG WIENER #
    FS_SCORE_wiener_stego_mg = []
    for i in range(len(stego_mg)):
        FS_SCORE_wiener_stego_mg.append( FS_SCORE(cover, stego_mg[i], wiener_stego_mg[i] ))




    # S-UNIWARD BILATERAL #
    FS_SCORE_bilateral_stego_uniward = []
    for i in range(len(stego_uniward)):
        FS_SCORE_bilateral_stego_uniward.append( FS_SCORE(cover, stego_uniward[i], bilateral_stego_uniward[i] ))

    # S-UNIWARD WIENER #
    FS_SCORE_wiener_stego_uniward = []
    for i in range(len(stego_uniward)):
        FS_SCORE_wiener_stego_uniward.append( FS_SCORE(cover, stego_uniward[i], wiener_stego_uniward[i] ))
        
    return FS_SCORE_bilateral_stego_mg, FS_SCORE_wiener_stego_mg, FS_SCORE_bilateral_stego_uniward, FS_SCORE_wiener_stego_uniward


