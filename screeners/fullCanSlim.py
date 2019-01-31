import os;
from finviz.screener import Screener

def get_screener_name():
    return 'fullCanSlim'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

	#http://freetraderchat.com/blog/top-5-finviz-scans/
	#https://finviz.com/screener.ashx?v=111&f=cap_midunder,fa_epsqoq_o5,fa_salesqoq_o5,sh_instown_o10,sh_price_u5,ta_averagetruerange_o0.25,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4

    filters = ['cap_midunder','fa_epsqoq_o5','fa_salesqoq_o5','sh_instown_o10','sh_price_u5','ta_averagetruerange_o0.25','ta_sma20_pa','ta_sma200_pa','ta_sma50_pa']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 


    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')