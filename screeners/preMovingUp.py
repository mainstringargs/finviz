import os;
from finviz.screener import Screener

def get_screener_name():
    return 'preMovingUp'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filters = ['sh_curvol_o200','sh_price_u7','sh_relvol_o1.5','sh_short_low','ta_rsi_nos50','ta_sma20_pa','ta_sma200_pa','ta_sma50_pa']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 

    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')