import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
str = input()
file_name = "output.csv"
f = open(file_name, "w", encoding = 'big5')
w = csv.writer(f)
htmlname="https://www.cwb.gov.tw/V8/C/K/bilingual_glossary.html"
html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")
cell = bsObj.find("table").find("thead").find("tr").findAll("th")
data = [[cell[0].text,cell[1].text,cell[2].text]]
w.writerows(data) # 將data寫入w物件
for single_tr in bsObj.find("table").find("tbody").findAll("tr"):
    # 對single_tr物件用findAll找所有"td"標籤,設為cell物件
    cell = single_tr.findAll("td")
    #將cell[0]、cell[1]與cell[2]中text取出(編號、英文、中文)組合為data串列
    F0 = cell[0].text
    F1 = cell[1].text
    F2 = cell[2].text
    # print(F0,F1,F2)
    if str in F1 or str in F2:
        print(f"{F1} {F2}")
    data = [[F0,F1,F2]]
    w.writerows(data) # 將data寫入w物件
f.close()