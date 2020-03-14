import matplotlib.pyplot as plt
import numpy as np
from  sklearn import preprocessing 
from config import PAYLOAD

def average_metric(metric):
    return np.array(metric).mean()

def mean_metric_via_all_payload(metric_array):
    ave = []
    for metric in metric_array:
        ave.append(average_metric(metric))
    return ave
    
    
def normalization_metric(metric):
    metric = np.array(metric)
    metric = metric.reshape(-1, 1)
    min_max_scaler = preprocessing.MinMaxScaler()
    metric_normalized = min_max_scaler.fit_transform(metric).ravel()
    return metric_normalized

def show_low_high_metric_value(metric_array, metric_name = ""):
    for metric in metric_array:
        max_idx = np.array(metric).argmax()
        min_idx = np.array(metric).argmin()
        print(max_idx,min_idx)
        print("Picture {} - Max {}: {:.3f}".format( max_idx , metric_name, metric[max_idx]  ))
        print("Picture {} - Min {}: {:.3f}\n".format( min_idx , metric_name, metric[min_idx]  ))


    
### Show 2 images ###
def plot_2images(image,filtered,idx_img,name_filtration = 0):
    if name_filtration:
        print("[*] {} [*]".format(name_filtration))
        
    plt.imshow(image[idx_img],cmap = plt.cm.gray)
    plt.show()
    plt.imshow(filtered[idx_img],cmap = plt.cm.gray)
    plt.show()

def plot_ave_on_payloads_metric(metric):
    for i in range(len(PAYLOAD)):
        plt.title("Payload {}:".format(PAYLOAD[i]))
        plt.grid()
        plt.xlabel("Samples N")
        plt.ylabel(" Metric val")
        plt.plot(metric[i])
        plt.show()    
    
def plot_ave_on_payloads_metric_via_payloads(metrics,name_plot):
    title_ = ["MG","UNIWARD"]
    
    plt.title("{}:".format(name_plot))
    plt.grid()
    plt.xlabel("Payload %")
    plt.ylabel("Ave metric")
    plt.xticks(np.arange(6),tuple(PAYLOAD))
    for i in range(len(metrics)):
        plt.plot(metrics[i],label = title_[(i)%2] )
    plt.legend()

    plt.show()    
    
def plot_ave_metric_all_filters(metric_bilateral_stego_mg, 
                                metric_wiener_stego_mg, 
                                metric_bilateral_stego_uniward, 
                                metric_wiener_stego_uniward,
                                name = "Metric",full = True) :
    
    ave_metric_bilateral_stego_mg = mean_metric_via_all_payload(metric_bilateral_stego_mg)
    ave_metric_wiener_stego_mg = mean_metric_via_all_payload(metric_wiener_stego_mg)
    
    ave_metric_bilateral_stego_uniward = mean_metric_via_all_payload(metric_bilateral_stego_uniward)
    ave_metric_wiener_stego_uniward = mean_metric_via_all_payload(metric_wiener_stego_uniward)

    if not full:
        ave = [
            ave_metric_bilateral_stego_mg,
            ave_metric_wiener_stego_mg,
            ave_metric_bilateral_stego_uniward,
            ave_metric_wiener_stego_uniward
        ]
        plot_ave_on_payloads_metric_via_payloads(ave,name)
    else:
        ave = [
            ave_metric_bilateral_stego_mg,
            ave_metric_bilateral_stego_uniward
        ]
        plot_ave_on_payloads_metric_via_payloads(ave,name+"-BILATERAL")
        
        ave = [
            ave_metric_wiener_stego_mg,
            ave_metric_wiener_stego_uniward
        ]
        plot_ave_on_payloads_metric_via_payloads(ave,name+"-WIENER")
        