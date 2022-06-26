import requests
import pandas as pd

def setor(papel):
  try:
    agent = {"User-Agent":"Mozilla/5.0"}
    res = requests.get(f'https://fundamentus.com.br/detalhes.php?papel={papel}', headers=agent)
    df = pd.read_html(res.content)[0]

    return df.iloc[2][1],df.iloc[3][1]
  except Exception as e:
    return 'nan'