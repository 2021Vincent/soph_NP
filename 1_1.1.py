import urllib.request #匯入套件
import json
# 公開資料檔案
url ="https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json/preview"
jsonName = 'bike.json'
urllib.request.urlretrieve(url,jsonName)
with open ("bike.json",encoding="utf8") as file:
    data = json.load(file)
    list=[]
    for i in range(len(data)):
        max=0
        for item in data:
            if int(item['tot'])>max:
                max=int(item['tot'])
                ii=item
        data.remove(ii)
        list.append(ii)
    for item in list:
        # print(item['tot'])
        print([item['sno'], item['sna'],item['tot'],item['sbi'],item['ar'],item['bemp']])
