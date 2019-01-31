import os;
from finviz.screener import Screener

def get_screener_name():
    return 'oversoldStocksBouncingAtTechnicalSupport'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

	#	https://www.intelligenttrendfollower.com/how-to-find-trend-following-stock-ideas-on-finviz/
	#https://finviz.com/screener.ashx?v=111&f=ta_pattern_tlsupport2,ta_rsi_os40&ft=3?a=128563647

    filters = ['ta_pattern_tlsupport2','ta_rsi_os40']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 


    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')