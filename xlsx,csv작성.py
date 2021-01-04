import csv
import openpyxl as xl
import glob

# xlsx파일 읽기
files=glob.glob('C:/Users/SNUH/Desktop/유일한/*.xlsx')
list=[]
for file in files:
    file=xl.load_workbook(file)
    file_a=file.active
    for r in file_a.rows:
        if r[0].value is None:
            continue
        list.append([])
        for c in r:
            list[-1].append(c.value)
        print(list[-1])

# csv파일읽기
files2=glob.glob('C:/Users/SNUH/Desktop/유일한/홍윤호교수님 연구/*.csv')
list=[]
for file in files2:
    file=open(file, 'r', encoding='utf-8')
    file_a=csv.reader(file)
    for line in file_a:
        print(line)
    file.close()

# csv파일 쓰기
for file in files2:
    file=open(file,'w',encoding='utf-8',newline='') #newline= 을 지정안하면 각 라인 뒤에 빈라인이 추가됨
    file_a=csv.writer(file)
    file_a.writerow([1,"aaa",False])
    file_a.writerow([2,"bbb",True])
    file_a.close()
