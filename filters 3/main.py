



if __name__ == "__main__":
    from pipeline import generate_all_type_of_samples,bilateral_all_samples,wiener_all_samples,mse_all_samples,ssim_all_samples,ncc_all_samples,fs_score_all_samples
    from config import path_cover,path_stego_mg,path_stego_uniward
    from graphics import plot_2images, plot_ave_metric_all_filters

    #  GENERATE DB COVER - STEGO_MG - STEGO_UNIWARD #
    cover,stego_mg,stego_uniward = generate_all_type_of_samples(path_cover,path_stego_mg, path_stego_uniward)

    # PASS ALL DB VIA BILATERAL #
    bilateral_cover,bilateral_stego_mg,bilateral_stego_uniward = bilateral_all_samples(cover,stego_mg,stego_uniward)

    # PASS ALL DB VIA WIENER #
    wiener_cover, wiener_stego_mg, wiener_stego_uniward = wiener_all_samples(cover, stego_mg, stego_uniward)


    # IDENTIFY MSE METRIC FOR ALL DB #
    MSE_bilateral_cover, MSE_wiener_cover, MSE_bilateral_stego_mg, MSE_wiener_stego_mg, MSE_bilateral_stego_uniward, MSE_wiener_stego_uniward =  mse_all_samples(cover, bilateral_cover, wiener_cover, stego_mg, bilateral_stego_mg, wiener_stego_mg,  stego_uniward, bilateral_stego_uniward, wiener_stego_uniward)


    # IDENTIFY SSIM METRIC FOR ALL DB #
    #SSIM_bilateral_cover, SSIM_wiener_cover, SSIM_bilateral_stego_mg, SSIM_wiener_stego_mg, SSIM_bilateral_stego_uniward, SSIM_wiener_stego_uniward = ssim_all_samples(cover, bilateral_cover, wiener_cover, stego_mg, bilateral_stego_mg, wiener_stego_mg,  stego_uniward, bilateral_stego_uniward, wiener_stego_uniward)

    # IDENTIFY NCC METRIC FOR ALL DB #
    NCC_bilateral_cover, NCC_wiener_cover, NCC_bilateral_stego_mg, NCC_wiener_stego_mg, NCC_bilateral_stego_uniward, NCC_wiener_stego_uniward = ncc_all_samples(cover, bilateral_cover, wiener_cover, stego_mg, bilateral_stego_mg, wiener_stego_mg,  stego_uniward, bilateral_stego_uniward, wiener_stego_uniward)

    # IDENTIFY FS METRIC FOR ALL DB #
    FS_SCORE_bilateral_stego_mg, FS_SCORE_wiener_stego_mg, FS_SCORE_bilateral_stego_uniward,FS_SCORE_wiener_stego_uniward = fs_score_all_samples(cover,stego_mg,  bilateral_stego_mg, wiener_stego_mg,  stego_uniward, bilateral_stego_uniward, wiener_stego_uniward)






    plot_2images(stego_mg[1],wiener_stego_mg[1],1)

    plot_ave_metric_all_filters(MSE_bilateral_stego_mg, 
                                MSE_wiener_stego_mg, 
                                MSE_bilateral_stego_uniward, 
                                MSE_wiener_stego_uniward,
                                "MSE")

    # plot_ave_metric_all_filters(SSIM_bilateral_stego_mg, 
    #                             SSIM_wiener_stego_mg, 
    #                             SSIM_bilateral_stego_uniward, 
    #                             SSIM_wiener_stego_uniward,
    #                             "SSIM")

    plot_ave_metric_all_filters(NCC_bilateral_stego_mg, 
                                NCC_wiener_stego_mg, 
                                NCC_bilateral_stego_uniward, 
                                NCC_wiener_stego_uniward,
                                "NCC")


    plot_ave_metric_all_filters(FS_SCORE_bilateral_stego_mg, 
                                FS_SCORE_wiener_stego_mg, 
                                FS_SCORE_bilateral_stego_uniward, 
                                FS_SCORE_wiener_stego_uniward,
                                "FS_SCORE")

