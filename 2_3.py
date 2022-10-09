# 載入 pig.csv
# 輸出全年成交平均重量的成交頭數，最低前 5 筆資料(平均重量)
# eg.
# 101
# 100
# 90
# 101
# 90
# 輸出全年成交平均價格的成交頭數，最高前 5 筆資料(平均價格)
# eg.
# 90
# 90
# 91
# 91
# 100
# 輸出全年成交平均重量的成交頭數，最低前 5 筆資料，原本資料的次序編號
# eg.
# 295
# 546
# 1255
# 2973
# 2084

import numpy as np
pig = np.genfromtxt("pig.csv",delimiter=",",skip_header=1)
a=np.arange(1,len(pig)+1).reshape(len(pig),1)
# a=np.reshape(a,[len(pig)])
pig = np.append(pig,a,axis=1)
# print(a)
# print(a)
# for elem in pig :
#     print(elem[0],elem[1],elem[2],elem[3])
pig1 = sorted(pig,key=lambda a: a[1])
pig2 = sorted(pig,key=lambda a: a[2])

print("全年成交平均重量的成交頭數，最低前 5 筆資料(平均重量)")
for i in range(5):
    print(f"{pig1[i][0]:.0f}")
print("全年成交平均價格的成交頭數，最高前 5 筆資料(平均價格)")
for i in range(-1,-6,-1):
    print(f"{pig2[i][0]:.0f}")
print("全年成交平均重量的成交頭數，最低前 5 筆資料，原本資料的次序編號")
for i in range(5):
    print(f"{pig1[i][3]:.0f}")