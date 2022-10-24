# import json
import pandas as pd
url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

js=pd.read_json(url)
df=pd.DataFrame(js)
# for a in df["tot"]:
#     print(a)
# df.sort_values(by=["tot"],axis=0)
# print(df1["sno"],df1["sna"])

a=df[df["tot"]>80][["sno","sna","tot"]]
print(a)
# for i in df:
#     print(i)
b=df.groupby(by="sarea")["tot"].sum()
# 統計並列出每區的場站總停車格(tot)總數

print(b)