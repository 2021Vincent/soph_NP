import numpy as np
import matplotlib.pyplot as plt
N = int(input())
# N=1000
list=[np.random.randint(0,101) for _ in range(N)]
bar_count = [0,0]
polyline_count = [0] * 20
scatter_count = [0] * 10
pie_count = [0,0,0]
# list.append(100)
for score in list:
    polyline_count[int((score-1)/5)]+=1
    if score == 100:
        scatter_count[9] +=1
    else:
        scatter_count[int(score/10)]+=1
    if score < 60:
        bar_count[0]+=1
        pie_count[0]+=1
    else:
        bar_count[1]+=1
        if score < 81:
            pie_count[1]+=1
        else:
            pie_count[2]+=1


# print(list)
# print(polyline_count)
plt.axes()
plt.style.use('_mpl-gallery')

labelsize=12
titlesize=14
plt.subplot(2,2,1)
xindex = np.arange(0,4,2)
plt.bar(xindex,bar_count,width=0.5)
plt.title('pass_fail_bar_plot', fontsize=titlesize)
plt.xlabel('Grade', fontsize=labelsize)
plt.ylabel('Quantity', fontsize=labelsize)
plt.xticks(xindex,["pass","fail"])

plt.subplot(2,2,2)

plt.plot(["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89","90-94","95-100"],polyline_count)
plt.title('score_range_polyline_plot', fontsize=titlesize)
plt.xlabel('Score_range', fontsize=labelsize)
plt.ylabel('Quantity', fontsize=labelsize)
plt.xticks(rotation=90)

plt.subplot(2,2,3)
plt.scatter(["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80-89","90-100"],scatter_count,s=100,marker=r'$\clubsuit$')
plt.title('score_range_scatter_plot', fontsize=titlesize)
plt.xlabel('Score_range', fontsize=labelsize)
plt.ylabel('Quantity', fontsize=labelsize)
plt.xticks(rotation=90)

plt.subplot(2,2,4)
plt.pie(pie_count,labels=["0-59","60-80","81-100"],colors = ['yellowgreen', 'gold', 'lightskyblue'])
plt.title('score_range_pie_chart', fontsize=titlesize)
plt.xlabel('Score_range', fontsize=labelsize)
plt.tight_layout()
plt.show()