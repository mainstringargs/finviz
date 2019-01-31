import os;
from finviz.screener import Screener

def get_screener_name():
    return 'greenPlus15'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

	#http://freetraderchat.com/blog/top-5-finviz-scans/
	#https://finviz.com/screener.ashx?v=111&f=sh_curvol_o200,sh_price_u10,ta_change_u,ta_changeopen_u,ta_perf_dup,ta_perf2_d15o&ft=4

    filters = ['sh_curvol_o200','sh_price_u10','ta_change_u','ta_changeopen_u','ta_perf_dup','ta_perf2_d15o']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 


    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')