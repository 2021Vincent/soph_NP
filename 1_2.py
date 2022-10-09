import urllib.request #匯入套件
# import zipfile
import csv
import codecs as cds
# 公開資料檔案
url ='https://www.aec.gov.tw/dataopen/index.php?id=2'
pmi = 'pmi.csv'
urllib.request.urlretrieve(url,pmi)
a=int(input())
b=int(input())
c=int(input())
d=int(input())
with open('pmi.csv','r',newline="",encoding="ANSI") as csvfile:
    readfile=csv.reader(csvfile)
    mylist=[]
    p=0
    for row in readfile:
        if p==0:
            p=1
            continue
        if (float(row[4]))>a-c and (float(row[4]))<a+c and (float(row[5]))>b-d and (float(row[5]))<b+d:
            mylist.append(row)
    # sorted(mylist,key=lambda data:float(data[2])*1000)
    for row in mylist:
        print(f"{row[0]} {row[1]} {row[2]}")
        # print(f"{row[1]} \t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")

