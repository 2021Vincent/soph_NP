# 使用 pandas
# 計算 2002 年全球人口各國平均數
# 計算 2002 年全球各洲平均壽命、平均財富
# import numpy as np
import pandas as pds
gapminder = pds.read_excel("gapminder.xlsx")
meanPop2002 = gapminder[gapminder['year'] == 2002][['pop']].mean()
# gapminder.head
# gapminder[gapminder['year'] == 2007][['lifeExp', 'gdpPercap']].mean()
print(f"2002 年全球人口各國平均數:{meanPop2002[0]:.4f}")

# for i in meanPop2002:
#     print(i)
# print(f"2002 年全球人口各國平均數:{meanPop2002:.4f}")
print(gapminder[gapminder["year"] == 2002].groupby(by="continent")[["lifeExp","gdpPercap"]].mean())

