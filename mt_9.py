import requests as rq
from bs4 import BeautifulSoup
n = int(input())
L=[input() for _ in range(n)]
m = int(input())
if(m%2==0):
    m-=1
url=f"https://www.etax.nat.gov.tw/etw-main/ETW183W2_1110{m}/"
html = rq.get(url,timeout=(2,5))
soup = BeautifulSoup(html.content,"lxml")
tr1 = soup.find("tbody").find_all("tr")[1].find("td").text
tr3 = soup.find("tbody").find_all("tr")[3].find("td").text
tr5s = []
for tr5 in soup.find("tbody").find_all("tr")[5].find("td").find("div").find_all("div"):
    a = tr5.text.replace(" ","")
    a = a.replace("\n","")
    tr5s.append(a)
tr1 = tr1.replace(" ","")
tr3 = tr3.replace(" ","")
tr1 = tr1.replace("\n","")
tr3 = tr3.replace("\n","")
total=0
pNameList=["特別獎","特獎","頭獎","二獎","三獎","四獎","五獎","六獎"]
moneyList=[10000000,2000000,200000,40000,10000,4000,1000,200]
for receipt in L:
    pname="無"
    money=0
    if (receipt==tr1):
        pname=pNameList[0]
        money+=moneyList[0]
    elif(receipt==tr3):
        pname=pNameList[1]
        money+=moneyList[1]
    else:
        flag=0
        for tr5 in tr5s:
            for i in range(6):
                if (receipt[i:8]==tr5[i:8]):
                    pname=pNameList[i+2]
                    money+=moneyList[i+2]
                    flag=1
                    break
            if (flag):
                break
    total+=money
    print(f"{receipt} {pname} {money}")
print(f"total_price：{total}")

# 3
# 05701949
# 97718570
# 65038222
# 7
# 4
# 82150976
# 12345486
# 48631657
# 44444516
# 1
# 3
# 28467179
# 16424386
# 12220402
# 4