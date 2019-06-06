import cv2
import re
import os
import numpy as np
import pandas as pd

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

hindi_letters=['ka','kha','ga','gha','kna','cha','chha','ja','jha','yna','taa','thaa','daa','dhaa','adna','ta','tha','da','na','pa','pha','ba','bha','ma','yaw','ra','la','va','sha','petchirayakha','patalosaw','ha','chaya','tra','gya']
path='dataset/test/character_'
for i in range(0,36):
    load_images_from_folder(path+str(i+1))    
