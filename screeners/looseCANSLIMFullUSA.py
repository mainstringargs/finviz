import os;
from finviz.screener import Screener

def get_screener_name():
    return 'looseCANSLIMFullUSA'

def dump_to_csv(dirName):


#http://freetraderchat.com/blog/can-slim-finvix-scan/

#https://finviz.com/screener.ashx?v=111&f=fa_epsqoq_o5,fa_salesqoq_o5,geo_usa,sh_instown_o10,ta_averagetruerange_o2.5,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4


    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filters = ['fa_epsqoq_o5','fa_salesqoq_o5','geo_usa','sh_instown_o10','ta_averagetruerange_o2.5','ta_sma20_pa','ta_sma200_pa','ta_sma50_pa']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='marketcap') 


    print((stock_list))
    stock_list.to_google_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')