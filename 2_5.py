# 載入 bike.json
# 1. 找出空位數大於 10 的站點資料，輸出所在區、站點名稱、地址、空位數
# eg. 新店區 大鵬華城 新北市新店區中正路700巷3號 14
# 2. 根據第一點的資料，
# 統計出每一區(新店區、板橋區、....)空位數大於 10 的資料，
# 輸出每一區空位數大於 10 的所有站點個數
# eg. 新店區 15
# 3. 根據第一點的資料，
# 統計出每一區(新店區、板橋區、....)空位數大於 10 的資料，
# 輸出每一區空位數大於 10 的所有加總空位數
# e.g.
# 新店區 30
# 板橋區 50
from tkinter.tix import COLUMN
import urllib.request
import pandas as pds
# import json
url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json/preview"
jsonName ="bike.json"
urllib.request.urlretrieve(url,jsonName)
df = pds.read_json("bike.json")
print(df[df["bemp"]>10][["sarea","sna","ar","bemp"]])
# print(df1)

print(df[df["bemp"]>10].groupby(by="sarea")[["sarea"]].count())

print(df[df["bemp"]>10].groupby(by="sarea")[["bemp"]].sum())
# with open ("bike.json",encoding= "utf-8") as file:

#     data = json.load(file)
#     df = pds.DataFrame(data)
#     df1 = df.drop(['sno'], axis=1)
#     # print(df)
#     # print(df)
#     print(df1["bemp"]>10)