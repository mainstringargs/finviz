import os
import sys
import pandas as pd
from yahoo_fin import stock_info as si
import csv
import datetime

now = datetime.datetime.now()

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

inputDate = sys.argv[1];
print("Using input date: "+inputDate);

dir = 'screenerOutput'

dirName = 'priceChanges'

if not os.path.exists(dirName):
	os.makedirs(dirName)


outputFile = 'priceChanges_'+inputDate.replace('-','')+"_"+str(now.year)+str(now.month)+str(now.day)+".csv";


with open(os.path.join(dirName, outputFile),'w', newline='') as outcsv:
    writer = csv.writer(outcsv, delimiter=',',quoting=csv.QUOTE_ALL)
    writer.writerow(['Screener','Ticker','Screener Cost','Current Price','Difference'])


    for file in os.listdir(dir):
        if file.endswith(".csv") and inputDate.replace('-','') in file:
	        screenerName = file.split('_')[0];
	        print("");				
	        print("ScreenerName "+screenerName);
	        print("");		
	        frame = pd.read_csv(os.path.join(dir, file))
	        frame = frame.sort_values('Ticker')
		
	        totalChange = 0;
	        totalInitialCost = 0;
	        totalCurrentPrice = 0;			
		
	        for index, row in frame.iterrows():
		        try:
	                 ticker = row['Ticker']
	                 screenerPrice = row['Price']
	                 currentPrice = si.get_live_price(ticker)
	                 print(ticker + " "+'{:.2f}'.format(screenerPrice) + " "+'{:.2f}'.format(currentPrice) + " " +'{:.2f}'.format(currentPrice - screenerPrice))
	                 totalChange = totalChange + (currentPrice - screenerPrice)
	                 totalInitialCost = totalInitialCost + screenerPrice;
	                 totalCurrentPrice = totalCurrentPrice + currentPrice;					 
	                 writer.writerow([screenerName,ticker,'{:.2f}'.format(screenerPrice),'{:.2f}'.format(currentPrice),'{:.2f}'.format(currentPrice - screenerPrice)])
		        except:
			         print("Exception"); 
	        print("");				
	        print("Total Change for "+screenerName + " "+'{:.2f}'.format(totalChange));
	        print("Total Screener Cost for "+screenerName + " "+'{:.2f}'.format(totalInitialCost));
	        print("Total Current Cost for "+screenerName + " "+'{:.2f}'.format(totalCurrentPrice));			
	        writer.writerow([screenerName,"TOTAL",'{:.2f}'.format(totalInitialCost),'{:.2f}'.format(totalCurrentPrice),'{:.2f}'.format(totalChange)])
	        writer.writerow([""])
	        print("============================");

		

