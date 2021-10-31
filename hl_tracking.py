import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt

sp500=pd.read_csv('S&P500.csv')

volatile_firms=[]
high=[]
low=[]
hl=[]
volume=[]
hl_avg=[]
vol_avg=[]

for stock in sp500['Symbol']:
    stock=stock.upper()
    try:
        stock_info=yf.Ticker(stock) #try-except whether the ticker in the data matches the ticker in yfinance
        stock_hist=stock_info.history(period='11d') #access market history within 11 days of the given Ticker. Columns: 'High', 'Low', 'Dividends','Split','Volume'
        stock_hist['HL']=stock_hist['High']-stock_hist['Low']
        HL_avg=stock_hist['HL'].iloc[1:11:1].mean()
        Vol_avg=stock_hist['Volume'].iloc[1:11:1].mean()
        if stock_hist['HL'].iloc[-1]>HL_avg:
            volatile_firms.append(stock)
            hl_avg.append(HL_avg)
            vol_avg.append(Vol_avg)
            high.append(stock_hist['High'].iloc[-1])
            low.append(stock_hist['Low'].iloc[-1])
            hl.append(stock_hist['HL'].iloc[-1])
            volume.append(stock_hist['Volume'].iloc[-1])
    except:
        pass

volatile_firms_df=pd.DataFrame({
    'High':high,
    'Low':low,
    'Today\'s High-Low':hl,
    'Average High-Low (last 10 days)':hl_avg,
    'Volume':volume,
    'Average Volume (last 10 days)':vol_avg
}, index=volatile_firms
)
volatile_firms_df.index.name='Ticker'

volatile_firms_df.to_excel('Volatile SP500 List ('+str(dt.date.today())+').xlsx', sheet_name=str(dt.date.today()))
