import requests
from bs4 import BeautifulSoup
import pandas as pd

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=8.9,image/webp,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'Cache-Control':'max-age=0'
}
base_url="https://www.coingecko.com/"


tables = []
for i in range(1,4):
    print('Processing page {0}'.format(i))
    params={
        'page':i
    }
    response = requests.get(base_url,headers=headers, params=params)
    soup = BeautifulSoup(response.content,'html.parser')
    tables.append(pd.read_html(str(soup))[0])

master_table = pd.concat(tables)
master_table = master_table.loc[:,master_table.columns[1:-1]]
master_table.to_csv("CryptoPrices.csv",index=False)

