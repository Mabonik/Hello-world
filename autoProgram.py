import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import collections

plt.style.use('ggplot')
data = pd.read_csv('auto-mpg.csv', sep=',')
count = len(data)

#(1)
col = list(data) + ['model']
ldata = data.values.tolist()

for i in range(count):
    ldata[i].append(ldata[i][len(ldata[i])-1].split(' ')[0])

data = pd.DataFrame(ldata, columns=col)


#
modelFreq = data['model'].value_counts().to_dict()  #функція для перетворення значення в словник.
originFreq = data['origin'].value_counts().to_dict()
mpgFreq = data['mpg'].value_counts().to_dict()
mpgFreq = collections.OrderedDict(sorted(mpgFreq.items()))


#за кількістю марок
fig, ax = plt.subplots()
fig.set_size_inches(13, 7)

ax.yaxis.grid(True)

plt.title('Графік по кількості марок')

barwidth = 0.75
xs = np.arange(0 ,len(modelFreq))
plt.bar(xs, modelFreq.values(), width=barwidth, color = ('plum'))

plt.xticks(xs, modelFreq.keys(), rotation = 90)

vals = list(modelFreq.values())

for i in range(len(modelFreq)):
    plt.text(x = xs[i]-0.5 , y = vals[i]+0.1, s = vals[i], size = 16)

plt.show()
#


#за походженням
fig, ax = plt.subplots()
fig.set_size_inches(7, 5)

ax.yaxis.grid(True)

plt.title('Графік по походженню')

barwidth = 0.75
xs = np.arange(0 ,len(originFreq))
plt.bar(xs, originFreq.values(), width=barwidth, color = ('mediumorchid'))

plt.xticks(xs, originFreq.keys())

vals = list(originFreq.values())

for i in range(len(originFreq)):
    plt.text(x = xs[i] , y = vals[i]+0.1, s = vals[i], size = 16)

plt.show()
#

#за споживанням
fig, ax = plt.subplots()
fig.set_size_inches(14, 7) #розмір розмітки

ax.yaxis.grid(True)

plt.title('Графік за споживанням')

barwidth = 0.5
xs = np.arange(0 ,len(mpgFreq))
plt.bar([x + 0.5 for x in xs], mpgFreq.values(), width=barwidth, color = ('plum'))

plt.xticks(np.arange(0 ,len(mpgFreq) + 1, len(mpgFreq)/15), mpgFreq.keys())

vals = list(mpgFreq.values())

plt.show()
#

#залежність потужності
cyl = data[['cyl', 'hp']].sort_values('cyl')

cylList = cyl['cyl'].unique()

maxVal = []
minVal = []
avgVal = []

for c in cylList:
    sliceData = cyl.loc[cyl['cyl'] == c]
    maxVal.append([c, sliceData[['hp']].max()])
    minVal.append([c, sliceData[['hp']].min()])
    avgVal.append([c, sliceData[['hp']].mean()])

fig, ax = plt.subplots()
fig.set_size_inches(7, 7)

ax.yaxis.grid(True)
ax.xaxis.grid(True)

plt.title('Залежність потужності від кількості цилідрів')

plt.scatter(cyl['cyl'].values, cyl['hp'].values, marker=".", color = ('plum'))
plt.plot(cylList, maxVal)
plt.plot(cylList, minVal)
plt.plot(cylList, avgVal,)
plt.show()


#залежність споживання
orig = data[['origin', 'mpg']]
origList = orig['origin'].unique()

maxVal = []
minVal = []
avgVal = []

for c in origList:
    sliceData = orig.loc[orig['origin'] == c]
    maxVal.append(sliceData[['mpg']].max())
    minVal.append(sliceData[['mpg']].min())
    avgVal.append(sliceData[['mpg']].mean())

fig, ax = plt.subplots()
fig.set_size_inches(10, 7)

ax.yaxis.grid(True)
ax.xaxis.grid(True)

plt.title('Залежність споживання від походження')

plt.scatter( orig['origin'].values, orig['mpg'].values, marker=".", color = ('plum'))
plt.plot( origList, maxVal)
plt.plot( origList, minVal)
plt.plot( origList, avgVal)
plt.show()

#графік за кількістю авто по роках
for o in origList:
    SliceData = data.loc[data['origin'] == o]
    avgweight = SliceData['weight'].mean()
    print ("Avarage weight of {:>10s} = {:.4f}".format(o, avgweight))

yearFreq = data['yr'].value_counts().to_dict()
yearFreq = collections.OrderedDict(sorted(yearFreq.items()))

fig, ax = plt.subplots()
fig.set_size_inches(12, 7)

ax.yaxis.grid(True)

plt.title('Графік кількості авто за роками')

barwidth = 0.5
xs = np.arange(0 ,len(yearFreq))
plt.bar([x + 0.5 for x in xs], yearFreq.values(), width=barwidth, color = ('plum'))

plt.xticks( [x + 0.5 for x in xs] , yearFreq.keys())

vals = list(yearFreq.values())

for i in range(len(yearFreq)):
    plt.text(x = xs[i] + 0.3 , y = vals[i]+0.15, s = vals[i], size = 16)

plt.show()





