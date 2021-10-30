import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt


sp500=pd.read_csv('S&P500.csv')

volatile_firms=[]
High=[]
Low=[]
HL=[]
Volume=[]
hl_avg=[]
vol_avg=[]
var=[volatile_firms, High, Low, HL, Volume, hl_avg, vol_avg]

for stock in sp500['Symbol']:
    stock=stock.upper()
    try:
        stock_info=yf.Ticker(stock)
        stock_hist=stock_info.history(period='11d')
        stock_hist['HL']=stock_hist['High']-stock_hist['Low']
        HL_avg=stock_hist['HL'].iloc[1:11:1].mean()
        Vol_avg=stock_hist['Volume'].iloc[1:11:1].mean()
        if stock_hist['HL'].iloc[-1]>HL_avg:
            volatile_firms.append(stock)
            hl_avg.append(HL_avg)
            vol_avg.append(Vol_avg)
            High.append(stock_hist['High'].iloc[-1])
            Low.append(stock_hist['Low'].iloc[-1])
            HL.append(stock_hist['HL'].iloc[-1])
            Volume.append(stock_hist['Volume'].iloc[-1])
    except:
        pass

volatile_firms_df=pd.DataFrame({
    'High':High,
    'Low':Low,
    'Today\'s High-Low':HL,
    'Average High-Low (last 10 days)':hl_avg,
    'Volume':Volume,
    'Average Volume (last 10 days)':vol_avg
}, index=volatile_firms
)
volatile_firms_df.index.name='Ticker'

volatile_firms_df.to_excel('Volatile SP500 List ('+str(dt.date.today())+').xlsx', sheet_name=str(dt.date.today()))
