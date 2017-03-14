import requests
import numpy as np
import matplotlib.pyplot as plt

def query():
    url = 'https://api.coinmarketcap.com/v1/ticker'
    req = requests.get(url)
    response = req.json()
    return response

alldat = query()
absc = []
ordn = []
labels = []
data = []
for i in alldat:
    if i['24h_volume_usd'] != None:
        i['24h_volume_usd'] = float(i['24h_volume_usd'])
        if i['24h_volume_usd'] > 1000:
            absc.append(i['market_cap_usd'])
            ordn.append(i['24h_volume_usd'])
            labels.append(i['name'])

abscX = np.asmatrix(absc)
ordnX = np.asmatrix(ordn)
labelsX = np.asmatrix(labels)
labelsX = np.transpose(labelsX)
data = np.r_[abscX[None,:],ordnX[None,:]]
data = np.transpose(data)

fig = plt.figure()
ax = plt.gca()
ax.scatter(absc, ordn, label = 'name')
ax.set_xscale('log')
ax.set_yscale('log')

z = 0
for i in labels:
    plt.annotate(i, xy=(absc[z], ordn[z]), xycoords='data',
    xytext=(-20,20), textcoords='offset points',ha = 'right', va = 'bottom',
    bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
    arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    z += 1
    plt.xlabel('Market cap')
    plt.ylabel('Volume')

plt.show()