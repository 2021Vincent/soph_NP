import numpy as np
import matplotlib.pyplot as plt
height = np.random.normal(170,10,1000)
height = [x for x in height if x>140 and x<201]
polyline_count = [0] * 12
pie_count = [0] *6
for h in height:
    polyline_count[int((h-140)/5)]+=1
    pie_count[int((h-140)/10)]+=1
labelsize=12
titlesize=14
plt.subplot(221)
ticks = ['141-145', '146-150', '151-155', '156-160', '161-165', '166-170', '171-175', '176-180', '181-185', '186-190', '191-195', '196-200']
plt.plot(ticks,polyline_count)
plt.title('score_range_polyline_plot', fontsize=titlesize)
plt.xlabel('Score_range', fontsize=labelsize)
plt.ylabel('Quantity', fontsize=labelsize)
plt.xticks(rotation=90)

plt.subplot(223)
labels = ["141-150", "151-160", "161-170", "171-180", "181-190", "191-200"]
plt.pie(pie_count,labels=labels,colors = ['yellowgreen', 'gold', 'lightskyblue'])
plt.title('score_range_pie_chart', fontsize=titlesize)
plt.xlabel('Score_range', fontsize=labelsize)

plt.tight_layout()
plt.show()