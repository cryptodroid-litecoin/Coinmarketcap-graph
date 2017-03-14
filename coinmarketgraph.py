import requests
import matplotlib.pyplot as plt

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

# Display the datas with matplotlib
fig = plt.figure()
ax = plt.gca()
ax.scatter(marketcap, volume, label = 'name')
ax.set_xscale('log')
ax.set_yscale('log')

# add legend for each coins
z = 0
for i in coinsnames:
    plt.annotate(i, xy=(marketcap[z], volume[z]), xycoords='data',
    xytext=(-20,20), textcoords='offset points',ha = 'right', va = 'bottom',
    bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
    arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    z += 1
    plt.xlabel('Market cap')
    plt.ylabel('Volume')

plt.show()
