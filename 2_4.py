# 使用 Pandas
# 載入 president_heights.csv
# 輸出總統身高的敘述統計資料
# 輸出總統身高，最高前 5 筆資料
# 輸出總統身高 > 180，最低的 5 筆資料
import pandas as pds

ph = pds.read_csv("president_heights.csv",delimiter=",")
# print(ph.info)
print(ph.describe())
print(ph.sort_values(by=["height(cm)"],ascending=False)[0:5])
print(ph[ph["height(cm)"]>180].sort_values(by=["height(cm)"]).head(5))
# print(ph.sort_values(by=["height(cm)"],ascending=False).head(5))

