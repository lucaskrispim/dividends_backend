import requests
import pandas as pd
import yfinance as yf
from ..utils import calc_rsi
from datetime import date

def getRsiByCompanyData(papel,window=14,period=15):

  data = None

  try:

    data = yf.Ticker(papel+".SA").history(period="1y")
    
    data['data'] = data.index

    data = data[(data.T != 0).any()]

    data['rsi'] = calc_rsi(data = data.copy(), column='Close', window=window)

    data = data[data.index >= f'{date.today().year}-{date.today().month}-{date.today().day-period}']

  except Exception as e:
    print(f"Erro {e} {papel}") 

  data.rename(columns={'data': 'x'}, inplace=True)

  return data[['x','rsi']].to_dict('records')