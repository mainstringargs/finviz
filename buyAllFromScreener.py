import os
import sys
import pandas as pd
from yahoo_fin import stock_info as si
import csv
from datetime import datetime, date, time, timedelta, timezone

import alpaca_trade_api as tradeapi
import pytz;
from yahoo_fin import stock_info as si
import time;

api = tradeapi.REST('XyZ','XYZ')

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

screenerName='looseCANSLIM'

if(len(sys.argv)>1):
    screenerName = sys.argv[1];
    
    
print("Using screenerName: "+screenerName);

maxStockPrice = 500.0;
account = api.get_account()

dir = 'screenerOutput'

print("Available Cash $"+account.cash);

        
def getfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    a.reverse()
    return a        
    
fileToUse = None;    
    
for file in getfiles(dir):
    if file.lower().startswith(screenerName.lower()) and file.lower().endswith(".csv") and int(file.lower().split('-')[1].replace('.csv',''))<120000:
        fileToUse = file;
        break;


frame = pd.read_csv(os.path.join(dir, fileToUse))

print("Ignoring these (More than $"+str(maxStockPrice)+":\n "+str(frame[frame.Price >= maxStockPrice][["Ticker","Price"]]))

frame = frame[frame.Price < maxStockPrice]

frame = frame.sort_values(by=['Price'], ascending=False)

print("\nBuying these (Less than $"+str(maxStockPrice)+":\n "+str(frame[frame.Price < maxStockPrice][["Ticker","Price"]]))

print("Total Potential Cost: "+str(frame["Price"].sum(axis=0)));

def buy_stock(ticker, price ):
    account = api.get_account();
    cash = account.cash;
    if(float(price) < float(cash)):
        print("Buying "+ticker + " "+str(price)+ " "+cash);
        
        (api.submit_order(
            ticker,
            1,
            'buy',
            'market',
            'day'
            ))

for maxNumberOfStock in range(1,5):      
    account = api.get_account(); 
    print("Available Cash $"+account.cash);
    
    for index, row in frame.iterrows():
        time.sleep(1)
        buy_stock(row['Ticker'], row['Price'])
    
    