import requests as rq
from bs4 import BeautifulSoup as bs
# import pandas as pd
url='https://scweb.cwb.gov.tw/zh-tw/earthquake/world/#'

html= rq.get(url,)
soup=bs(html.content,"lxml")
L=[]
for tr in soup.find("tbody").find_all("tr"):

    tds = tr.find_all("td")
    date = tds[0].text
    dep=tds[3].text
    mag=tds[4].text
    posi=tds[5].text
    posi=posi.replace("\r","") #取代不需要的字元
    posi=posi.replace("\n","")
    posi=posi.replace(" ","")
    dep=dep.replace("\r","") #取代不需要的字元
    dep=dep.replace("\n","")
    dep=dep.replace(" ","")
    mag=mag.replace("\r","") #取代不需要的字元
    mag=mag.replace("\n","")
    mag=mag.replace(" ","")
    L.append([date,dep,mag,posi])
    # print(mag)
L = sorted(L,key = lambda x :float(x[2]),reverse=True)
p=0
for a in L:
    if p<3:
        print(f"{a[0]} {a[1]} {a[2]} {a[3]}")
    p+=1
# p=0
# tmp=[]
# for a in L:
#     if not tmp:
#         tmp.append(a)
#     else:
#         for t in tmp:
#             if str(a[3]) == str(t[3]):
#                 tmp.append