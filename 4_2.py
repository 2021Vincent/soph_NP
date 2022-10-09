from bs4 import BeautifulSoup as bs4

import requests as rq

url = "https://invoice.etax.nat.gov.tw/"

html = rq.get(url,timeout=(2,5))
soup = bs4(html.text,"html.parser")
haha=input()
for index,spanObj in enumerate(soup.findAll("span",{"class":{"font-weight-bold etw-color-red","font-weight-bold"}})):
    if index<2:
        if spanObj.text == haha:
            print(f"{index+1}st price")
            print(spanObj.text)
    elif index<8:
        if index%2==0:
            buff =f"{spanObj.text}" 
        else:
            # print(spanObj.text)
            buff+=f"{spanObj.text}"
            # if buff == haha:
            #     print("head price")
            # elif buff[0:3] == haha[0:3]
            print(buff)
            num=0
            congrets = "no shit"
            for i in range(7,-1,-1):
                if buff[i] == haha[i]:
                    num+=1
                if i==5:
                    if num ==3:
                        congrets="win 200"
                    elif num==2:
                        congrets="almost win 200"
                if i==0 and num==8:
                    congrets="win 200,000"
            print(congrets)


    