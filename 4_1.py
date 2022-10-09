from bs4 import BeautifulSoup as bs4

import requests as rq
# import pandas as pd

html = rq.get("https://tw.stock.yahoo.com/quote/2330/dividend",timeout=(2,5))
soup = bs4(html.text,"html.parser")

for single_li in soup.find("ul",{"class":"M(0) P(0) List(n)"}).findAll("li"):
    year = single_li.find("div",{"class":"D(f) W(98px) Ta(start)"})
    dividend = single_li.find("span")
    print(f"{year.text} {dividend.text}")
