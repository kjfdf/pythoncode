import shutil
import os
import glob
import os.path

files = glob.glob('C:/Users/SNUH/Desktop/유일한/*.txt') #특정확장자를 가진 목록뽑기
target='C:/Users/SNUH/Desktop/유일한/practice'
for file in files:
    if not os.path.isdir(target): #target 디렉토리가 없으면 먼저 만듦
        os.mkdir(target)
    shutil.copy(file,target) #files목록내의 txt확장자를 가진 파일들을 하나씩 target 디렉토리에 옮김. 

