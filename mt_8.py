import requests as rq
import pandas as pd
citys = ['基隆市', '台北市', '新北市', '桃園市', '新竹市','新竹縣','苗栗縣','台中市','彰化縣', '雲林縣', '南投縣', 
'嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣', '連江縣', '金門縣', '澎湖縣']
Q=input()
allres=[]
for city in citys:
    data = {'strTargetField':'COUNTY','strKeyWords':city}
    rqpost = rq.post("https://www.ibon.com.tw/retail_inquiry_ajax.aspx", data=data)
    df = pd.read_html(rqpost.text, header=0)[0]
    res=[]
    # print(df)
    for _,row in df.iterrows():
        if Q in row["地址"]:
            end = row["地址"].find("號")
            start = end - 1
            while(row["地址"][start:end].isdigit()==True):
                start-=1
            compare = int(row["地址"][start+1:end])
            res.append([row["店號"],row["店名"],row["地址"],compare])
    if not res:
        continue
    allres.extend(sorted(res,key=lambda a:a[3]))

for a in allres:
    print(a[0], a[1],a[2])

