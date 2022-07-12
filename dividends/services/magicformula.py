import requests
import pandas as pd
from ..utils.company import setor
from ..models import Company

def getCompaniesAndSectors(sector="zero"):
  try:
    agent = {"User-Agent":"Mozilla/5.0"}
    res = requests.get('https://fundamentus.com.br/resultado.php', headers=agent)
  except Exception as e:
    return False

  df = pd.read_html(res.content)[0]

  for coluna in list(df):
    if coluna != 'Papel':
      df[coluna] = df[coluna].astype(str).str.replace('.','')
      df[coluna] = df[coluna].astype(str).str.replace(',','.')
      df[coluna] = df[coluna].astype(str).str.rstrip('%').astype('float')/100

  df.drop(df[df['Liq.2meses'] < 1.0e6].index, inplace = True)
  df.drop(df[df['EV/EBIT']<=0].index, inplace = True)
  
  ranking = pd.DataFrame()
  ranking['pos'] = range(1,len(df))
  ranking['EV/EBIT'] = df.sort_values(by=['EV/EBIT'])['Papel'][:len(df)-1].values 
  ranking['ROIC'] = df.sort_values(by=['ROIC'],ascending=False)['Papel'][:len(df)-1].values

  a = ranking.pivot_table(columns='EV/EBIT',values='pos')
  b = ranking.pivot_table(columns='ROIC',values='pos')

  t = pd.concat([a,b])
  rank = t.dropna(axis=1).sum().sort_values().reset_index()

  rank.columns = ['abbreviation', 'posicao']

  ev = []

  roic = []

  nome = []

  s = []
  
  for index, row in rank.iterrows():
    ev.append( df[df['Papel'] == row['abbreviation']]['EV/EBIT'].values[0] )
    roic.append( round(df[df['Papel'] == row['abbreviation']]['ROIC'].values[0]*100.0,2) )
    
    company = Company.objects.get(abbreviation=row['abbreviation'])
    nome.append(company.name)
    s.append(company.sector)

  rank['sector'] = s

  rank['name'] = nome

  rank['ev'] = ev

  rank['roic'] = roic
  
  rank['id'] = rank.index
  
  if sector != "zero": 
    
    rank = rank[rank['sector']==sector]

    return rank.to_dict('records'), Company.objects.order_by('sector').exclude(sector='nan').values('sector').distinct()

  return rank.to_dict('records'), Company.objects.order_by('sector').exclude(sector='nan').values('sector').distinct()
