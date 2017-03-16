import requests
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from numpy.linalg import lstsq

# Get datas from coinmarketcap api
def query():
    req = requests.get('https://api.coinmarketcap.com/v1/ticker')
    response = req.json()
    return response

# select coins with a daily volume above 10K $
alldata = query()
marketcap = []
volume = []
coinsnames = []
pchange24 = []
data = []
for i in alldata:
    if i['24h_volume_usd'] != None:
        i['24h_volume_usd'] = float(i['24h_volume_usd'])
        if i['market_cap_usd'] != None:
            i['market_cap_usd'] = float(i['market_cap_usd'])
            if i['24h_volume_usd'] > 10000:
                marketcap.append(i['market_cap_usd'])
                volume.append(i['24h_volume_usd'])
                coinsnames.append(i['name'])
                pchange24.append(i['percent_change_24h'])

# Display the datas with matplotlib
fig = plt.figure()
ax = plt.gca()
ax.scatter(marketcap, volume, label = 'name')
ax.set_xscale('log')
ax.set_yscale('log')

# add the name for each coins and colors code for marketcap change for the last 24h
def anotate(c):
        plt.annotate(coinsnames[z], xy=(marketcap[z], volume[z]), xycoords='data',
        xytext=(-20,20), textcoords='offset points',ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = c, alpha = 0.25),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
z = 0
for i in pchange1h:
    i = float(i)
    if i >= 0:
        anotate('green')
    elif i < 0:
        anotate('red')
    z += 1

green_patch = mpatches.Patch(color='green', alpha = 0.25, label='up for the last 24h')
red_patch = mpatches.Patch(color='red', alpha = 0.25, label='down for the last 24h')
plt.legend(loc='upper left', handles=[green_patch, red_patch])
plt.xlabel('Market cap')
plt.ylabel('Volume')
plt.show()
