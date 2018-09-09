## grabs FX rate data

from datetime import datetime
from forex_python.converter import get_rate
import matplotlib.pyplot as plt
import pandas as pd

rate1 = 'USD' #input()
rate2 = 'GBP' #input()
dateList = []
rateList = []

for i in range(1,11):
    d = datetime(2018, 8, i)
    fx = get_rate(rate1, rate2, d)
    dateList.append(str(d))
    rateList.append(fx)

forexDict = {'date': dateList, 'rate': rateList}
forexDF = pd.DataFrame.from_dict(data=forexDict)
forexDF['date'] = pd.to_datetime(forexDF['date'])
forexDF.set_index('date', inplace=True)

plt.plot(forexDF)
plt.xlabel('Date')
plt.xticks(rotation=60)
plt.ylabel(rate1 + ' to ' + rate2)
plt.title('FX Movement')
plt.show()
