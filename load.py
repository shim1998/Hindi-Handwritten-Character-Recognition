import cv2
import re
import os
import numpy as np
import pandas as pd

def writefile(data,path):
    df=pd.DataFrame(np.array(data,dtype="object"))
    with open(path,'a+') as f:
        df.to_csv(f,mode='w',header=False)

def load_images_from_folder(folder,letter):
    flag=0
    images = []
    for filename in os.listdir(folder):
        final=[]
        img = cv2.imread(os.path.join(folder,filename))
        final.append(letter)
        final.append(img.flatten())
        writefile(final,'dataset.csv')
        # if flag==0:
        #     cv2.imshow('image',img)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()
        #     flag=1
        if img is not None:
            images.append(img)
    return images

hindi_letters=['ka','kha','ga','gha','kna','cha','chha','ja','jha','yna','taa','thaa','daa','dhaa','adna','ta','tha','da','na','pa','pha','ba','bha','ma','yaw','ra','la','va','sha','petchirayakha','patalosaw','ha','chaya','tra','gya']
path='dataset/Test/character_'
for i in range(0,1):
    load_images_from_folder(path+str(i+1)+'_'+hindi_letters[i],hindi_letters[i])    
