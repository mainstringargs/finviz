import os;
from finviz.screener import Screener

def get_screener_name():
    return 'red'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

	#http://freetraderchat.com/blog/top-5-finviz-scans/
	#https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o200,sh_price_u10,ta_averagetruerange_o0.25,ta_change_d,ta_pattern_horizontal,ta_perf_ddown,ta_perf2_d5u&ft=4
	
    filters = ['sh_avgvol_o200','sh_price_u10','ta_averagetruerange_o0.25','ta_change_d','ta_pattern_horizontal','ta_perf_ddown','ta_perf2_d5u']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 


    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')