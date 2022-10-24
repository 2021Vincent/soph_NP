import pandas as pd
url ='https://data.ntpc.gov.tw/api/datasets/1688B7B8-106E-4967-AA38-DBD86D81D495/json/preview'
df = pd.read_json(url,encoding="utf-8")
b = df["ope"]=="否"
c = df["cha"]=="是"
a= df[b][c][["sta","add","no"]]
print(a)
