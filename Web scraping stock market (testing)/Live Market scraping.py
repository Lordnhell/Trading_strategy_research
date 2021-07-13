import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import statistics

headers = {
    'User-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

starttime = time.time()
data = {'Time_stamp' : [], 'mark_close' : [],'MA20':[],'MA50':[],'MA100':[],'MA200':[]}
ma20 = 0
df = pd.DataFrame(data)

def MA_calc(new_price,days):
    df_len = int(len(df))
    ma_days = 0
    if df_len >= days:
        ma_days = (new_price + df.loc[df_len - (days - 1):df_len,'mark_close'].sum()) / days
    return round(ma_days,2)
        
            

def current_price_caller(share_code):
    url = 'https://finance.yahoo.com/quote/' + share_code + '/'
    r = requests.get(url,{'headers':headers})
    soup = bs4.BeautifulSoup(r.text,'html.parser')
    result = soup.find_all('div',{'class' : 'D(ib) Mend(20px)'})[0].find('span').text
    result = result .replace(',','')
    result = float(result)
    return result

while True:
    price = current_price_caller('tsla')
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    
    MA20 = MA_calc(price,20)
    MA50 = MA_calc(price,50)
    MA100 = MA_calc(price,100)
    MA200 = MA_calc(price,200)
    
    append_list = [now,price,MA20,MA50,MA100,MA200]
    df.loc[len(df)] = append_list
    print(append_list)
    
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
