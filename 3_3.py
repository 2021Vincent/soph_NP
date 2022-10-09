import requests
import pandas as pd
city = ['基隆市', '台北市', '新北市', '桃園市', '新竹市','新竹縣','苗栗縣','台中市','彰化縣', '雲林縣', '南投縣', '嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣', '連江縣', '金門縣', '澎湖縣']
# city = []
# for _ in range(3):
#     a = input()
#     if a in all_city:
#         city.append(a)
#     else:
#         print("city_error")
#         exit()
for index, city in enumerate(city):
    data = {'strTargetField':'COUNTY','strKeyWords':'%s' % city}
    res = requests.post('https://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    roadAddressRecord ={}
    if index == 0:
        df_7_11_store = pd.read_html(res.text, header=0)[0]
        df_7_11_store['縣市'] = city
    if index > 0:
        oneCity_store = pd.read_html(res.text, header=0)[0]
        oneCity_store['縣市'] = city
        df_7_11_store = pd.concat([df_7_11_store, oneCity_store])
    count = pd.read_html(res.text, header=0)[0].shape[0]
    # print(count)
    data = pd.read_html(res.text, header=0)[0]
    # print(data)
    for i in range(count):
        fullAddress = data.iloc[i,2]
        #找城市名稱開頭，路結尾的地址字串
        start = fullAddress.find(city[0])
        end = fullAddress.find('路')+1
        #end = fullAddress.find('街')+1
        if end<3: continue #空的資料跳過
        roadAddress = fullAddress[start:end]
        #print(roadAddress)
        if roadAddress not in roadAddressRecord:
            roadAddressRecord[roadAddress]=1
        else:
            roadAddressRecord[roadAddress]+=1
    print('%2d) %-*s %4d' % (index+1, 5, city, pd.read_html(res.text, header=0)[0].shape[0]))
    # print('------印出超過 9 間小七的路名---------')
    # for key, value in roadAddressRecord.items():
    #     if value>3:
    #         print(key, ',', value)
    # print('------印出排序之後前五名---------')
    num=0
    for key, value in sorted(roadAddressRecord.items(), key=lambda item:item[1], reverse=True):
        if (num==3): break
        print(key, ',', value)
        num = num +1         
df_7_11_store.to_excel('7_11.xlsx', index=False)
