import shutil
import os

path='C:/Users/SNUH/Desktop/유일한/EMG 머신러닝 연구/EMG_data/normal_data/'
files=os.listdir(path)
dir='C:/Users/SNUH/Desktop/유일한/EMG 머신러닝 연구/EMG_data/figure4/'
for file in files:
    shutil.copy(path+file,dir+file)