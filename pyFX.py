## grabs FX rate data for one month

from datetime import datetime
from forex_python.converter import get_rate
import matplotlib.pyplot as plt
import pandas as pd

rateUSD = 'USD' #input()
rate1 = 'GBP' #input()
rate2 = 'EUR' #input()
year = 2018 #input()
month = 8 #input()
dateList = []
rate1List = []
rate2List = []

for i in range(1,30):
    d = datetime(year, month, i)
    fx1 = get_rate(rate1, rateUSD, d)
    fx2 = get_rate(rate2, rateUSD, d)
    dateList.append(str(d))
    rate1List.append(fx1)
    rate2List.append(fx2)

forexDict = {'date': dateList, 
             'rate1': rate1List,
             'rate2': rate2List}
forexDF = pd.DataFrame.from_dict(data=forexDict)
forexDF['date'] = pd.to_datetime(forexDF['date'])
forexDF.set_index('date', inplace=True)

plt.plot(forexDF)
plt.xlabel('Date')
plt.xticks(rotation=60)
plt.ylabel('Currency to USD')
plt.title('FX Movement Against ' + rate1)
plt.legend([rate1, rate2])
plt.show()
