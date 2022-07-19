import requests
import pandas as pd
import yfinance as yf
from datetime import date

def getCandleStickByCompanyData(papel,period=15):

  data = None

  try:

    data = yf.Ticker(papel+".SA").history(period=f"{period}"+"d")
    
    data = data[(data.T != 0).any()]

    data['data'] = data.index

  except Exception as e:
    print(f"Erro {papel}") 

  candleList = []

  for item in data.to_dict('records'):
    if item['Open'] > 0.0 and item['High'] > 0.0 and item['Low'] > 0.0 and item['Close'] > 0.0:
      candleList.append({
        'x': item.pop('data', None),
        'y': [round(x,2) for x in [item['Open'],item['High'],item['Low'],item['Close']]]
      })

  return candleList


def getDividendsByCompanyData(papel,period=1):

  data = None

  try:

    data = yf.Ticker(papel+".SA").history(period='max')
    
    data['data'] = data.index

    dataDividesnds = data[data.index >= f'{date.today().year-period}-{date.today().month}-{date.today().day}']
    dataDividesnds = dataDividesnds[dataDividesnds['Dividends'] > 0.0]

  except Exception as e:
    print(f"Erro {e} {papel}") 

  return dataDividesnds.to_dict('records')