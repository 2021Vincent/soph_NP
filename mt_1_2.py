import urllib.request #匯入套件
import zipfile
import csv
# 公開資料檔案
O=int(input())
url ='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
zipName = 'F.zip' #壓縮檔案名稱
urllib.request.urlretrieve(url,zipName) #下載壓縮檔
f=zipfile.ZipFile(zipName) #開啟壓縮檔
#file_dir = './FF'
file_dir = './' #解壓縮目錄
for fileName in f.namelist(): #壓縮檔案列表檔名
    f.extract(fileName,file_dir) #擷取壓縮檔案
    # print(fileName) #印出解壓縮檔案名稱
    f.close() #關檔
f = open(fileName,'r',encoding = 'utf8') #開啟CSV檔案，，唯讀 utf-8解碼
plots = csv.reader(f, delimiter=',') #讀取CSV檔案間隔逗號，設定給plots串列物件
p=0
# L=[]
for row in plots: #印出UBIKE資料
    if p==0:
        p=1
        continue
    if int(row[12])>O:
        # L.append(row)
        print(f"{row[0]} {row[1]} {row[12]}")
f.close()
