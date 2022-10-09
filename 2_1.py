import numpy as np
pig = np.genfromtxt("pig.csv",delimiter=",",skip_header=1)
print(f"全年成交最低平均重量的成交頭數:{pig[pig[:,1].argmin(axis=0)][0]:.0f}")
print(f"全年成交最高平均價格的成交頭數:{pig[pig[:,2].argmax(axis=0)][0]:.0f}")
