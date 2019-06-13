import cv2
import re
import os
import numpy as np
import pandas as pd

def writefile(data,path):
    df=pd.DataFrame(np.array(data,dtype="object"))
    with open(path,'a+') as f:
        df.to_csv(f,mode='a',header=False)

def load_images_from_folder(folder,letter,output):
    # flag=0
    images = []
    for filename in os.listdir(folder):
        final=[]
        img = cv2.imread(os.path.join(folder,filename),0)
        #img=255-img
        #roi=img[2:30,2:30]
        final.append([str(letter)]+list(img.flatten()))
        writefile(final,output)
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

# path='dataset/Train/digit_'
# for i in range(0,10):
#     load_images_from_folder(path+str(i),str(i),'dataset.csv')    
#     print(i)

def load_images_from_folder_2(folder,letter,output):
    # flag=0
    images = []
    for filename in os.listdir(folder):
        final=[]
        img = cv2.imread(os.path.join(folder,filename),0)
        img=255-img
        roi=img[2:30,2:30]
        final.append([str(letter)]+list(roi.flatten()))
        writefile(final,output)
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

path='nhcd/numerals/'
for i in range(0,10):
        load_images_from_folder(path+str(i),str(i),'dataset.csv')
        print(i)
consonants=['ka','kha','ga','gha','kna','cha','chha','ja','jha','yna','ta','tha','da','dha','ana','taa','thaa','daa','dhaa','na','pa','pha','ba','bha','ma','ya','ra','la','va','motosaw','petchiryosaw','patalosaw','ha','ksha','tra','gya']
path='nhcd/consonants/'
for i in range(0,36):
        load_images_from_folder(path+str(i+1),consonants[i],'dataset.csv')
        print(consonants[i])
path='nhcd/vowels/'
vowels=['a','aa','i','ee','u','oo','ae','ai','o','au','an','ah']
for i in range(0,10):
        load_images_from_folder(path+str(i+1),vowels[i],'dataset_of_vowels.csv')
        print(vowels[i])
print("First test Dataset ready!")

hindi_letters=['ka','kha','ga','gha','kna','cha','chha','ja','jha','yna','ta','tha','da','dha','ana','taa','thaa','daa','dhaa','na','pa','pha','ba','bha','ma','ya','ra','la','va','motosaw','petchiryosaw','patalosaw','ha','ksha','tra','gya']
path='dataset/Train/character_'
for i in range(0,36):
    load_images_from_folder_2(path+str(i+1),hindi_letters[i],'train.csv')    
    print(hindi_letters[i])
path='dataset/Train/digit_'
for i in range(0,10):
    load_images_from_folder_2(path+str(i),str(i),'train.csv')    
    print(i)
print("Train Dataset Ready!")

path='dataset/Test/character_'
for i in range(0,36):
    load_images_from_folder_2(path+str(i+1),consonants[i],'test.csv')    
    print(consonants[i])
path='dataset/Test/digit_'
for i in range(0,10):
    load_images_from_folder_2(path+str(i),str(i),'test.csv')    
    print(i)
print("Test Dataset Ready!")