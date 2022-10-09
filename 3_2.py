# from urllib import response
# import os
# from pathlib import Path
import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW",timeout=(2,5)) #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
list=[]
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"): #針對匯率表格分析
    cell = single_tr.findAll("td") #找到每一個表格
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] #找到表格中幣別
    currency_name = currency_name.replace("\r","") #取代不需要的字元
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    bid_rate = cell[1].contents[0]
    ask_rate = cell[2].contents[0] #找到幣別匯率
    if ask_rate != "-":
        list.append([float(ask_rate)-float(bid_rate),currency_name])



    # print(currency_name,ask_rate,bid_rate)
    file_name = "bankRate" + currency_name + ".csv" #每種幣別存一個檔案
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime()) #記錄目前時間
    if not exists(file_name):
        data = [['時間', '匯率'], [now_time, ask_rate]] #準備寫入檔案資料
    else:
        data = [[now_time, ask_rate]]
    f = open(file_name, "a") #開啟檔案
    w = csv.writer(f) #建立寫入CSV物件
    w.writerows(data) #寫入資料
    f.close()


list=sorted(list,key=lambda a :a[1],reverse=True)
# for i in list:
#     print(i[0],i[1])
print(f"{list[0][1]}\t{list[0][0]:.4f}")
print(f"{list[1][1]}\t{list[1][0]:.4f}")
print(f"{list[2][1]}\t{list[2][0]:.4f}")
