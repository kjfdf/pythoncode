import os.path, time
import glob
import shutil

target="C:/Users/SNUH/Desktop/유일한/practice/"
files=glob.glob("C:/Users/SNUH/Desktop/유일한/*.txt")
for file in files:
    print("last modified: %s" %time.ctime(os.path.getmtime(file))) #이걸로 작동시키면 수정시간 기준 실행
    print("created: %s" %time.ctime(os.path.getctime(file))) #이걸로 작동시키면 생성시간 기준 실행
    d=time.ctime(os.path.getctime(file))
    week=d[0:3]
    month=d[4:8]
    day=int(d[9:10])
    hour=int(d[11:13])
    min=int(d[14:16])
    sec=int(d[17:19])
    year=int(d[20:24])
    day=int(day)
    hour=int(hour)

    if year<2021 and year>2019 and day>=1:  #생성년도 2020년이고 날짜 1일이상인 것들 모두 복사해서 넣음
        shutil.copy(file,target)
