# 輸出全年成交平均重量的標準差 e.g. 2.3954 std
# 輸出全年成交平均價格的中位數 e.g. 70.82 median
# 輸出全年成交平均重量的第三個四分位數 124.1 
import numpy as np
pig = np.genfromtxt("pig.csv",delimiter=",",skip_header=1)
print(f"全年成交平均重量的標準差:{pig[:,1].std(axis=0):.2f}")
print(f"全年成交平均價格的中位數:{np.median(pig[:,2]):.4f}")
print(f"全年成交平均重量的第三個四分位數:{np.percentile(pig[:,1],75):.4f}")