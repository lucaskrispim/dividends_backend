import requests
import pandas as pd
from ..utils.company import setor
from ..models import Company,CompanyAndDividends
import yfinance as yf

def storeAllCompanies():

  try:
    agent = {"User-Agent":"Mozilla/5.0"}
    res = requests.get('https://fundamentus.com.br/resultado.php', headers=agent)
  except Exception as e:
    return

  df = pd.read_html(res.content)[0]

  for coluna in list(df):
    if coluna != 'Papel':
      df[coluna] = df[coluna].astype(str).str.replace('.','')
      df[coluna] = df[coluna].astype(str).str.replace(',','.')
      df[coluna] = df[coluna].astype(str).str.rstrip('%').astype('float') #/100

  df.drop(df[df['Div.Yield'] == 0.0].index, inplace = True)

  df.rename(columns={'Div.Yield':'dy','Cotação':'price'}, inplace=True)

  df['price'] = df['price']/100.0

  Company.objects.all().delete()
  i = 0
  for index, row in df.iterrows():
    a,b = setor(row['Papel'])
    company = Company(id=i,name=a,abbreviation=row['Papel'],sector=b,dy=row['dy'],price=row['price'])
    i=i+1
    #print(f"{i} {row['Papel']} {row['dy']} {row['price']}")
    company.save()


def storeDividendsByPeriodAndByCompany():

  try:
    agent = {"User-Agent":"Mozilla/5.0"}
    res = requests.get('https://fundamentus.com.br/resultado.php', headers=agent)
  except Exception as e:
    return

  df = pd.read_html(res.content)[0]  

  df.drop(df[df['Div.Yield'] == 0.0].index, inplace = True)

  CompanyAndDividends.objects.all().delete()
  i = 0
  for index, row in df.iterrows():
    a,b = setor(row['Papel'])
    try:
      data1 = yf.Ticker(row['Papel']+".SA").history(period='1y')
      data3 = yf.Ticker(row['Papel']+".SA").history(period='3y')
      data5 = yf.Ticker(row['Papel']+".SA").history(period='5y')

      company = CompanyAndDividends(id=i,abbreviation=row['Papel'],
                                    dy1= data1[data1['Dividends'] != 0.0]['Dividends'].sum()/data1['Close'].iloc[-1],
                                    dy3= data3[data3['Dividends'] != 0.0]['Dividends'].sum()/data3['Close'].iloc[-1],
                                    dy5= data5[data5['Dividends'] != 0.0]['Dividends'].sum()/data5['Close'].iloc[-1],
                                    r1= data1[data1['Dividends'] != 0.0]['Dividends'].sum()/data1['Close'].iloc[0],
                                    r3= data3[data3['Dividends'] != 0.0]['Dividends'].sum()/data3['Close'].iloc[0],
                                    r5= data5[data5['Dividends'] != 0.0]['Dividends'].sum()/data5['Close'].iloc[0]
                                    )
      company.save()
      i=i+1
    except Exception as e:
      print("Erro") 

