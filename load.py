import cv2
import re
import os
import numpy as np
import pandas as pd

def writefile(data,path):
    df=pd.DataFrame(np.array(data,dtype="object"))
    with open(path,'a+') as f:
        df.to_csv(f,mode='a',header=False)

def load_images_from_folder(folder,letter):
    # flag=0
    images = []
    for filename in os.listdir(folder):
        final=[]
        img = cv2.imread(os.path.join(folder,filename),0)
        img=255-img
        roi=img[2:30,2:30]
        final.append([letter]+list(roi.flatten()))
        writefile(final,'dataset.csv')
        # if flag==0:
        #     cv2.imshow('image',img)
        #     cv2.imshow('cropped',roi)
        #     print(img.shape)
        #     print(roi.shape)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()
        #     flag=1
        if img is not None:
            images.append(img)
    return images

hindi_letters=['ka','kha','ga','gha','kna','cha','chha','ja','jha','yna','taa','thaa','daa','dhaa','adna','ta','tha','da','dha','na','pa','pha','ba','bha','ma','yaw','ra','la','va','sha','petchiryakha','patalosaw','ha','chhya','tra','gya']
path='dataset/Test/character_'
for i in range(0,36):
    load_images_from_folder(path+str(i+1)+'_'+hindi_letters[i],hindi_letters[i])    
    print(hindi_letters[i])
path='dataset/Train/character_'
for i in range(0,36):
    load_images_from_folder(path+str(i+1)+'_'+hindi_letters[i],hindi_letters[i])    
    print(hindi_letters[i])
path='dataset/Test/digit_'
for i in range(0,10):
    load_images_from_folder(path+str(i),str(i))    
    print(i)
path='dataset/Train/digit_'
for i in range(0,10):
    load_images_from_folder(path+str(i),str(i))    
    print(i)
