import numpy as np
url='https://www.bot.com.tw/Govinfo/opendata/csv/233/110GoldPassbook.csv'
a = np.genfromtxt("110GoldPassbook.csv",encoding="UTF-8",delimiter=",",skip_header=True).astype(int)
print(a)
b=sorted(a,key=lambda x : x[3])
for i in b[0:5]:
    print(f"{i[0]} {i[3]} {i[4]}")
print(np.median(a[:,3]))
print(f"{np.mean(a[:,4],axis=0):.2f}")
print(f"{np.std(a[:,4],axis=0):.2f}")
